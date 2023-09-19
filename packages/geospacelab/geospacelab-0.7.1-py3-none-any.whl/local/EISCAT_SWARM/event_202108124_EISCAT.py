import datetime
import numpy as np
import pathlib

import geospacelab.express.eiscat_dashboard as eiscat
import geospacelab.toolbox.utilities.pydatetime as dttool

import geospacelab.visualization.mpl.colormaps as cm
default_colormap = cm.cmap_jet_modified()

def test_esr_32m():
    dt_fr = datetime.datetime.strptime('20210824' + '0900', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20210824' + '1200', '%Y%m%d%H%M')

    site = 'ESR'
    antenna = '32m'
    modulation = ''
    # load_mode = 'dialog'
    load_mode = 'AUTO'
    data_file_type = 'eiscat-hdf5'

    dashboard = eiscat.EISCATDashboard(
        dt_fr, dt_to,
        site=site, antenna=antenna, modulation=modulation,
        data_file_type=data_file_type, load_mode=load_mode,
        figure_config={'figsize': (9, 6)})

    # select beams before assign the variables
    az_el_pairs = [(83.8, 77.9), (83.2, 78.0), (83.0, 78.5), (83.0, 78.5)]
    dashboard.select_beams(az_el_pairs=az_el_pairs)  # (83.8, 77.9)  and (107.0, 101.6)
    dashboard.check_beams()
    # dashboard.status_mask(bad_status=[1, 2, 3])
    # dashboard.residual_mask()
    
    n_e = dashboard.assign_variable('n_e')
    n_e.visual.axis[0].data_res = 300
    
    T_i = dashboard.assign_variable('T_i')

    T_e = dashboard.assign_variable('T_e')

    v_i = dashboard.assign_variable('v_i_los')

    az = dashboard.assign_variable('AZ')
    el = dashboard.assign_variable('EL')

    layout = [[n_e], [T_e], [T_i], [v_i], [az, [el]]]
    dashboard.set_layout(panel_layouts=layout, left=0.12, right=0.87)
    dashboard.draw(time_res=900)
    dashboard.show()
    
    
if __name__ == "__main__":
    test_esr_32m()