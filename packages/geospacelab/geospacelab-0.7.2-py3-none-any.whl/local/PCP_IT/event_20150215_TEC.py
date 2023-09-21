import datetime
import numpy as np
import pathlib
import pickle

from geospacelab.datahub import DataHub
from geospacelab.visualization.mpl import create_figure
from geospacelab.visualization.mpl.dashboards import TSDashboard
from geospacelab.visualization.mpl.geomap.geodashboards import GeoDashboard
import geospacelab.toolbox.utilities.pydatetime as dttool
import cartopy.crs as ccrs

import solar_terminator as st

file_dir_root = pathlib.Path("/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results")


def show_TEC():
    fig = create_figure(figsize=(10, 6))

    dt_fr_tec = datetime.datetime(2015, 2, 15, 15, )
    dt_to_tec = datetime.datetime(2015, 2, 15, 23, 59)
    db_tec = fig.add_dashboard(dashboard_class=GeoDashboard, dt_fr=dt_fr_tec, dt_to=dt_to_tec)
    ds_tec = db_tec.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    tec = db_tec.assign_variable('TEC_MAP', dataset_index=0)
    dts = db_tec.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db_tec.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db_tec.assign_variable('GEO_LON', dataset_index=0).value

    data_file_paths = [
        '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
    ds_sd = db_tec.dock(
        datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

    phi_sd = db_tec.assign_variable('GRID_phi', dataset=ds_sd)
    dts_sd = db_tec.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
    mlat_sd = db_tec.assign_variable('GRID_MLAT', dataset=ds_sd)
    mlon_sd = db_tec.assign_variable('GRID_MLON', dataset=ds_sd)
    mlt_sd = db_tec.assign_variable(('GRID_MLT'), dataset=ds_sd)

    db_tec.set_layout(2, 4, left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.19, )
    ind = 0

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

    for row in range(2):
        for col in range(4):
            time_c = dts_tec[ind]
            panel = db_tec.add_polar_map(
                row_ind=row, col_ind=col,
                style='mlt-fixed', cs='AACGM', mlt_c=0.,
                pole='N', ut=time_c, boundary_lat=55,
            )
            # panel1 = db.add_polar_map(
            #     row_ind=0, col_ind=0,
            #     style='lst-fixed', cs='GEO', lst_c=0.,
            #     pole='N', ut=time_c, boundary_lat=55,
            #     )
            panel.overlay_coastlines()
            panel.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5, lat_label_config={'fontsize': 6})

            ind_t_c = np.where(dts == time_c)[0]
            if not list(ind_t_c):
                return
            tec_ = tec.value[ind_t_c[0], :, :]
            pcolormesh_config = tec.visual.plot_config.pcolormesh

            import cmasher
            pcolormesh_config.update(c_lim=[0, 14])

            # import geospacelab.visualization.mpl.colormaps as cm
            # pcolormesh_config.update(cmap='jet')
            ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                             **pcolormesh_config, regridding=True, grid_res=.5)

            # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)

            if ind == len(dts_tec) - 1:
                panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.15, bottom=0.35, width=0.07, height=1.5)

            ind_t = ds_sd.get_time_ind(ut=time_c)
            # initialize the polar map

            phi_ = phi_sd.value[ind_t]
            mlat_ = mlat_sd.value[ind_t]
            mlt_ = mlt_sd.value[ind_t]
            mlon_ = mlon_sd.value[ind_t]

            # grid_mlat, grid_mlt, grid_phi = dataset_superdarn.grid_phi(mlat_, mlt_, phi_, interp_method='cubic')
            grid_mlat, grid_mlt, grid_phi = ds_sd.postprocess_roll(mlat_, mlt_, phi_)

            # re-grid the original data with higher spatial resolution, default mlt_res = 0.05, mlat_res = 0.5. used for plotting.
            # grid_mlat, grid_mlt, grid_fac = dataset_ampere.grid_fac(phi_, mlt_res=0.05, mlat_res=0.05, interp_method='linear')

            levels = np.array([-35e3, -30e3, -25e3, -20e3, -15e3, -10e3, -5e3, 5e3, 10e3, 15e3, 20e3, 25e3, 30e3, 35e3])
            # levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
            # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
            ict = panel.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt},
                                          cs='AACGM',
                                          colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7)

            # az_list = np.arange(-87.5, 87.5, 1.)
            # alt = 110.
            # lons, lats = st.terminator(time_c, alt, az_list=az_list)
            # coords = {'lat': lats, 'lon': lons, 'height': alt}
            # panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1., linestyle=':', color='purple')
            # alt = 300.
            # lons, lats = st.terminator(time_c, alt, az_list=az_list)
            # coords = {'lat': lats, 'lon': lons, 'height': alt}
            # panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1., linestyle=':', color='k')

            panel.overlay_sites(
                site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
                cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r')

            panel.overlay_sites(
                site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
                cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

            panel.add_label(x=0.0, y=0.95, label="({:c})".format(97+ind), fontsize=12)
            panel.add_title(0.5, 1.1, title="T{:d}: {:s} UT".format(ind+1, time_c.strftime("%H:%M")), fontsize=12)
            ind += 1
    db_tec.save_figure(file_name="event_20150215_TECs", file_dir=file_dir_root)
    pass


def show_TEC_2():
    fig = create_figure(figsize=(10, 6))

    dt_fr_tec = datetime.datetime(2015, 2, 15, 15, )
    dt_to_tec = datetime.datetime(2015, 2, 15, 23, 59)
    db_tec = fig.add_dashboard(dashboard_class=GeoDashboard, dt_fr=dt_fr_tec, dt_to=dt_to_tec)
    ds_tec = db_tec.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    tec = db_tec.assign_variable('TEC_MAP', dataset_index=0)
    dts = db_tec.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db_tec.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db_tec.assign_variable('GEO_LON', dataset_index=0).value

    data_file_paths = [
        '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
    ds_sd = db_tec.dock(
        datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

    phi_sd = db_tec.assign_variable('GRID_phi', dataset=ds_sd)
    dts_sd = db_tec.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
    mlat_sd = db_tec.assign_variable('GRID_MLAT', dataset=ds_sd)
    mlon_sd = db_tec.assign_variable('GRID_MLON', dataset=ds_sd)
    mlt_sd = db_tec.assign_variable(('GRID_MLT'), dataset=ds_sd)

    db_tec.set_layout(2, 4, left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.19, )
    ind = 0

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

    ds_s1_f18 = db_tec.dock(
        datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'],
        dt_fr=dt_fr_tec,
        dt_to=dt_to_tec,
        sat_id='f18', replace_orbit=True)

    ds_s1_f19 = db_tec.dock(
        datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'],
        dt_fr=dt_fr_tec,
        dt_to=dt_to_tec,
        sat_id='f19', replace_orbit=True)

    for row in range(2):
        for col in range(4):
            time_c = dts_tec[ind]
            panel = db_tec.add_polar_map(
                row_ind=row, col_ind=col,
                style='mlt-fixed', cs='AACGM', mlt_c=0.,
                pole='N', ut=time_c, boundary_lat=55,
            )
            # panel1 = db.add_polar_map(
            #     row_ind=0, col_ind=0,
            #     style='lst-fixed', cs='GEO', lst_c=0.,
            #     pole='N', ut=time_c, boundary_lat=55,
            #     )
            panel.overlay_coastlines()
            panel.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5, lat_label_config={'fontsize': 6})

            ind_t_c = np.where(dts == time_c)[0]
            if not list(ind_t_c):
                return
            tec_ = tec.value[ind_t_c[0], :, :]
            pcolormesh_config = tec.visual.plot_config.pcolormesh

            import cmasher
            pcolormesh_config.update(c_lim=[0, 14])

            # import geospacelab.visualization.mpl.colormaps as cm
            # pcolormesh_config.update(cmap='jet')
            ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                             **pcolormesh_config, regridding=True, grid_res=.5)

            # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)

            if ind == len(dts_tec) - 1:
                panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.15, bottom=0.35, width=0.07, height=1.5)

            ind_t = ds_sd.get_time_ind(ut=time_c)
            # initialize the polar map

            # phi_ = phi_sd.value[ind_t]
            # mlat_ = mlat_sd.value[ind_t]
            # mlt_ = mlt_sd.value[ind_t]
            # mlon_ = mlon_sd.value[ind_t]
            #
            # # grid_mlat, grid_mlt, grid_phi = dataset_superdarn.grid_phi(mlat_, mlt_, phi_, interp_method='cubic')
            # grid_mlat, grid_mlt, grid_phi = ds_sd.postprocess_roll(mlat_, mlt_, phi_)
            #
            # # re-grid the original data with higher spatial resolution, default mlt_res = 0.05, mlat_res = 0.5. used for plotting.
            # # grid_mlat, grid_mlt, grid_fac = dataset_ampere.grid_fac(phi_, mlt_res=0.05, mlat_res=0.05, interp_method='linear')
            #
            # levels = np.array([-35e3, -30e3, -25e3, -20e3, -15e3, -10e3, -5e3, 5e3, 10e3, 15e3, 20e3, 25e3, 30e3, 35e3])
            # # levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
            # # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
            # ict = panel.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt},
            #                               cs='AACGM',
            #                               colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7)

            # az_list = np.arange(-87.5, 87.5, 1.)
            # alt = 110.
            # lons, lats = st.terminator(time_c, alt, az_list=az_list)
            # coords = {'lat': lats, 'lon': lons, 'height': alt}
            # panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1., linestyle=':', color='purple')
            # alt = 300.
            # lons, lats = st.terminator(time_c, alt, az_list=az_list)
            # coords = {'lat': lats, 'lon': lons, 'height': alt}
            # panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1., linestyle=':', color='k')

            if ind in [0, 2]:
                ds_s1 = ds_s1_f18
            elif ind in [4, 6]:
                ds_s1 = ds_s1_f19
            else:
                ds_s1 = None

            if ds_s1 is not None:
                sc_dt = ds_s1['SC_DATETIME'].value.flatten()
                sc_lat = ds_s1['SC_GEO_LAT'].value.flatten()
                sc_lon = ds_s1['SC_GEO_LON'].value.flatten()
                sc_alt = ds_s1['SC_GEO_ALT'].value.flatten()

                ind_t = np.where((sc_dt > time_c - datetime.timedelta(minutes=35)) & (
                        sc_dt < time_c + datetime.timedelta(minutes=35)))[0]
                sc_coords = {'lat': sc_lat[ind_t], 'lon': sc_lon[ind_t], 'height': sc_alt[ind_t]}

                v_H = ds_s1['v_i_H'].value.flatten()[ind_t]
                panel.overlay_cross_track_vector(
                    vector=v_H, unit_vector=1000, vector_unit='m/s', alpha=0.2, color='c', vector_width=2.,
                    sc_coords=sc_coords, sc_ut=sc_dt[ind_t], cs='GEO', edge='on', edge_alpha=0.9, edge_color='c',
                    legend_pos_x=0.9, legend_pos_y=0.9, legend_linewidth=2., legend_label=r'$v_i=1000$ m/s', legend_fontsize=8,
                )
                # Overlay the satellite trajectory with ticks
                panel.overlay_sc_trajectory(
                    sc_ut=sc_dt[ind_t], sc_coords=sc_coords, cs='GEO', color='#9090C0',
                    time_tick_label_rotation=90., time_tick_label_offset=0.1, time_tick_label_fontsize=6,
                    time_tick_label_fontweight='bold',
                )

            panel.overlay_sites(
                site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
                cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r')

            panel.overlay_sites(
                site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
                cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

            panel.add_label(x=0.0, y=0.95, label="({:c})".format(97+ind), fontsize=12)
            panel.add_title(0.5, 1.1, title="T{:d}: {:s} UT".format(ind+1, time_c.strftime("%H:%M")), fontsize=12)
            ind += 1
    db_tec.save_figure(file_name="event_20150215_TECs_with_DMSP", file_dir=file_dir_root)
    pass

if __name__ == "__main__":
    show_TEC_2()
