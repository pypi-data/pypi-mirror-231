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


def show_IMF_and_TEC():
    fig = create_figure(figsize=(10, 10))

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
    ds_6 = db_omni.dock(datasource_contents=['fmi', 'image', 'ie'], data_file_paths=[fp_ie])

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

    layout = [[Bx, By, Bz], [ncf], [sme, ie]]
    db_omni.set_layout(panel_layouts=layout, left=0.2, right=0.8, top=0.9, bottom=0.6)
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

    db_tec.set_layout(2, 4, left=0.05, right=0.9, bottom=0.05, top=0.52, wspace=0.19, )
    ind = 0
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
            panel.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)

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
                                             **pcolormesh_config, regridding=True, grid_res=0.5)

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

            panel.overlay_sites(
                site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
                cs='GEO', marker='o', markersize=5, color='k', alpha=1, markerfacecolor='white', markeredgecolor='k')

            panel.add_label(x=0.0, y=0.95, label="(d{:d})".format(ind+1), fontsize=12)
            panel.add_title(0.5, 1.1, title="T{:d}: {:s} UT".format(ind+1, time_c.strftime("%H:%M")), fontsize=12)
            ind += 1
    db_omni.save_figure(file_name="IMF_with_TECs_20150215", file_dir=file_dir_root)
    pass

def show_IMF():
    dt_fr_omni = datetime.datetime(2015, 2, 15, 15)
    dt_to_omni = datetime.datetime(2015, 2, 16, 0)
    # dt_fr_omni = datetime.datetime(2015, 2, 27, 0)
    # dt_to_omni = datetime.datetime(2015, 2, 28, 0)
    db_omni = TSDashboard(dt_fr=dt_fr_omni, dt_to=dt_to_omni, figure_config={'figsize': (7, 3.5)})

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
    # fp_ie = '/home/lei/extra/AFEISCAT3/Data/Indices/IL/IL20150215.dat'
    ds_6 = db_omni.dock(datasource_contents=['fmi', 'image', 'ie'])

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

    layout = [[Bx, By, Bz], [E_sw, [ncf]], [sme, ie]]
    db_omni.set_layout(panel_layouts=layout, left=0.14, right=0.88)
    db_omni.draw()
    # db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
    # db_omni.add_shading(dt_fr, time_c, alpha=0.15)
    db_omni.add_panel_labels()
    db_omni.save_figure(file_name='omni_geomag_v3', file_dir=file_dir_root)
    db_omni.show()


def show_TECs():
    file_path = file_dir_root / "Quiet_TEC_for_Event_2015_02_15_5days.pickle"
    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    def tec_omni_draw(time_c):
        dt_fr_tec = datetime.datetime(2015, 2, 15, 15)
        dt_to_tec = datetime.datetime(2015, 2, 15, 23, 59)
        # diff_sec = (dt_to - dt_fr).total_seconds()
        # times = [dt_fr + datetime.timedelta(seconds=sec) for sec in np.arange(0, diff_sec + 1, 300)]

        db = GeoDashboard(dt_fr=dt_fr_tec, dt_to=dt_to_tec, figure_config={'figsize': (14, 8)})
        db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])

        tec = db.assign_variable('TEC_MAP', dataset_index=0)
        dts = db.assign_variable('DATETIME', dataset_index=0).value.flatten()
        glat = db.assign_variable('GEO_LAT', dataset_index=0).value
        glon = db.assign_variable('GEO_LON', dataset_index=0).value

        dt_fr_omni = datetime.datetime(2015, 2, 15, 14)
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

        Bx = db_omni.assign_variable('B_x_GSM', dataset=db_omni.datasets[0])
        By = db_omni.assign_variable('B_y_GSM', dataset=db_omni.datasets[0])
        Bz = db_omni.assign_variable('B_z_GSM', dataset=db_omni.datasets[0])

        n_p = db_omni.assign_variable('n_p', dataset=db_omni.datasets[0])
        v_sw = db_omni.assign_variable('v_sw', dataset=db_omni.datasets[0])
        v_sw.visual.axis[1].lim = [200, 500]
        p_dyn = db_omni.assign_variable('p_dyn', dataset=db_omni.datasets[0])

        au = db_omni.assign_variable('AU', dataset=db_omni.datasets[1])
        au.visual.axis[1].lim = [None, None]
        al = db_omni.assign_variable('AL', dataset=db_omni.datasets[1])
        ae = db_omni.assign_variable('AE', dataset=db_omni.datasets[1])

        sym_h = db_omni.assign_variable('SYM_H', dataset=db_omni.datasets[2])
        sym_h.visual.axis[1].lim = [None, None]
        sym_h.visual.axis[1].label = '@v.label'

        kp = db_omni.assign_variable('Kp', dataset=db_omni.datasets[3])

        layout = [[Bx, By, Bz], [v_sw], [au, al, ae]]
        db_omni.set_layout(panel_layouts=layout, left=0.07, top=0.75, bottom=0.25, right=0.4)
        db_omni.draw()
        db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
        db_omni.add_shading(dt_fr, time_c, alpha=0.15)
        db_omni.add_panel_labels()

        # plt.style.use('dark_background')
        # dt_fr_1 = datetime.datetime.strptime('20201209' + '1300', '%Y%m%d%H%M')
        # dt_to_1 = datetime.datetime.strptime('20201210' + '1200', '%Y%m%d%H%M')

        db.set_layout(2, 2, left=0.47, right=0.92, bottom=0.05, top=0.9, wspace=0.45, )
        ##################### quiet tec #################
        panel_1 = db.add_polar_map(
            row_ind=0, col_ind=0,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        panel_1.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)
        ind_t_q = int((time_c - dttool.get_start_of_the_day(time_c)).total_seconds() / 300)
        tec_ = data['TEC_MAP_Quiet'][ind_t_q]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[0, 14])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel_1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                         **pcolormesh_config, regridding=True, grid_res=0.5)
        panel_1.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
        panel_1.overlay_coastlines()
        panel_1.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=8, color='purple', alpha=1)

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel_1.add_title(title='Quiet TEC\n' + time_c.strftime("%H:%M UT"), fontsize=18)

        ####################################################################################################
        panel_2 = db.add_polar_map(
            row_ind=0, col_ind=1,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        # panel1 = db.add_polar_map(
        #     row_ind=0, col_ind=0,
        #     style='lst-fixed', cs='GEO', lst_c=0.,
        #     pole='N', ut=time_c, boundary_lat=55,
        #     )
        panel_2.overlay_coastlines()
        panel_2.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)

        ind_t_c = np.where(dts == time_c)[0]
        if not list(ind_t_c):
            return
        tec_ = tec.value[ind_t_c[0], :, :]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[0, 14])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel_2.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                        **pcolormesh_config, regridding=True, grid_res=0.5)

        # ipc = panel1.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO', **pcolormesh_config)
        panel_2.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)

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
        # levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
        # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
        ict = panel_2.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                     colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7)

        # Add sites
        panel_2.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=8, color='purple', alpha=1)

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel_2.add_title(title='TEC\n' + time_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=18)

        ##################### delta tec #################
        panel_3 = db.add_polar_map(
            row_ind=1, col_ind=0,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        panel_3.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)
        ind_t_q = int((time_c - dttool.get_start_of_the_day(time_c)).total_seconds() / 300)
        tec_ = tec.value[ind_t_c[0]] - data['TEC_MAP_Quiet'][ind_t_q]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[-15, 15])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel_3.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                         **pcolormesh_config, regridding=True, grid_res=0.5)
        panel_3.add_colorbar(ipc, c_label=r"$\Delta$TEC", c_scale='linear', left=1.1, bottom=0.1, width=0.05,
                             height=0.7)
        panel_3.overlay_coastlines()
        panel_3.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=8, color='purple', alpha=1)

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel_3.add_title(title="$\Delta$TEC\n" + time_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=18)

        ##################### delta tec percentation#################
        panel_4 = db.add_polar_map(
            row_ind=1, col_ind=1,
            style='mlt-fixed', cs='AACGM', mlt_c=0.,
            pole='N', ut=time_c, boundary_lat=55,
        )
        panel_4.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)
        ind_t_q = int((time_c - dttool.get_start_of_the_day(time_c)).total_seconds() / 300)
        tec_ = (tec.value[ind_t_c[0]] - data['TEC_MAP_Quiet'][ind_t_q]) / data['TEC_MAP_Quiet'][ind_t_q]
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[-4, 4])

        # import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='jet')
        ipc = panel_4.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                         **pcolormesh_config, regridding=True, grid_res=0.5)
        panel_4.add_colorbar(ipc, c_label=r"Ratio", c_scale='linear', left=1.1, bottom=0.1, width=0.05,
                             height=0.7)
        panel_4.overlay_coastlines()
        panel_4.overlay_sites(
            site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=8, color='purple', alpha=1)

        # # viewer.add_text(0.5, 1.1, "dashboard title")
        panel_4.add_title(title='rTEC\n' + time_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=18)

        fp_res_rec = file_dir_root / "delta_TEC_MAPS_AACGM_MLT" / "qd_5"
        fp_res_rec.mkdir(exist_ok=True)
        db.save_figure(fp_res_rec /  ("TEC_MAP_OMNI_" + time_c.strftime("%Y-%m-%d_%H%M")), append_time=False)
        print(time_c)

    dt_fr = datetime.datetime(2015, 2, 15, 15)
    dt_to = datetime.datetime(2015, 2, 15, 23, 0)
    diff_sec = (dt_to - dt_fr).total_seconds()
    times = [dt_fr + datetime.timedelta(seconds=sec) for sec in np.arange(0, diff_sec + 1, 300)]

    for time_0 in times:
        tec_omni_draw(time_0)


def calc_quiet_tec():
    quiet_days = [
        datetime.datetime(2015, 1, 25),
        datetime.datetime(2015, 2, 13),
        datetime.datetime(2015, 2, 14),
        datetime.datetime(2015, 2, 22),
        datetime.datetime(2015, 2, 27)
    ]
    # quiet_days = [
    #     datetime.datetime(2011, 2, 12),
    #     datetime.datetime(2011, 2, 13),
    #     datetime.datetime(2012, 2, 11),
    #     datetime.datetime(2012, 2, 12),
    #     datetime.datetime(2013, 2, 12),
    #     datetime.datetime(2013, 2, 13),
    #     datetime.datetime(2013, 2, 13),
    #     datetime.datetime(2013, 2, 14),
    #     datetime.datetime(2016, 2, 15),
    #     datetime.datetime(2017, 2, 12),
    #     datetime.datetime(2017, 2, 13),
    #     datetime.datetime(2017, 2, 14),
    #     datetime.datetime(2017, 2, 15),
    #     datetime.datetime(2017, 2, 16),
    #     datetime.datetime(2018, 2, 12),
    #     datetime.datetime(2018, 2, 13),
    #     datetime.datetime(2018, 2, 14),
    #     datetime.datetime(2019, 2, 15),
    #     datetime.datetime(2019, 2, 16),
    #     datetime.datetime(2019, 2, 17),
    #     datetime.datetime(2015, 1, 25),
    #     datetime.datetime(2015, 2, 13),
    #     datetime.datetime(2015, 2, 14),
    #     datetime.datetime(2015, 2, 22),
    #     datetime.datetime(2015, 2, 27)
    # ]

    hhs = range(24)
    for hh in hhs:
        print(hh)
        dh = DataHub()
        ds_list = []
        for qd in quiet_days:
            print(qd)
            delta_t = datetime.timedelta(minutes=10)
            dt_fr = qd + datetime.timedelta(hours=hh)
            dt_to = qd + datetime.timedelta(hours=hh + 1)
            ds = dh.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'], dt_fr=dt_fr - delta_t,
                         dt_to=dt_to + delta_t)
            ds_list.append(ds)
        times = [
            dt_fr + datetime.timedelta(seconds=sec)
            for sec in np.arange(0, (dt_to - dt_fr).total_seconds() - 1, 300)
        ]

        for ind, ds in enumerate(ds_list):
            tec_ = ds['TEC_MAP'].value

            nt = tec_.shape[0]
            print(nt)
            for ii in range(nt):
                if ii < 2 or ii > nt - 3:
                    continue
                tec_[ii, ::] = np.nanmean(tec_[ii - 2: ii + 3], axis=0)
            if ind == 0:
                tec_arr = tec_[:, :, :, np.newaxis]
            else:
                tec_arr = np.concatenate((tec_arr, tec_[:, :, :, np.newaxis]), axis=3)

        tec_arr = np.nanmin(tec_arr, axis=3)
        tec_arr = tec_arr[2:14, ::]
        if hh == 0:
            tec_arrs = np.array(tec_arr)
        else:
            tec_arrs = np.concatenate((tec_arrs, tec_arr), axis=0)

    data = {
        'TEC_MAP_Quiet': tec_arrs,
        'Quiet_Days': quiet_days
    }
    file_path = file_dir_root / "Quiet_TEC_for_Event_2015_02_15_5days.pickle"
    with open(file_path, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    return tec_arrs



if __name__ == "__main__":
    # calc_quiet_tec()
    show_IMF()
    # show_IMF_and_TEC()
    # show_TECs()
