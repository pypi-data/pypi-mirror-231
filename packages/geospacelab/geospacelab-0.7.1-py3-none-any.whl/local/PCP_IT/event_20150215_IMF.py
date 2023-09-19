import datetime
import numpy as np
import pathlib
import pickle

from geospacelab.datahub import DataHub
from geospacelab.visualization.mpl import create_figure
from geospacelab.visualization.mpl.dashboards import TSDashboard
from geospacelab.visualization.mpl.geomap.geodashboards import GeoDashboard
import geospacelab.toolbox.utilities.pydatetime as dttool

file_dir_root = pathlib.Path("/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results")


def show_IMF():
    fig = create_figure(figsize=(8, 6))

    dt_fr_omni = datetime.datetime(2015, 2, 15, 15)
    dt_to_omni = datetime.datetime(2015, 2, 16, 0)
    # dt_fr_omni = datetime.datetime(2015, 2, 27, 0)
    # dt_to_omni = datetime.datetime(2015, 2, 28, 0)
    db_omni = fig.add_dashboard(dashboard_class=TSDashboard, dt_fr=dt_fr_omni, dt_to=dt_to_omni)
    omni_config = {
        'omni_type': 'OMNI2',
        'omni_res': '1min',
        'load_mode': 'AUTO',
        'allow_load': True
    }
    ds_1 = db_omni.dock(datasource_contents=['cdaweb', 'omni'], **omni_config)
    ds_2 = db_omni.dock(datasource_contents=['wdc', 'ae'], allow_load=True, load_mode='AUTO')
    ds_3 = db_omni.dock(datasource_contents=['wdc', 'asysym'])
    ds_4 = db_omni.dock(datasource_contents=['gfz', 'kpap'])
    ds_5 = db_omni.dock(datasource_contents=['supermag', 'indices'])
    fp_ie = '/home/lei/extra/AFEISCAT3/Data/Indices/IL/IL20150215.dat'
    ds_6 = db_omni.dock(datasource_contents=['fmi', 'image', 'ie'], data_file_paths=[fp_ie], load_mode='assigned')

    ds_1.add_NCF()
    Bx = db_omni.assign_variable('B_x_GSM', dataset=db_omni.datasets[0])
    By = db_omni.assign_variable('B_y_GSM', dataset=db_omni.datasets[0])
    Bz = db_omni.assign_variable('B_z_GSM', dataset=db_omni.datasets[0])

    n_p = db_omni.assign_variable('n_p', dataset=db_omni.datasets[0])
    v_sw = db_omni.assign_variable('v_sw', dataset=db_omni.datasets[0])
    v_sw.visual.axis[1].lim = [200, 500]
    E_sw = v_sw.clone()
    E_sw.value = v_sw.value * ds_1['B_T_GSM'].value * 1e-3
    E_sw.unit = 'mV/m'
    E_sw.unit_label = None
    E_sw.label = r'$E_{sw}$'
    E_sw.visual.axis[1].lim = [0, 4]
    ncf = ds_1['NCF']
    ncf.visual.plot_config.style = '1P'
    ncf.visual.axis[1].label = '@v.label'
    ncf.visual.axis[1].unit = '@v.unit'

    p_dyn = db_omni.assign_variable('p_dyn', dataset=db_omni.datasets[0])

    au = db_omni.assign_variable('AU', dataset=db_omni.datasets[1])
    au.visual.axis[1].lim = [None, None]
    al = db_omni.assign_variable('AL', dataset=db_omni.datasets[1])
    ae = db_omni.assign_variable('AE', dataset=db_omni.datasets[1])

    sym_h = db_omni.assign_variable('SYM_H', dataset=db_omni.datasets[2])
    sym_h.visual.axis[1].lim = [None, None]
    sym_h.visual.axis[1].label = '@v.label'

    kp = db_omni.assign_variable('Kp', dataset=db_omni.datasets[3])

    sme = ds_5['SML']
    sme.visual.axis[1].lim = [-295, 60]
    sme.visual.axis[1].label = "Indices"
    ie = ds_6['IL']

    layout = [[Bx, By, Bz], [v_sw], [n_p], [ncf], [sme, ie]]
    db_omni.set_layout(panel_layouts=layout, left=0.12, right=0.85, top=0.92, bottom=0.1)
    db_omni.draw()
    # db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
    # db_omni.add_shading(dt_fr, time_c, alpha=0.15)
    db_omni.add_panel_labels()

    # db_omni.show()

    dts_tec = [
        datetime.datetime(2015, 2, 15, 17, 20),
        datetime.datetime(2015, 2, 15, 18, 5),
        datetime.datetime(2015, 2, 15, 18, 55),
        datetime.datetime(2015, 2, 15, 19, 40),
        datetime.datetime(2015, 2, 15, 20, 25),
        datetime.datetime(2015, 2, 15, 21, 10),
        datetime.datetime(2015, 2, 15, 22, 0),
        datetime.datetime(2015, 2, 15, 22, 25),
    ]

    # add vertical lines:
    for ind, dt in enumerate(dts_tec):
        db_omni.add_vertical_line(dt, top_extend=0.02, label='T{:d}'.format(ind+1), linewidth=1)

    db_omni.save_figure(file_name="Event_20150215_IMF", file_dir=file_dir_root)
    pass


if __name__ == "__main__":
    show_IMF()