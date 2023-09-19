import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib

from geospacelab import preferences as pref

# pref.user_config['visualization']['mpl']['style'] = 'dark'  # or 'light'

import geospacelab.visualization.mpl.dashboards as dashboards
import geospacelab.observatory.earth.geodesy as gd
from geospacelab.observatory.orbit.utilities import LEOToolbox

def test_grace_acc():
    # Set the starting and stopping time
    dt_fr = datetime.datetime(2016, 1, 31, 0)
    dt_to = datetime.datetime(2016, 2, 4, 23, 59)
    add_APEX = True  # if True, "SC_APEX_LAT" and "SC_APEX_LON" will be added, default is False

    # Create a dashboard object, equivalent to a datahub object, however, with the additional visulization control.
    db = dashboards.TSDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (12, 12)})

    # Dock the datasets. Different datasets store different types of data.
    # Dock the SWARM-A DNS-POD data
    ds_A = db.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='A', product_version='v02',
                   add_APEX=add_APEX)
    # Dock the SWARM-C DNS-POD data
    ds_B = db.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='B', product_version='v02',
                   add_APEX=add_APEX)
    # Dock the ASYSYM dataset
    ds_sym = db.dock(datasource_contents=['wdc', 'asysym'])
    # Dock the AE dataset
    ds_ae = db.dock(datasource_contents=['wdc', 'ae'])
    # Dock the Kp dataset
    ds_kp = db.dock(datasource_contents=['gfz', 'kpap'])  
    
    # Assign variables from the datasets for plotting
    rho_n_A = ds_A['rho_n']
    rho_n_B = ds_B['rho_n']
    rho_n_A.visual.axis[1].label = r'$\rho$'
    rho_n_A.visual.axis[2].label = 'GRACE-A'
    rho_n_B.visual.axis[2].label = 'GRACE-B'

    glat_A = ds_A['SC_GEO_LAT']
    glat_B = ds_B['SC_GEO_LAT']
    glat_A.visual.axis[2].label = 'GRACE-A'
    glat_B.visual.axis[2].label = 'GRACE-B'

    glon_A = db.assign_variable('SC_GEO_LON', dataset=ds_A)
    glon_B = db.assign_variable('SC_GEO_LON', dataset=ds_B)
    lst_A = db.assign_variable('SC_GEO_LST', dataset=ds_A)

    glon_A.visual.axis[2].label = 'GRACE-A'
    glon_B.visual.axis[2].label = 'GRACE-C'
    
    alt = ds_A['SC_GEO_ALT']
    alt.unit = 'km'
    alt.label = 'h'
    alt.visual.axis[1].lim = [340, 420]
    alt.visual.axis[1].unit = '@v.unit'
    alt.visual.plot_config.line = {'linestyle': '', 'marker': '.'} 
    
    flag = ds_A['FLAG']
    
    sym_h = ds_sym['SYM_H']
    ae = ds_ae['AE']
    kp = ds_kp['Kp']

    # Set the plotting layout
    db.set_layout([[sym_h, [ae]], [rho_n_A, rho_n_B], [glat_A, glat_B], [alt], [glon_A, [lst_A]], [flag], [kp]])
    db.draw()
    # db.savefig(file_name='xxx.png', file_dir='xxx/xxx')
    
    db.show()
    
    # Extract the data array from variables:
    rho_n_arr = rho_n_A.value
    sym_h_arr = sym_h.value
    ae_arr = ae.value
    

if __name__ == "__main__":
    test_grace_acc()