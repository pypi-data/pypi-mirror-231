from tkinter import TRUE
import scipy.io as sio
import pathlib
import datetime
import numpy as np
import matplotlib.pyplot as plt

from geospacelab.datahub import DatasetUser
from geospacelab.visualization.mpl.dashboards import Dashboard, TSDashboard
from geospacelab.cs import GEOCSpherical
import geospacelab.visualization.mpl.geomap.geodashboards as geomap

fp_res = pathlib.Path('/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results')


def visual_solar_wind():
    dt_fr = datetime.datetime(2015, 2, 15, 15)
    dt_to = datetime.datetime(2015, 2, 16, 0)
    db = TSDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (14, 7)})
    omni_config = {
        'omni_type': 'OMNI2',
        'omni_res': '1min',
        'load_mode': 'AUTO',
        'allow_load': True
    }
    ds_1 = db.dock(datasource_contents=['cdaweb', 'omni'], **omni_config)
    ds_2 = db.dock(datasource_contents=['wdc', 'ae'], allow_load=True, load_mode='AUTO')
    ds_3 = db.dock(datasource_contents=['wdc', 'asysym'])
    ds_4 = db.dock(datasource_contents=['gfz', 'kpap'])

    Bx = db.assign_variable('B_x_GSM', dataset=db.datasets[0])
    By = db.assign_variable('B_y_GSM', dataset=db.datasets[0])
    Bz = db.assign_variable('B_z_GSM', dataset=db.datasets[0])

    n_p = db.assign_variable('n_p', dataset=db.datasets[0])
    v_sw = db.assign_variable('v_sw', dataset=db.datasets[0])
    v_sw.visual.axis[1].lim = [240, 510]
    p_dyn = db.assign_variable('p_dyn', dataset=db.datasets[0])

    au = db.assign_variable('AU', dataset=db.datasets[1])
    au.visual.axis[1].lim = [None, None]
    al = db.assign_variable('AL', dataset=db.datasets[1])
    ae = db.assign_variable('AE', dataset=db.datasets[1]) 

    sym_h = db.assign_variable('SYM_H', dataset=db.datasets[2])
    sym_h.visual.axis[1].lim = [None, None]
    sym_h.visual.axis[1].label = '@v.label'

    kp = db.assign_variable('Kp', dataset=db.datasets[3])

    layout = [[Bx, By, Bz], [v_sw], [n_p, [p_dyn]], [au, al, ae], [kp, [sym_h]]]
    db.set_layout(panel_layouts=layout)
    # plt.style.use('dark_background')
    # dt_fr_1 = datetime.datetime.strptime('20201209' + '1300', '%Y%m%d%H%M')
    # dt_to_1 = datetime.datetime.strptime('20201210' + '1200', '%Y%m%d%H%M')

    db.draw()
    db.add_panel_labels()
    db.save_figure(file_name='omni_geomag', file_dir=fp_res)


def tec_maps():
    dt_fr = datetime.datetime(2015, 2, 15, 17)
    dt_to = datetime.datetime(2015, 2, 15, 23, 0)
    diff_sec = (dt_to - dt_fr).total_seconds()
    times = [dt_fr + datetime.timedelta(seconds=sec) for sec in np.arange(0, diff_sec + 1, 300)]

    db = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (20, 10)})
    db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])

    tec = db.assign_variable('TEC_MAP', dataset_index=1)
    dts = db.assign_variable('DATETIME', dataset_index=1).value.flatten()
    glat = db.assign_variable('GEO_LAT', dataset_index=1).value
    glon = db.assign_variable('GEO_LON', dataset_index=1).value

    dt_fr_omni = datetime.datetime(2015, 2, 15, 16)
    dt_to_omni = datetime.datetime(2015, 2, 16, 0, 0)
    db_omni = TSDashboard(dt_fr=dt_fr_omni, dt_to=dt_to_omni, figure=db.figure)
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

    Bx = db_omni.assign_variable('B_x_GSM', dataset=db_omni.datasets[1])
    By = db_omni.assign_variable('B_y_GSM', dataset=db_omni.datasets[1])
    Bz = db_omni.assign_variable('B_z_GSM', dataset=db_omni.datasets[1])

    n_p = db_omni.assign_variable('n_p', dataset=db_omni.datasets[1])
    v_sw = db_omni.assign_variable('v_sw', dataset=db_omni.datasets[1])
    p_dyn = db_omni.assign_variable('p_dyn', dataset=db_omni.datasets[1])

    au = db_omni.assign_variable('AU', dataset=db_omni.datasets[2])
    au.visual.axis[1].lim = [None, None]
    al = db_omni.assign_variable('AL', dataset=db_omni.datasets[2])

    sym_h = db_omni.assign_variable('SYM_H', dataset=db_omni.datasets[3])
    sym_h.visual.axis[1].lim = [None, None]
    sym_h.visual.axis[1].label = '@v.label'

    kp = db_omni.assign_variable('Kp', dataset=db_omni.datasets[4])

    layout = [[Bx, By, Bz], [v_sw], [au, al]]

    # plt.style.use('dark_background')
    # dt_fr_1 = datetime.datetime.strptime('20201209' + '1300', '%Y%m%d%H%M')
    # dt_to_1 = datetime.datetime.strptime('20201210' + '1200', '%Y%m%d%H%M')

    for time_c in times:

        db.set_layout(1, 1, left=0.55, wspace=0.1)
        ind_t = np.where(dts == time_c)[0]
        if not list(ind_t):
            continue
        panel1 = db.add_polar_map(
            row_ind=0, col_ind=0,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        # panel1 = db.add_polar_map(
        #     row_ind=0, col_ind=0, 
        #     style='lst-fixed', cs='GEO', lst_c=0., 
        #     pole='N', ut=time_c, boundary_lat=55,
        #     )
        panel1.overlay_coastlines()
        panel1.overlay_gridlines()
        #
        tec_ = tec.value[ind_t[0], :, :]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[5, 25])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                        **pcolormesh_config, regridding=True, grid_res=0.5)

        # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
        panel1.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)

        # overlay superdarn
        # specify the file full path
        data_file_paths = ['/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
        # data_file_paths = ['/Users/lcai/Geospacelab/Data/SuperDARN/POTMAP/2016/SuperDARM_POTMAP_20160314_10min_test.txt']

        ds_sd = db.dock(
            datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

        phi_sd = db.assign_variable('GRID_phi', dataset=ds_sd)
        dts_sd = db.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
        mlat_sd = db.assign_variable('GRID_MLAT', dataset=ds_sd)
        mlon_sd = db.assign_variable('GRID_MLON', dataset=ds_sd)
        mlt_sd = db.assign_variable(('GRID_MLT'), dataset=ds_sd)

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
        # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
        ict = panel1.overlay_contour(grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                     colors='y', levels=levels)

        # Add sites
        panel1.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=5, color='purple')

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel1.add_title(title=time_c.strftime("%Y-%m-%d %H:%M UT"))

        db_omni.set_layout(panel_layouts=layout, top=0.8, bottom=0.3, left=0.1, right=0.45)
        db_omni.draw()
        db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
        db_omni.add_shading(dt_fr, time_c, alpha=0.15)
        db_omni.add_panel_labels()

        fp_res_rec = fp_res / "TEC_MAPS_AACGM_MLT"
        fp_res_rec.mkdir(exist_ok=True)
        plt.savefig(fp_res_rec / ("TEC_MAP_OMNI_" + time_c.strftime("%Y-%m-%d_%H%M")))
        print(time_c)
        db.figure.clear()
        db.figure._gridspecs = []
        pass


def tec_omni_maps():
    def tec_omni_draw(time_c):
        dt_fr_tec = datetime.datetime(2015, 2, 15, 17)
        dt_to_tec = datetime.datetime(2015, 2, 15, 23, 0)
        # diff_sec = (dt_to - dt_fr).total_seconds()
        # times = [dt_fr + datetime.timedelta(seconds=sec) for sec in np.arange(0, diff_sec + 1, 300)]

        db = geomap.GeoDashboard(dt_fr=dt_fr_tec, dt_to=dt_to_tec, figure_config={'figsize': (20, 10)})
        db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])

        tec = db.assign_variable('TEC_MAP', dataset_index=1)
        dts = db.assign_variable('DATETIME', dataset_index=1).value.flatten()
        glat = db.assign_variable('GEO_LAT', dataset_index=1).value
        glon = db.assign_variable('GEO_LON', dataset_index=1).value

        dt_fr_omni = datetime.datetime(2015, 2, 15, 16)
        dt_to_omni = datetime.datetime(2015, 2, 16, 0, 0)
        db_omni = TSDashboard(dt_fr=dt_fr_omni, dt_to=dt_to_omni, figure=db.figure)

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

        Bx = db_omni.assign_variable('B_x_GSM', dataset=db_omni.datasets[1])
        By = db_omni.assign_variable('B_y_GSM', dataset=db_omni.datasets[1])
        Bz = db_omni.assign_variable('B_z_GSM', dataset=db_omni.datasets[1])

        n_p = db_omni.assign_variable('n_p', dataset=db_omni.datasets[1])
        v_sw = db_omni.assign_variable('v_sw', dataset=db_omni.datasets[1])
        v_sw.visual.axis[1].lim = [200, 500]
        p_dyn = db_omni.assign_variable('p_dyn', dataset=db_omni.datasets[1])

        au = db_omni.assign_variable('AU', dataset=db_omni.datasets[2])
        au.visual.axis[1].lim = [None, None]
        al = db_omni.assign_variable('AL', dataset=db_omni.datasets[2])
        ae = db_omni.assign_variable('AE', dataset=db_omni.datasets[2])

        sym_h = db_omni.assign_variable('SYM_H', dataset=db_omni.datasets[3])
        sym_h.visual.axis[1].lim = [None, None]
        sym_h.visual.axis[1].label = '@v.label'

        kp = db_omni.assign_variable('Kp', dataset=db_omni.datasets[4])

        layout = [[Bx, By, Bz], [v_sw], [au, al, ae]]

        # plt.style.use('dark_background')
        # dt_fr_1 = datetime.datetime.strptime('20201209' + '1300', '%Y%m%d%H%M')
        # dt_to_1 = datetime.datetime.strptime('20201210' + '1200', '%Y%m%d%H%M')

        db.set_layout(1, 1, left=0.55, wspace=0.1)
        ind_t = np.where(dts == time_c)[0]
        if not list(ind_t):
            return
        panel1 = db.add_polar_map(
            row_ind=0, col_ind=0,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        # panel1 = db.add_polar_map(
        #     row_ind=0, col_ind=0,
        #     style='lst-fixed', cs='GEO', lst_c=0.,
        #     pole='N', ut=time_c, boundary_lat=55,
        #     )
        panel1.overlay_coastlines()
        panel1.overlay_gridlines()
        #
        tec_ = tec.value[ind_t[0], :, :]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[0, 20])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                        **pcolormesh_config, regridding=True, grid_res=0.5)

        # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
        panel1.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)

        # overlay superdarn
        # specify the file full path
        data_file_paths = [
            '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
        # data_file_paths = ['/Users/lcai/Geospacelab/Data/SuperDARN/POTMAP/2016/SuperDARM_POTMAP_20160314_10min_test.txt']

        ds_sd = db.dock(
            datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

        phi_sd = db.assign_variable('GRID_phi', dataset=ds_sd)
        dts_sd = db.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
        mlat_sd = db.assign_variable('GRID_MLAT', dataset=ds_sd)
        mlon_sd = db.assign_variable('GRID_MLON', dataset=ds_sd)
        mlt_sd = db.assign_variable(('GRID_MLT'), dataset=ds_sd)

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
        # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
        ict = panel1.overlay_contour(grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                     colors='grey', levels=levels)

        # Add sites
        panel1.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='*', markersize=7, color='#E013C4', alpha=1)

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel1.add_title(title=time_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=18)

        db_omni.set_layout(panel_layouts=layout, top=0.8, bottom=0.3, left=0.1, right=0.45)
        db_omni.draw()
        db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
        db_omni.add_shading(dt_fr, time_c, alpha=0.15)
        db_omni.add_panel_labels()

        fp_res_rec = fp_res / "TEC_MAPS_AACGM_MLT"
        fp_res_rec.mkdir(exist_ok=True)
        plt.savefig(fp_res_rec / ("TEC_MAP_OMNI_" + time_c.strftime("%Y-%m-%d_%H%M")))
        print(time_c)

    dt_fr = datetime.datetime(2015, 2, 15, 17)
    dt_to = datetime.datetime(2015, 2, 15, 23, 0)
    diff_sec = (dt_to - dt_fr).total_seconds()
    times = [dt_fr + datetime.timedelta(seconds=sec) for sec in np.arange(0, diff_sec + 1, 300)]

    for time_0 in times:
        tec_omni_draw(time_0)


def visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N'):
    band = 'LBHS'
    dt_fr = dmsp_dn - datetime.timedelta(minutes=60)
    dt_to = dmsp_dn + datetime.timedelta(minutes=60)
    time_c = dmsp_dn
    sat_id = dmsp_sat_id
    orbit_id = dmsp_orbit_id

    # Create a geodashboard object
    dashboard = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (18, 12)})

    # If the orbit_id is specified, only one file will be downloaded. This option saves the downloading time.
    # dashboard.dock(datasource_contents=['jhuapl', 'dmsp', 'ssusi', 'edraur'], pole='N', sat_id='f17', orbit_id='46863')
    # If not specified, the data during the whole day will be downloaded.
    ds_dmsp = dashboard.dock(datasource_contents=['jhuapl', 'dmsp', 'ssusi', 'edraur'], pole=pole, sat_id=sat_id,
                             orbit_id=orbit_id)
    ds_s1 = dashboard.dock(
        datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'],
        dt_fr=time_c - datetime.timedelta(minutes=45),
        dt_to=time_c + datetime.timedelta(minutes=45),
        sat_id=sat_id, replace_orbit=True)
    ds_tec = dashboard.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])

    dashboard.set_layout(2, 1, left=0.05, right=0.4, bottom=0.05, top=0.9, hspace=0.25)

    # TEC Map
    tec = dashboard.assign_variable('TEC_MAP', dataset=ds_tec)
    dts_tec = dashboard.assign_variable('DATETIME', dataset=ds_tec).value.flatten()
    glat = dashboard.assign_variable('GEO_LAT', dataset=ds_tec).value
    glon = dashboard.assign_variable('GEO_LON', dataset=ds_tec).value

    ind_t = ds_tec.get_time_ind(ut=dmsp_dn, time_res=300)
    panel_tec = dashboard.add_polar_map(
        row_ind=0, col_ind=0,
        style='mlt-fixed', cs='AACGM', mlt_c=0.,
        pole='N', ut=time_c, boundary_lat=55,
    )

    panel_tec.overlay_coastlines()
    panel_tec.overlay_gridlines(lat_res=5, lon_label_separator=5)
    #
    tec_ = tec.value[ind_t]
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[0, 14])

    # import geospacelab.visualization.mpl.colormaps as cm
    # pcolormesh_config.update(cmap='jet')
    ipc = panel_tec.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                       **pcolormesh_config, regridding=True, grid_res=0.5)
    # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
    panel_tec.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.08, bottom=0.1, width=0.05, height=0.7)

    # overlay superdarn
    data_file_paths = [
        '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
    ds_sd = dashboard.dock(
        datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

    phi_sd = dashboard.assign_variable('GRID_phi', dataset=ds_sd)
    dts_sd = dashboard.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
    mlat_sd = dashboard.assign_variable('GRID_MLAT', dataset=ds_sd)
    mlon_sd = dashboard.assign_variable('GRID_MLON', dataset=ds_sd)
    mlt_sd = dashboard.assign_variable(('GRID_MLT'), dataset=ds_sd)

    ind_t_sd = ds_sd.get_time_ind(ut=time_c)
    # initialize the polar map

    phi_ = phi_sd.value[ind_t_sd]
    mlat_ = mlat_sd.value[ind_t_sd]
    mlt_ = mlt_sd.value[ind_t_sd]
    mlon_ = mlon_sd.value[ind_t_sd]

    # grid_mlat, grid_mlt, grid_phi = dataset_superdarn.grid_phi(mlat_, mlt_, phi_, interp_method='cubic')
    grid_mlat, grid_mlt, grid_phi = ds_sd.postprocess_roll(mlat_, mlt_, phi_)

    # re-grid the original data with higher spatial resolution, default mlt_res = 0.05, mlat_res = 0.5. used for plotting.
    # grid_mlat, grid_mlt, grid_fac = dataset_ampere.grid_fac(phi_, mlt_res=0.05, mlat_res=0.05, interp_method='linear')

    levels = np.array([-35e3, -30e3, -25e3, -20e3, -15e3, -10e3, -5e3, 5e3, 10e3, 15e3, 20e3, 25e3, 30e3, 35e3])
    # levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
    # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
    ict = panel_tec.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt},
                                cs='AACGM',
                                colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7)

    panel_tec.overlay_sites(
            site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
            cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r')

    panel_tec.overlay_sites(
            site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
            cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

    # Overlay cross-track velocity along satellite trajectory
    sc_dt = ds_s1['SC_DATETIME'].value.flatten()
    sc_lat = ds_s1['SC_GEO_LAT'].value.flatten()
    sc_lon = ds_s1['SC_GEO_LON'].value.flatten()
    sc_alt = ds_s1['SC_GEO_ALT'].value.flatten()

    ind_t1 = np.where((sc_dt > time_c - datetime.timedelta(minutes=35)) & (
                    sc_dt < time_c + datetime.timedelta(minutes=35)))[0]
    sc_coords = {'lat': sc_lat[ind_t1], 'lon': sc_lon[ind_t1], 'height': sc_alt[ind_t1]}

    v_H = ds_s1['v_i_H'].value.flatten()[ind_t1]
    panel_tec.overlay_cross_track_vector(
            vector=v_H, unit_vector=1000, vector_unit='m/s', alpha=0.2, color='c', vector_width=2.,
            sc_coords=sc_coords, sc_ut=sc_dt[ind_t1], cs='GEO', edge='on', edge_alpha=0.9, edge_color='c',
            legend_pos_x=0.9, legend_pos_y=0.9, legend_linewidth=2., legend_label= r'$v_i=1000$ m/s',
        )
        # Overlay the satellite trajectory with ticks
    panel_tec.overlay_sc_trajectory(
            sc_ut=sc_dt[ind_t1], sc_coords=sc_coords, cs='GEO', color='#9090C0',
            time_tick_label_rotation=90., time_tick_label_offset=0.1, time_tick_label_fontsize=10,
            time_tick_label_fontweight='bold', 
        )

    # # viewer.add_text(0.5, 1.1, "dashboard title")
    panel_tec.add_title(title="GNSS/TEC map, " + dts_tec[ind_t].strftime("%Y-%m-%d %H:%M UT"))

    # Get the variables: LBHS emission intensiy, corresponding times and locations
    lbhs = dashboard.assign_variable('GRID_AUR_' + band, dataset=ds_dmsp)
    dts = dashboard.assign_variable('DATETIME', dataset=ds_dmsp).value.flatten()
    mlat = dashboard.assign_variable('GRID_MLAT', dataset=ds_dmsp).value
    mlon = dashboard.assign_variable('GRID_MLON', dataset=ds_dmsp).value
    mlt = dashboard.assign_variable(('GRID_MLT'), dataset=ds_dmsp).value

    # Search the index for the time to plot, used as an input to the following polar map
    ind_t = dashboard.datasets[0].get_time_ind(ut=time_c)
    if (dts[ind_t] - time_c).total_seconds() / 60 > 60:  # in minutes
        raise ValueError("The time does not match any SSUSI data!")
    lbhs_ = lbhs.value[ind_t]
    mlat_ = mlat[ind_t]
    mlon_ = mlon[ind_t]
    mlt_ = mlt[ind_t]
    # Add a polar map panel to the dashboard. Currently the style is the fixed MLT at mlt_c=0. See the keywords below:
    panel_dmsp = dashboard.add_polar_map(
        row_ind=1, col_ind=0, style='mlt-fixed', cs='AACGM',
        mlt_c=0., pole=pole, ut=time_c, boundary_lat=55., mirror_south=True
    )

    # Some settings for plotting.
    pcolormesh_config = lbhs.visual.plot_config.pcolormesh
    # Overlay the SSUSI image in the map.
    ipc = panel_dmsp.overlay_pcolormesh(
        data=lbhs_, coords={'lat': mlat_, 'lon': mlon_, 'mlt': mlt_}, cs='AACGM', **pcolormesh_config)
    # Add a color bar
    panel_dmsp.add_colorbar(ipc, c_label=band + " (R)", c_scale=pcolormesh_config['c_scale'], left=1.08, bottom=0.1,
                            width=0.05, height=0.7)

    ict = panel_dmsp.overlay_contour(grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                     colors='y', levels=levels)

    # Overlay the gridlines
    panel_dmsp.overlay_gridlines(lat_res=5, lon_label_separator=5)

    # Overlay the coastlines in the AACGM coordinate
    panel_dmsp.overlay_coastlines()

    # Overlay cross-track velocity along satellite trajectory
    sc_dt = ds_s1['SC_DATETIME'].value.flatten()
    sc_lat = ds_s1['SC_GEO_LAT'].value.flatten()
    sc_lon = ds_s1['SC_GEO_LON'].value.flatten()
    sc_alt = ds_s1['SC_GEO_ALT'].value.flatten()

    ind_t1 = np.where((sc_dt > time_c - datetime.timedelta(minutes=35)) & (
                    sc_dt < time_c + datetime.timedelta(minutes=35)))[0]
    sc_coords = {'lat': sc_lat[ind_t1], 'lon': sc_lon[ind_t1], 'height': sc_alt[ind_t1]}

    v_H = ds_s1['v_i_H'].value.flatten()[ind_t1]
    panel_dmsp.overlay_cross_track_vector(
            vector=v_H, unit_vector=1000, vector_unit='m/s', alpha=0.2, color='c', vector_width=2.,
            sc_coords=sc_coords, sc_ut=sc_dt[ind_t1], cs='GEO', edge='on', edge_alpha=0.9, edge_color='c',
            legend_pos_x=0.9, legend_pos_y=0.9, legend_linewidth=2., legend_label= r'$v_i=1000$ m/s',
        )
    # Overlay the satellite trajectory with ticks
    panel_dmsp.overlay_sc_trajectory(
            sc_ut=sc_dt[ind_t1], sc_coords=sc_coords, cs='GEO', color='#9090C0',
            time_tick_label_rotation=90., time_tick_label_offset=0.1, time_tick_label_fontsize=10,
            time_tick_label_fontweight='bold', 
        )

    # # Overlay swarm satellite trajectory

    # sc2_dt = ds_grace['SC_DATETIME'].value.flatten()
    # sc2_lat = ds_grace['SC_GEO_LAT'].value.flatten()
    # sc2_lon = ds_grace['SC_GEO_LON'].value.flatten()
    # sc2_alt = ds_grace['SC_GEO_ALT'].value.flatten()
    # sc2_coords = {'lat': sc2_lat, 'lon': sc2_lon, 'height': sc2_alt}

    # u_H_grace = ds_grace['u_CROSS'].value.flatten()
    # panel1.overlay_cross_track_vector(
    #     vector=u_H_grace, unit_vector=1000, vector_unit='m/s', alpha=1, color='k',
    #     sc_coords=sc2_coords, sc_ut=sc2_dt, cs='GEO',
    # ) 
    # panel1.overlay_sc_trajectory(sc_ut=sc2_dt, sc_coords=sc2_coords, cs='GEO', color='m')

    # Overlay sites
    # panel_dmsp.overlay_sites(
    #    site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.}, cs='GEO',
    #    marker='^', markersize=5, color='purple')
    panel_tec.overlay_sites(
            site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
            cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r')

    panel_tec.overlay_sites(
            site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
            cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

    # Add the title and save the figure
    polestr = 'North' if pole == 'N' else 'South'
    panel_dmsp.add_title(
        title='DMSP/SSUSI, ' + band + ', ' + sat_id.upper() + ', ' + polestr + ', ' + time_c.strftime(
            '%Y-%m-%d %H%M UT'))

    # delta_t = 15
    # dt_fr = grace_dn - datetime.timedelta(minutes=delta_t)
    # dt_to = grace_dn + datetime.timedelta(minutes=delta_t)

    # timeline_extra_labels = ['GEO_LAT', 'GEO_LON', 'AACGM_LAT', 'AACGM_MLT']
    # db_g = TSDashboard(dt_fr=dt_fr, dt_to=dt_to, timeline_extra_labels=timeline_extra_labels, figure=dashboard.figure)

    # DMSP SSJ
    diff_minutes = 15
    dt_fr_2 = dmsp_dn - datetime.timedelta(minutes=diff_minutes / 2)
    dt_to_2 = dmsp_dn + datetime.timedelta(minutes=diff_minutes / 2)
    dashboard_2 = TSDashboard(dt_fr=dt_fr_2, dt_to=dt_to_2, figure=dashboard.figure,
                              timeline_extra_labels=['GEO_LAT', 'GEO_LON', 'AACGM_LAT', 'AACGM_MLT'])

    dataset_s1 = dashboard_2.dock(datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'], sat_id=sat_id)
    dataset_s4 = dashboard_2.dock(datasource_contents=['madrigal', 'satellites', 'dmsp', 's4'], sat_id=sat_id)
    dataset_e = dashboard_2.dock(datasource_contents=['madrigal', 'satellites', 'dmsp', 'e'], sat_id=sat_id)

    n_e = dashboard_2.assign_variable('n_e', dataset=dataset_s1)
    v_i_H = dashboard_2.assign_variable('v_i_H', dataset=dataset_s1)
    v_i_V = dashboard_2.assign_variable('v_i_V', dataset=dataset_s1)
    d_B_D = dashboard_2.assign_variable('d_B_D', dataset=dataset_s1)
    d_B_P = dashboard_2.assign_variable('d_B_P', dataset=dataset_s1)
    d_B_F = dashboard_2.assign_variable('d_B_F', dataset=dataset_s1)

    JE_e = dashboard_2.assign_variable('JE_e', dataset=dataset_e)
    JE_i = dashboard_2.assign_variable('JE_i', dataset=dataset_e)
    jE_e = dashboard_2.assign_variable('jE_e', dataset=dataset_e)
    jE_i = dashboard_2.assign_variable('jE_i', dataset=dataset_e)
    E_e_MEAN = dashboard_2.assign_variable('E_e_MEAN', dataset=dataset_e)
    E_i_MEAN = dashboard_2.assign_variable('E_i_MEAN', dataset=dataset_e)

    T_i = dashboard_2.assign_variable('T_i', dataset=dataset_s4)
    T_e = dashboard_2.assign_variable('T_e', dataset=dataset_s4)
    c_O_p = dashboard_2.assign_variable('COMP_O_p', dataset=dataset_s4)

    layout = [
        [v_i_H, v_i_V],
#        [d_B_P, d_B_D, d_B_F],
#        [E_e_MEAN, E_i_MEAN],
#        [JE_e, JE_i],
        [jE_e],
        [jE_i],
        [n_e, [c_O_p]],
        [T_i, T_e]
    ]
    dashboard_2.set_layout(panel_layouts=layout, left=0.55, right=0.9, hspace=0.01)
    dashboard_2.draw()
    # uts = dashboard_2.search_UTs(AACGM_LAT=66.6, GEO_LON=[8, 32])
    # if list(uts):
    #     dashboard_2.add_vertical_line(uts[0])
    # uts = dashboard_2.search_UTs(AACGM_LAT=75.4, GEO_LON=[0, 30])
    # if list(uts):
    #     dashboard_2.add_vertical_line(uts[0])
    dashboard_2.add_panel_labels()

    dashboard_2.save_figure(file_dir=fp_res, file_name='DMSP_TEC')
    dashboard_2.show()
    # db_swarm.show()

    # return dashboard


def event_1_1():
    dmsp_dn = datetime.datetime.strptime('20150215' + '190800', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f18'
    dmsp_orbit_id = '27478'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_2():
    dmsp_dn = datetime.datetime.strptime('20150215' + '172700', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f18'
    dmsp_orbit_id = '27477'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_3():
    dmsp_dn = datetime.datetime.strptime('20150215' + '204900', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f18'
    dmsp_orbit_id = '27479'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_4():
    dmsp_dn = datetime.datetime.strptime('20150215' + '193400', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f16'
    dmsp_orbit_id = '58456'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_5():
    dmsp_dn = datetime.datetime.strptime('20150215' + '175300', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f16'
    dmsp_orbit_id = '58455'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_6():
    dmsp_dn = datetime.datetime.strptime('20150215' + '211600', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f16'
    dmsp_orbit_id = '58457'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_7():
    dmsp_dn = datetime.datetime.strptime('20150215' + '181600', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f17'
    dmsp_orbit_id = '42734'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_8():
    dmsp_dn = datetime.datetime.strptime('20150215' + '195700', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f17'
    dmsp_orbit_id = '42735'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_9():
    dmsp_dn = datetime.datetime.strptime('20150215' + '213800', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f17'
    dmsp_orbit_id = '42736'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_10():
    dmsp_dn = datetime.datetime.strptime('20150215' + '184500', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f19'
    dmsp_orbit_id = '04493'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_11():
    dmsp_dn = datetime.datetime.strptime('20150215' + '202600', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f19'
    dmsp_orbit_id = '04494'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


def event_1_12():
    dmsp_dn = datetime.datetime.strptime('20150215' + '220800', '%Y%m%d%H%M%S')
    dmsp_sat_id = 'f19'
    dmsp_orbit_id = '04495'

    visual_dmsp_tec(dmsp_dn, dmsp_sat_id, dmsp_orbit_id, pole='N')


if __name__ == '__main__':
    event_1_1()
    event_1_2()
    event_1_3()
    event_1_4()
    event_1_5()
    event_1_6()
    event_1_7()
    event_1_8()
    event_1_9()
    event_1_10()
    event_1_11()
    event_1_12()
    # visual_solar_wind()
    # tec_omni_maps()
