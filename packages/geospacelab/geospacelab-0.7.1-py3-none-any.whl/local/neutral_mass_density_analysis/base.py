import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib

from geospacelab import preferences as pref
import geospacelab.visualization.mpl as mpl
from geospacelab.datahub import DataHub

# pref.user_config['visualization']['mpl']['style'] = 'dark'  # or 'light'

import geospacelab.visualization.mpl.dashboards as dashboards
from geospacelab.visualization.mpl.dashboards import TSDashboard
from geospacelab.visualization.mpl.geomap.geodashboards import GeoDashboard
import geospacelab.observatory.earth.geodesy as gd
from geospacelab.observatory.orbit.utilities import LEOToolbox

# Set the file folder for the results
file_dir_root = pathlib.Path('/home/lei/01-Work/01-Project/OY20-ISSI_IT/Event_201603/')
file_dir_root = pathlib.Path(__file__).parent.resolve()


class NeutralMassDensityAnalysis(TSDashboard):
    def __init__(self, dt_fr=None, dt_to=None, figure='new', figure_config=None, **kwargs):
        super().__init__(dt_fr=dt_fr, dt_to=dt_to, figure=figure, figure_config=figure_config, **kwargs)
        
    def group_by_sc_sector(
            ds_sc=None,
            sector_name='N', variable_names=None,
            boundary_lat=None, sector_cs=None,
            x_grid_res=10 * 60, y_grid_res=0.25, along_track_interp=True):
        ds_leo = LEOToolbox(ds_sc.dt_fr, ds_sc.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.group_by_sector(sector_name=sector_name, boundary_lat=boundary_lat, sector_cs=sector_cs)
        ds_leo.griddata_by_sector(sector_name=sector_name, variable_names=variable_names, 
                                  along_track_interp= along_track_interp,
                                  x_grid_res=x_grid_res, y_grid_res=y_grid_res)
        return ds_leo
    
    def smooth_along_track(ds_sc=None, variable_names=None, time_window=450., time_res=10.):
        # ds_sc = getattr(self, 'ds_' + sat_id.upper())
        ds_leo = LEOToolbox(ds_sc.dt_fr, ds_sc.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.smooth_along_track(
            time_window=time_window, time_res=time_res,
            variable_names=variable_names, 
            )
        for var_name in variable_names:
            ds_sc[var_name + '_AVG'] = ds_leo[var_name + '_AVG']
            ds_sc[var_name + '_RSD'] = ds_leo[var_name + '_RSD']
            ds_sc[var_name + '_RSD_PERC'] = ds_leo[var_name + '_RSD_PERC']

        return ds_sc
    
    def calc_dual_sat_distance(ds_sc_1, ds_sc_2, var_name=None, label=None):

        glat_1 = ds_sc_1['SC_GEO_LAT'].flatten()
        glon_1 = ds_sc_1['SC_GEO_LON'].flatten()
        alt_1 = ds_sc_1['SC_GEO_ALT'].flatten()

        glat_2 = ds_sc_2['SC_GEO_LAT'].flatten()
        glon_2 = ds_sc_2['SC_GEO_LON'].flatten()
        alt_2 = ds_sc_2['SC_GEO_ALT'].faltten()

        r = 6371. + alt_1

        d = gd.calc_great_circle_distance(glat_1, glon_1, glat_2, glon_2, r=r)

        D = ds_sc_1.add_variable(var_name=var_name)
        D.label = label if label is not None else var_name
        D.value = d[:, np.newaxis]
        D.unit = 'km'
        D.visual.axis[1].unit = 'km'
        D.visual.axis[1].lim = [0,400]
        D.visual.plot_config.style = '1noE'
        return D  
    
    def calc_dual_sat_diff_density_with_time_shift(ds_sc_1, ds_sc_2,
        time_shift=35., t_res=10., 
        interp=True, **kwargs):

        if interp:
            ds_1 = ds_sc_1.interp_evenly()
            ds_2 = ds_sc_2.interp_evenly()
        else:
            ds_1 = ds_sc_1
            ds_2 = ds_sc_2 

        N = int(np.fix(time_shift/t_res))
        rho_shift = ds_1['rho_n'].flatten() - np.roll(ds_2['rho_n'].flatten(), N)
        d_rho_dt = (ds_1['rho_n'].flatten() - np.roll(ds_2['rho_n'].flatten(), N)) / time_shift

        var = ds_1['rho_n'].clone()
        ds_1['delta_rho_n'] = var
        var.value = rho_shift[:, np.newaxis]
        var.label = r'$\delta \rho_n$'

        var = ds_1['rho_n'].clone()
        ds_1['partial_deriv_rho_n'] = var
        var.value = d_rho_dt[:, np.newaxis]
        var.label = r'$\partial \rho_n / \partial t$'
        var.unit = 'kg m-3'
        var.unit_label = r'kg$\cdot$m$^{-3}$$\cdot$s$^{-1}$' 

        return ds_1

    def calc_dual_sat_diff_density(ds_sc_1, ds_sc_2, interp=False):
        
        if interp:
            ds_sc_1 = ds_sc_1.interp_evenly()
            ds_sc_2 = ds_sc_2.interp_evenly()
            
        rho_A = ds_sc_1['rho_n']
        rho_B = ds_sc_2['rho_n']
        lat_A = ds_sc_1['SC_GEO_LAT']
        lat_B = ds_sc_2['SC_GEO_LAT']
        diff_rho = rho_A.clone()
        diff_rho_abs = rho_A.clone()
        diff_rho.value = (rho_B.value - rho_A.value) * np.sign(lat_B.value - lat_A.value)
        diff_rho_abs.value = np.abs(rho_B.value - rho_A.value)
        diff_rho.label = r'$\Delta\rho_n$'
        diff_rho_abs.label = r'$|\Delta\rho_n|$'
        ds_sc_1['DIFF_rho_n'] = diff_rho
        ds_sc_2['DIFF_rho_n_ABS'] = diff_rho_abs

        diff_rho_perc = rho_A.clone()
        diff_rho_perc.value = np.abs(rho_B.value - rho_A.value) / rho_A.value * 100
        diff_rho_perc.label = r'$|\Delta\rho_n|/\rho_n^A$*100'
        diff_rho_perc.unit = '%'
        diff_rho_perc.unit_label = None
        ds_sc_1['PERC_DIFF_rho_n_ABS'] = diff_rho_perc
        
        diff_rho_perc = rho_A.clone()
        diff_rho_perc.value = (rho_B.value - rho_A.value) * np.sign(lat_B.value - lat_A.value) / rho_A.value * 100
        diff_rho_perc.label = r'$\Delta\rho_n/\rho_n^A$*100'
        diff_rho_perc.unit = '%'
        diff_rho_perc.unit_label = None
        ds_sc_1['PERC_DIFF_rho_n'] = diff_rho_perc
        return ds_sc_1
    
    