import numpy as np
import datetime
import scipy
import pathlib
import copy
from scipy import interpolate

from pymsis import msis

from geospacelab.datahub import DataHub
from geospacelab.datahub import DatasetUser


import geospacelab.visualization.mpl.dashboards as dashboards
import geospacelab.observatory.earth.geodesy as gd
from geospacelab.observatory.orbit.utilities import LEOToolbox


class MSISDataset(DatasetUser):
    
    def __init__(self, dt_fr, dt_to, msis_version=2, **kwargs):
        self.msis_version = msis_version
        
        super().__init__(dt_fr, dt_to, **kwargs)
        self.visual = 'on'
        
    def get_along_track_output(self, ds_sc):
        dt_fr_1 = self.dt_fr - datetime.timedelta(days=100)
        dt_to_1 = self.dt_fr + datetime.timedelta(days=100)
        dh = DataHub(self.dt_fr, self.dt_to)
        ds_f107 = dh.dock(datasource_contents=['gfz', 'snf107'], dt_fr=dt_fr_1, dt_to=dt_to_1)
        ds_kpap = dh.dock(datasource_contents=['gfz', 'kpap'], dt_fr=dt_fr_1, dt_to=dt_to_1)
        
        dts =  ds_sc['SC_DATETIME'].flatten()
        glats = ds_sc['SC_GEO_LAT'].flatten()
        glons = ds_sc['SC_GEO_LON'].flatten()
        galts = ds_sc['SC_GEO_ALT'].flatten()
        
        f107_dts = ds_f107['DATETIME'].flatten()
        f107_data = ds_f107['F107_ADJ'].flatten()
        from scipy.signal import savgol_filter
        f107a_data = savgol_filter(f107_data, 81, 1)
        # f107a_data = np.convolve(f107_data, np.ones(81), 'valid') / 81 
        
        ap_dts = ds_kpap['DATETIME'].flatten()
        ap_data = ds_kpap['ap'].flatten()
        Ap_data = ds_kpap['Ap'].flatten() 
        rho_sc = np.empty((0, 1))
        alt_at = np.arange(200, 610, 10,)
        rho_at_grid = np.empty((0, alt_at.shape[0]))
        for (dt, glat, glon, alt) in zip(dts, glats, glons, galts):
            
            ind_t = np.where(f107_dts == datetime.datetime(dt.year, dt.month, dt.day, 0))[0]
            f107 = f107_data[ind_t]
            f107a = f107_data[ind_t] 
            
            diff_sectime = np.array([(t - dt).total_seconds() for t in ap_dts])
            ind_t = np.where(np.abs(diff_sectime) == np.min(np.abs(diff_sectime)))[0][-1] 
            aps = [[
                Ap_data[ind_t],
                ap_data[ind_t],
                ap_data[ind_t-1],
                ap_data[ind_t-2], 
                ap_data[ind_t-3],
                np.mean(ap_data[ind_t-11:ind_t-3]),
                np.mean(ap_data[ind_t-19:ind_t-11]), 
            ]]
            
            output = msis.run(dt, glon, glat, alt, f107, f107a, aps, version=self.msis_version)
            output = np.squeeze(output)
            rho_sc = np.vstack((rho_sc, np.array([output[0]])))
            
            output = msis.run(dt, glon, glat, alt_at, f107, f107a, aps, version=self.msis_version) 
            output = np.squeeze(output).T
            rho_at_grid = np.vstack((rho_at_grid, output[0, :])) 
            
        
        self['SC_DATETIME'] = ds_sc['SC_DATETIME'].clone()
        
        var = self.add_variable(var_name='ALT_AT_GRID')
        var.value = alt_at
        
        var = ds_sc['rho_n'].clone()
        self['rho_n_SC'] = var
        var.value = rho_sc
        
        var = self.add_variable(var_name='rho_n_AT_GRID')
        var.value = rho_at_grid
        var.label = ds_sc['rho_n'].label
        var.unit = ds_sc['rho_n'].unit
        var.depends = {
            0: {'UT': 'SC_DATETIME'},
            1: {'ALT': 'ALT_AT_GRID'},
        }
        

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
        variable_names=variable_names)
    for var_name in variable_names:
        ds_sc[var_name + '_AVG'] = ds_leo[var_name + '_AVG']
        ds_sc[var_name + '_RSD'] = ds_leo[var_name + '_RSD']
        ds_sc[var_name + '_RSD_PERC'] = ds_leo[var_name + '_RSD_PERC']

    return ds_sc


if __name__ == '__main__':
    
    sat_name = 'grace'
    sat_id = 'A'
    product = 'dns_acc'
    
    dt_fr = datetime.datetime(2016, 3, 14)
    dt_to = datetime.datetime(2016, 3, 21)
    dh_sc = DataHub(dt_fr, dt_to, visual='on')
    ds_sc = dh_sc.dock(datasource_contents=['tud', sat_name, product], sat_id=sat_id, product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_msis = MSISDataset(dt_fr, dt_to)
    
    ds_msis.get_along_track_output(ds_sc)
    
    import pickle
    data = {
        'MSIS_rho_n_sc': ds_msis['rho_n_SC'].value,
        'MSIS_rho_n_AT_GRID': ds_msis['rho_n_AT_GRID'].value,
        'MSIS_SC_DATETIME': ds_msis['SC_DATETIME'].value, 
        'MSIS_ALT_AT_GRID': ds_msis['ALT_AT_GRID'].value,  
        }
    
    fp = pathlib.Path('/home/lei/01-Work/01-Project/OY20-ISSI_IT/Event_201603/') / \
        ('MSIS_' + sat_name + '_' + sat_id + '_' + product + '_' + \
        dt_fr.strftime("%Y%m%d_%H%M") + '-' + dt_to.strftime("%Y%m%d_%H%M") + '.pickle')
    with open(fp, 'wb') as handle:
        pickle.dump(data, handle)
    
    
    