
# Licensed under the BSD 3-Clause License
# Copyright (C) 2021 GeospaceLab (geospacelab)
# Author: Lei Cai, Space Physics and Astronomy, University of Oulu

__author__ = "Lei Cai"
__copyright__ = "Copyright 2021, GeospaceLab"
__license__ = "BSD-3-Clause License"
__email__ = "lei.cai@oulu.fi"
__docformat__ = "reStructureText"


import datetime
import numpy as np
import matplotlib.pyplot as plt
from geospacelab import preferences as pref
# pref.user_config['visualization']['mpl']['style'] = 'dark'

import geospacelab.visualization.mpl.geomap.geodashboards as geomap
import geospacelab.visualization.mpl as gsl_mpl


def test_tec():

    dt_fr = datetime.datetime(2021, 8, 24, 1)
    dt_to = datetime.datetime(2021, 8, 24, 23)
    db = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (15, 10)})
    db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    db.set_layout(2, 3, wspace=0.5)

    tec = db.assign_variable('TEC_MAP', dataset_index=0)
    dts = db.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db.assign_variable('GEO_LON', dataset_index=0).value

    """
    Generation of the first panel
    """
    time_c = datetime.datetime(2021, 8, 24, 9, 30)
    ind_t = np.where(dts == time_c)[0]

    # Add the first panel
    # AACGM LAT-MLT in the northern hemisphere
    panel = db.add_polar_map(row_ind=0, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)
    # AACGM LAT-MLT in the southern hemisphere
    # panel = db.add_polar_map(row_ind=0, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='S', ut=time_c, mirror_south=True)
    # GEO LAT-LST in the northern hemisphere
    # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lst-fixed', cs='GEO', lst_c=0., pole='N', ut=time_c, boundary_lat=60)
    # GEO LAT-LST in the southern hemisphere
    # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lst-fixed', cs='GEO', lst_c=0, pole='S', ut=time_c, mirror_south=True)
    # GEO LAT-LON in the southern hemisphere
    # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lon-fixed', cs='GEO', lon_c=0., pole='S', ut=time_c,
    #                          boundary_lat=0, mirror_south=False)
    # GEO LAT-LON in the northern hemisphere
    # pid = db.add_polar_map(row_ind=0, col_ind=0, style='lon-fixed', cs='GEO', lon_c=0., pole='N', ut=time_c,
    #                        boundary_lat=30, mirror_south=False)
    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    # retrieve the data array
    tec_ = tec.value[ind_t[0]]
    # Configuration for plotting
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 12])
    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')

    # overlay the 2-D TEC map
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    # add the panel title
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    """
    Repeating process for the second panel
    """
    time_c = datetime.datetime(2021, 8, 24, 10, 0)
    ind_t = np.where(dts == time_c)[0]

    panel = db.add_polar_map(row_ind=0, col_ind=1, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)

    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    tec_ = tec.value[ind_t[0], :, :]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 12])

    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    """
    Repeating process for the third panel
    """
    time_c = datetime.datetime(2021, 8, 24, 10, 30)
    ind_t = np.where(dts == time_c)[0]

    panel = db.add_polar_map(row_ind=0, col_ind=2, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)

    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    tec_ = tec.value[ind_t[0], :, :]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 12])

    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    """
    Repeating process for the fourth panel
    """
    time_c = datetime.datetime(2021, 8, 24, 11, 0)
    ind_t = np.where(dts == time_c)[0]

    panel = db.add_polar_map(row_ind=1, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)

    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    tec_ = tec.value[ind_t[0], :, :]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 15])

    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    """
    Repeating process for the fifth panel
    """
    time_c = datetime.datetime(2021, 8, 24, 11, 30)
    ind_t = np.where(dts == time_c)[0]

    panel = db.add_polar_map(row_ind=1, col_ind=1, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)
    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    tec_ = tec.value[ind_t[0], :, :]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 15])

    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    """
        Repeating process for the sixth panel
    """
    time_c = datetime.datetime(2021, 8, 24, 12, 0)
    ind_t = np.where(dts == time_c)[0]

    panel = db.add_polar_map(row_ind=1, col_ind=2, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=60)

    panel.overlay_coastlines()
    panel.overlay_gridlines()
    #
    tec_ = tec.value[ind_t[0], :, :]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[5, 15])

    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='jet')
    ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))

    plt.savefig('example_tec_aacgm_fixed_mlt', dpi=200)
    plt.show()


def show_tec_maps(dt_fr=None, dt_to=None, *, rows=3, cols=3, time_res=5.):

    def add_tec_map(pole='N', no_colorbar=False):

        """
        Generation of a tec panel
        """
        time_c = dt_c
        ind_t = np.where(dts_arr == time_c)[0]

        # Add the first panel
        # AACGM LAT-MLT in the northern hemisphere
        panel = db.add_polar_map(style='mlt-fixed', cs='AACGM', mlt_c=0., pole=pole, ut=time_c,
                                 boundary_lat=55.)
        # AACGM LAT-MLT in the southern hemisphere
        # panel = db.add_polar_map(row_ind=0, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='S', ut=time_c, mirror_south=True)
        # GEO LAT-LST in the northern hemisphere
        # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lst-fixed', cs='GEO', lst_c=0., pole='N', ut=time_c, boundary_lat=60)
        # GEO LAT-LST in the southern hemisphere
        # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lst-fixed', cs='GEO', lst_c=0, pole='S', ut=time_c, mirror_south=True)
        # GEO LAT-LON in the southern hemisphere
        # panel = db.add_polar_map(row_ind=0, col_ind=0, style='lon-fixed', cs='GEO', lon_c=0., pole='S', ut=time_c,
        #                          boundary_lat=0, mirror_south=False)
        # GEO LAT-LON in the northern hemisphere
        # pid = db.add_polar_map(row_ind=0, col_ind=0, style='lon-fixed', cs='GEO', lon_c=0., pole='N', ut=time_c,
        #                        boundary_lat=30, mirror_south=False)
        panel.overlay_coastlines()
        panel.overlay_gridlines(lon_label_separator=5, lat_label_clock=4.)
        #
        # retrieve the data array
        tec_ = tec.value[ind_t[0]]
        # Configuration for plotting
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[5, 12])
        import geospacelab.visualization.mpl.colormaps as cm
        pcolormesh_config.update(cmap='jet')

        # overlay the 2-D TEC map
        ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat_arr, 'lon': glon_arr, 'height': 250.}, cs='GEO',
                                       **pcolormesh_config)
        if not no_colorbar:
            panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.2, bottom=1.,
                            width=0.05, height=2.5)

        # add the panel title# Add sites
        panel.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='*', markersize=7, color='#E013C4', alpha=1)

        panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))
        panel.add_label(0.08, 0.95, label=f"({chr(97+ind)})", fontsize=14, color='k')

    # create time series
    diff_t = (dt_to - dt_fr).total_seconds() / 60.
    dts = [dt_fr + datetime.timedelta(minutes=t) for t in np.arange(0, diff_t + 1, time_res)]

    pole = 'N'

    fig = gsl_mpl.create_figure(figsize=(12, 12))
    db = fig.add_dashboard(dashboard_class=geomap.GeoDashboard, dt_fr=dt_fr, dt_to=dt_to)
    db.set_layout(rows, cols, left=0.03, right=0.9, bottom=0.05, top=0.9, hspace=0.2, wspace=0.3)
    ds_tec = db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    tec = ds_tec['TEC_MAP']
    dts_arr = ds_tec['DATETIME'].value.flatten()
    glat_arr = ds_tec['GEO_LAT'].value
    glon_arr = ds_tec['GEO_LON'].value

    for ind, dt_c in enumerate(dts):
        if ind == len(dts) - 1:
            nocb = False
        else:
            nocb = True
        add_tec_map(pole=pole, no_colorbar=nocb)
    file_dir = "/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results"
    file_name = f"TEC_MAPS_{dt_fr.strftime('%Y%m%d-%H%M')}_{dt_to.strftime('%Y%m%d-%H%M')}_tres{str(time_res)}"
    db.save_figure(file_dir=file_dir, file_name=file_name, append_time=False)
    db.show()


def events():
    events =[
        (
            datetime.datetime(2016, 2, 14, 16),
            datetime.datetime(2016, 2, 14, 21)
        ),
        (
            datetime.datetime(2019, 9, 27, 19),
            datetime.datetime(2019, 9, 28, 0)
        ),
        (
            datetime.datetime(2014, 11, 30, 16),
            datetime.datetime(2014, 11, 30, 21)
        ),

    ]

    time_res = 20.
    rows = 4
    cols = 4
    for ind, event in enumerate(events):
        if ind > 0:
            continue
        print(event)

        show_tec_maps(dt_fr=event[0], dt_to=event[1], rows=rows, cols=cols, time_res=time_res)


if __name__ == "__main__":
    events()



