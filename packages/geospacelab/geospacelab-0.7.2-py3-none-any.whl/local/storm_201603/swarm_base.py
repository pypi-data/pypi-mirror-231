import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib

from geospacelab import preferences as pref

# pref.user_config['visualization']['mpl']['style'] = 'dark'  # or 'light'

import geospacelab.visualization.mpl.dashboards as dashboards
import geospacelab.observatory.earth.geodesy as gd
from geospacelab.observatory.orbit.utilities import LEOToolbox


class SCAnalysisBase(dashboards.TSDashboard):

    def __init__(self, dt_fr=None, dt_to=None, sat_id='AB', add_APEX=True, add_AACGM=True,
                 figure='new', figure_config={'figsize': (12, 8)}, **kwargs):
        if dt_fr is None:
            dt_fr = datetime.datetime(2016, 2, 2, 0)
        if dt_to is None:
            dt_to = datetime.datetime(2016, 2, 4, 0)

        super().__init__(dt_fr=dt_fr, dt_to=dt_to, figure=figure, figure_config=figure_config, **kwargs)
        self.ds_sectors = None

    def group_by_sector(
            self,
            ds_sc=None,
            sector_name='N', variable_names=None,
            boundary_lat=None, sector_cs=None,
            x_grid_res=20 * 60, y_grid_res=0.5):
        ds_leo = LEOToolbox(self.dt_fr, self.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.group_by_sector(sector_name=sector_name, boundary_lat=boundary_lat, sector_cs=sector_cs)
        ds_leo.griddata_by_sector(sector_name=sector_name, variable_names=variable_names,
                                  x_grid_res=x_grid_res, y_grid_res=y_grid_res)

        self.add_dataset(ds_leo, kind='user-defined')
        self.ds_sectors = self.get_current_dataset()
        return ds_leo

    def smooth_along_track(self, ds_sc=None, variable_names=None, time_window=450., time_res=10.):
        # ds_sc = getattr(self, 'ds_' + sat_id.upper())
        ds_leo = LEOToolbox(self.dt_fr, self.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.smooth_along_track(
            time_window=time_window, time_res=time_res,
            variable_names=variable_names)
        for var_name in variable_names:
            ds_sc[var_name + '_AVG'] = ds_leo[var_name + '_AVG']
            ds_sc[var_name + '_RSD'] = ds_leo[var_name + '_RSD']
            ds_sc[var_name + '_RSD_PERC'] = ds_leo[var_name + '_RSD_PERC']

        return

class GraceAnalysisDNSACC(dashboards.TSDashboard):

    def __init__(self, dt_fr=None, dt_to=None, sat_id='AB', add_APEX=True, add_AACGM=True,
                 figure='new', figure_config={'figsize': (12, 8)}, **kwargs):
        if dt_fr is None:
            dt_fr = datetime.datetime(2016, 2, 2, 0)
        if dt_to is None:
            dt_to = datetime.datetime(2016, 2, 4, 0)

        super().__init__(dt_fr=dt_fr, dt_to=dt_to, figure=figure, figure_config=figure_config, **kwargs)
        self.ds_sectors = None

        if 'A' in sat_id:
            self.ds_A = self.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='A', product_version='v02',
                                  add_APEX=add_APEX, add_AACGM=add_AACGM)

        if 'B' in sat_id:
            self.ds_B = self.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='B', product_version='v02',
                                  add_APEX=add_APEX, add_AACGM=add_AACGM)

        self.ds_asysym = self.dock(datasource_contents=['wdc', 'asysym'])
        self.ds_ae = self.dock(datasource_contents=['wdc', 'ae'])

    def group_by_sector(
            self,
            sat_id='A',
            sector_name='N', variable_names=None,
            boundary_lat=None, sector_cs=None,
            x_grid_res=20 * 60, y_grid_res=0.5):
        ds_sc = getattr(self, 'ds_' + sat_id.upper())
        ds_leo = LEOToolbox(self.dt_fr, self.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.group_by_sector(sector_name=sector_name, boundary_lat=boundary_lat, sector_cs=sector_cs)
        ds_leo.griddata_by_sector(sector_name=sector_name, variable_names=variable_names,
                                  x_grid_res=x_grid_res, y_grid_res=y_grid_res)

        self.add_dataset(ds_leo, kind='user-defined')
        self.ds_sectors = self.get_current_dataset()
        return ds_leo

    def smooth_along_track(self, sat_id='A', variable_names=None, time_window=450., time_res=10.):
        ds_sc = getattr(self, 'ds_' + sat_id.upper())
        ds_leo = LEOToolbox(self.dt_fr, self.dt_to)
        ds_leo.clone_variables(ds_sc)
        ds_leo.smooth_along_track(
            time_window=time_window, time_res=time_res,
            variable_names=variable_names)
        for var_name in variable_names:
            ds_sc[var_name + '_AVG'] = ds_leo[var_name + '_AVG']
            ds_sc[var_name + '_RSD'] = ds_leo[var_name + '_RSD']
            ds_sc[var_name + '_RSD_PERC'] = ds_leo[var_name + '_RSD_PERC']

        return

    def calc_diff_AB_by_time(self):
        rho_A = self.ds_A['rho_n']
        rho_B = self.ds_B['rho_n']
        lat_A = self.ds_A['SC_GEO_LAT']
        lat_B = self.ds_B['SC_GEO_LAT']
        diff_rho = rho_A.clone()
        diff_rho_abs = rho_A.clone()
        diff_rho.value = (rho_B.value - rho_A.value) * np.sign(lat_B.value - lat_A.value)
        diff_rho_abs.value = np.abs(rho_B.value - rho_A.value)
        diff_rho.label = r'$\Delta\rho_n$'
        diff_rho_abs.label = r'$|\Delta\rho_n|$'
        self.ds_A['DIFF_rho_n'] = diff_rho
        self.ds_A['DIFF_rho_n_ABS'] = diff_rho_abs

        diff_rho_perc = rho_A.clone()
        diff_rho_perc.value = np.abs(rho_B.value - rho_A.value) / rho_A.value * 100
        diff_rho_perc.label = r'$|\Delta\rho_n|/\rho_n^A$*100'
        diff_rho_perc.unit = '%'
        diff_rho_perc.unit_label = None
        self.ds_A['PERC_DIFF_rho_n_ABS'] = diff_rho_perc

        diff_rho_perc = rho_A.clone()
        diff_rho_perc.value = (rho_B.value - rho_A.value) * np.sign(lat_B.value - lat_A.value) / rho_A.value * 100
        diff_rho_perc.label = r'$\Delta\rho_n/\rho_n^A$*100'
        diff_rho_perc.unit = '%'
        diff_rho_perc.unit_label = None
        self.ds_A['PERC_DIFF_rho_n'] = diff_rho_perc

    def calc_d_between_A_and_B(self):
        ds_A = self.ds_A
        ds_B = self.ds_B

        glat_1 = ds_A['SC_GEO_LAT'].value
        glon_1 = ds_A['SC_GEO_LON'].value
        alt_1 = ds_A['SC_GEO_ALT'].value

        glat_2 = ds_B['SC_GEO_LAT'].value
        glon_2 = ds_B['SC_GEO_LON'].value
        alt_2 = ds_B['SC_GEO_ALT'].value

        r = 6371 + np.nanmean(alt_1.flatten())

        d = gd.calc_great_circle_distance(glat_1, glon_1, glat_2, glon_2, r=r)

        D = self.ds_A.add_variable(var_name='d_AB', value=d)
        D.unit = 'km'
        D.visual.axis[1].unit = 'km'
        D.visual.plot_config.style = '1noE'
        return D

    def quicklook_single_measurements(
            self, sat_id='A', sc_alt_lim=[340, 510],
            figure_config={'figsize': (12, 8)}, db_layout_config=dict(),
            save_fig=False, file_dir=None, file_name=None):
        db = dashboards.TSDashboard(
            dt_fr=self.dt_fr, dt_to=self.dt_to, figure='new',
            figure_config=figure_config)
        ds = getattr(self, 'ds_' + sat_id)
        rho = ds['rho_n']

        glat = self.assign_variable('SC_GEO_LAT', dataset=ds)
        glat.visual.axis[2].label = 'GRACE-' + sat_id

        glon = self.assign_variable('SC_GEO_LON', dataset=ds)

        alt = self.assign_variable('SC_GEO_ALT', dataset=ds)
        alt.unit = 'km'
        alt.label = 'h'
        alt.visual.axis[1].lim = sc_alt_lim
        alt.visual.plot_config.line = {'linestyle': '', 'marker': '.'}

        lst = self.assign_variable('SC_GEO_LST', dataset=ds)
        lst.label = 'LST'
        lst.visual.axis[1].lim = [0, 24]
        lst.visual.plot_config.line = {'linestyle': '', 'marker': '.'}

        glon.visual.axis[1].label = 'GLON'

        flag = self.assign_variable('FLAG', dataset=ds)

        # Dock the dataset for the geomagnetic activity indices.
        sym_h = self.assign_variable('SYM_H', dataset=self.ds_asysym)
        ae = self.assign_variable('AE', dataset=self.ds_ae)

        panel_layouts = [[sym_h, [ae]], [rho], [glat], [alt], [glon, [lst]], [flag]]
        db.set_layout(panel_layouts=panel_layouts, **db_layout_config)
        db.draw()
        if save_fig:
            db.save_figure(file_dir=file_dir, file_name=file_name)

        db.show()