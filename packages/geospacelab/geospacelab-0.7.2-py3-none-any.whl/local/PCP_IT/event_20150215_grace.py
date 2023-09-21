import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib

from geospacelab import preferences as pref

# pref.user_config['visualization']['mpl']['style'] = 'dark'  # or 'light'

import geospacelab.visualization.mpl.dashboards as dashboards
import geospacelab.visualization.mpl.geomap.geodashboards as geomap
from geospacelab.observatory.orbit.utilities import LEOToolbox

fp_res = pathlib.Path('/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results')


def show_grace_wind_and_tec():
    dts_grace = [
        datetime.datetime(2015, 2, 15, 17, 20),
        datetime.datetime(2015, 2, 15, 18, 55),
        datetime.datetime(2015, 2, 15, 20, 25),
        datetime.datetime(2015, 2, 15, 22, 00),
    ]

    dt_fr = datetime.datetime(2015, 2, 15, 15)
    dt_to = datetime.datetime(2015, 2, 15, 23, 59)

    # dts_grace = [
    #     datetime.datetime(2015, 2, 14, 16, 0),
    #     datetime.datetime(2015, 2, 14, 17, 30),
    #     datetime.datetime(2015, 2, 14, 19, 0),
    #     datetime.datetime(2015, 2, 14, 20, 30),
    # ]

    # dt_fr = datetime.datetime(2015, 2, 14, 15)
    # dt_to = datetime.datetime(2015, 2, 14, 23, 59)

    db = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (10, 10)})

    ds_tec = db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    tec = db.assign_variable('TEC_MAP', dataset_index=0)
    dts = db.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db.assign_variable('GEO_LON', dataset_index=0).value

    ds_grace = db.dock(datasource_contents=['tud', 'grace', 'wnd_acc'],
                   dt_fr=dt_fr, dt_to=dt_to, sat_id='A', product_version='v02',
                   add_APEX=False)
    grace_dt = ds_grace['SC_DATETIME'].value.flatten()
    grace_lat = ds_grace['SC_GEO_LAT'].value.flatten()
    grace_lon = ds_grace['SC_GEO_LON'].value.flatten()
    grace_alt = ds_grace['SC_GEO_ALT'].value.flatten()
    grace_v_H = ds_grace['u_CT'].flatten()

    ds_s1_f18 = db.dock(
        datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'],
        dt_fr=dt_fr,
        dt_to=dt_to,
        sat_id='f18', replace_orbit=True)

    ds_s1_f19 = db.dock(
        datasource_contents=['madrigal', 'satellites', 'dmsp', 's1'],
        dt_fr=dt_fr,
        dt_to=dt_to,
        sat_id='f19', replace_orbit=True)

    data_file_paths = [
        '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
    ds_sd = db.dock(
        datasource_contents=['superdarn', 'potmap'], load_mode='assigned', data_file_paths=data_file_paths)

    phi_sd = db.assign_variable('GRID_phi', dataset=ds_sd)
    dts_sd = db.assign_variable('DATETIME', dataset=ds_sd).value.flatten()
    mlat_sd = db.assign_variable('GRID_MLAT', dataset=ds_sd)
    mlon_sd = db.assign_variable('GRID_MLON', dataset=ds_sd)
    mlt_sd = db.assign_variable(('GRID_MLT'), dataset=ds_sd)

    db.set_layout(2, 2, wspace=0.3, left=0.08, right=0.88, top=0.92, bottom=0.08)
    for ind, time_c in enumerate(dts_grace):
        row = int(ind/2)
        col = ind % 2
        panel = db.add_polar_map(row_ind=row, col_ind=col, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c,
                                 boundary_lat=55)
        panel.overlay_coastlines()
        panel.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)
        #
        # retrieve the data array
        ind_t = ds_tec.get_time_ind(ut=time_c, time_res=300)
        tec_ = tec.value[ind_t]
        # Configuration for plotting
        pcolormesh_config = tec.visual.plot_config.pcolormesh
        pcolormesh_config.update(c_lim=[0, 14])
        import geospacelab.visualization.mpl.colormaps as cm
        # pcolormesh_config.update(cmap='GnBu')

        # overlay the 2-D TEC map
        ipc = panel.overlay_pcolormesh(
            tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
            regridding=True, grid_res=0.5,
            **pcolormesh_config,
        )
        if ind == len(dts_grace)-1:
            panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.3, width=0.07, height=1.5)

        ind_t = np.where((grace_dt > time_c - datetime.timedelta(minutes=25)) &
                         (grace_dt < time_c + datetime.timedelta(minutes=25)))[0]

        grace_coords = {'lat': grace_lat[ind_t], 'lon': grace_lon[ind_t], 'height': grace_alt[ind_t]}

        v_H = grace_v_H[ind_t]

        panel.overlay_cross_track_vector(
            vector=v_H, unit_vector=500, vector_unit='m/s', alpha=0.1, color='darkblue', vector_width=5,
            sc_coords=grace_coords, sc_ut=grace_dt[ind_t], cs='GEO', edge='on', edge_alpha=0.9, edge_color='darkblue',
            legend_pos_x=0.9, legend_pos_y=1.03, legend_linewidth=2., legend_label= r'$u=500$ m/s',
        )
        # # Overlay the satellite trajectory with ticks
        # panel1.overlay_sc_trajectory(sc_ut=sc_dt, sc_coords=sc_coords, cs='GEO')

        # Overlay swarm satellite trajectory
        panel.overlay_sc_trajectory(
            sc_ut=grace_dt[ind_t], sc_coords=grace_coords, cs='GEO', color='m',
            time_tick_label_rotation=90., time_tick_label_offset=-0.08, time_tick_label_fontsize=10, 
        )

        # overlay dmsp
        if ind in [0, 1]:
            ds_s1 = ds_s1_f18
        else:
            ds_s1 = ds_s1_f19

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
            legend_pos_x=0.9, legend_pos_y=0.9, legend_linewidth=2., legend_label= r'$v_i=1000$ m/s',
        )
        # Overlay the satellite trajectory with ticks
        panel.overlay_sc_trajectory(
            sc_ut=sc_dt[ind_t], sc_coords=sc_coords, cs='GEO', color='#9090C0',
            time_tick_label_rotation=90., time_tick_label_offset=0.1, time_tick_label_fontsize=10,
            time_tick_label_fontweight='bold', 
        )

        # overlay superdarn
        ind_t = ds_sd.get_time_ind(ut=time_c)
        # initialize the polar map
        
        phi_ = phi_sd.value[ind_t]
        mlat_ = mlat_sd.value[ind_t]
        mlt_ = mlt_sd.value[ind_t]
        mlon_ = mlon_sd.value[ind_t]
        
        grid_mlat, grid_mlt, grid_phi = ds_sd.grid_phi(mlat_, mlt_, phi_, interp_method='cubic')
        # grid_mlat, grid_mlt, grid_phi = ds_sd.postprocess_roll(mlat_, mlt_, phi_)
        
        levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
        levels = np.array([-35e3, -30e3, -25e3, -20e3, -15e3, -10e3, -5e3, 5e3, 10e3, 15e3, 20e3, 25e3, 30e3, 35e3])
        # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
        ict = panel.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                    colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7, regridding=True, sparsely=False)

        # Add sites
        panel.overlay_sites(
            site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
            cs='GEO', marker='o', markersize=5, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r')

        panel.overlay_sites(
            site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
            cs='GEO', marker='o', markersize=5, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

        panel.add_label(x=0.0, y=0.95, label="({:c})".format(ord('a')+ind), fontsize=15)
        panel.add_title(0.5, 1.1, title="T{:d}: {:s} UT".format(ind*2 + 1, time_c.strftime("%H:%M")), fontsize=12)

    db.save_figure(file_name="grace_wind_tec_v3", file_dir=fp_res)
    db.show()

    pass


def test_grace_wind_mapping():

    # Set the starting and stopping time
    time_c = datetime.datetime(2015, 2, 15, 20, 25)
    dt_fr = datetime.datetime(2015, 2, 15, 15)
    dt_to = datetime.datetime(2015, 2, 15, 23, 59)

    # time_c = datetime.datetime(2016, 2, 3, 1, 48)
    # dt_fr = datetime.datetime(2016, 2, 2, 15)
    # dt_to = datetime.datetime(2016, 2, 3, 23, 59)
    
    dt_fr_grace = time_c - datetime.timedelta(minutes=25)
    dt_to_grace = time_c + datetime.timedelta(minutes=25)
    add_APEX = True  # if True, "SC_APEX_LAT" and "SC_APEX_LON" will be added, default is False

    # Create a geodashboard object
    db = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (5, 5)})
    # Dock the GPS TEC maps
    ds_tec = db.dock(datasource_contents=['madrigal', 'gnss', 'tecmap'])
    # Dock the datasets. Different datasets store different types of data.
    # Dock the SWARM-A DNS-POD data
    ds_A = db.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], 
                   dt_fr=dt_fr_grace, dt_to=dt_to_grace, sat_id='A', product_version='v02',
                   add_APEX=add_APEX)
    # Dock the SWARM-C DNS-POD data
    ds_B = db.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], 
                   dt_fr=dt_fr_grace, dt_to=dt_to_grace, sat_id='B', product_version='v02',
                   add_APEX=add_APEX)
    
    tec = db.assign_variable('TEC_MAP', dataset_index=0)
    dts = db.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db.assign_variable('GEO_LON', dataset_index=0).value

    db.set_layout(1, 1, wspace=0.5)
    ind_t = ds_tec.get_time_ind(ut=time_c, time_res=300)

    # Add the first panel
    # AACGM LAT-MLT in the northern hemisphere
    panel = db.add_polar_map(row_ind=0, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole='N', ut=time_c, boundary_lat=50)
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
    panel.overlay_gridlines(lat_label_clock=4.2, lon_label_separator=5)
    #
    # retrieve the data array
    tec_ = tec.value[ind_t]
    # Configuration for plotting
    pcolormesh_config = tec.visual.plot_config.pcolormesh
    pcolormesh_config.update(c_lim=[0, 10])
    import geospacelab.visualization.mpl.colormaps as cm
    pcolormesh_config.update(cmap='GnBu')

    # overlay the 2-D TEC map
    ipc = panel.overlay_pcolormesh(
        tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
        regridding=True, grid_res=0.5,
        **pcolormesh_config,
    )
    panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.1, bottom=0.1, width=0.05, height=0.7)
    # add the panel title

    data_file_paths = [
        '/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/SuperDARN_potential_20150215.txt']
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

    levels = np.array([-35e3, -25e3, -15e3, -5e3, 5e3, 10e3, 15e3, 25e3, 35e3])
    levels = np.array([-35e3, -30e3, -25e3, -20e3, -15e3, -10e3, -5e3, 5e3, 10e3, 15e3, 20e3, 25e3, 30e3, 35e3])
    # ipc = panel1.add_pcolor(fac_, coords={'lat': mlat[ind_t, ::], 'lon': None, 'mlt': mlt[ind_t, ::], 'height': 250.}, cs='AACGM', **pcolormesh_config)
    ict = panel.overlay_contour(-grid_phi, coords={'lat': grid_mlat, 'lon': None, 'mlt': grid_mlt}, cs='AACGM',
                                  colors='darkgrey', levels=levels, linewidths=1.5, alpha=0.7)

    panel.add_title(title=time_c.strftime("%Y-%m-%d %H:%M"))
    
    # # Overlay grace crosswind 
    grace_dt = ds_A['SC_DATETIME'].value.flatten()
    grace_lat = ds_A['SC_GEO_LAT'].value.flatten()
    grace_lon = ds_A['SC_GEO_LON'].value.flatten()
    grace_alt = ds_A['SC_GEO_ALT'].value.flatten()
    grace_coords = {'lat': grace_lat, 'lon': grace_lon, 'height': grace_alt}
    #
    # ds_leo = LEOToolbox(dt_fr_grace, dt_to_grace)
    # ds_leo.clone_variables(ds_A)
    # orbit_unit_vector = ds_leo.trajectory_local_unit_vector()
    #
    # wind_unit_vector = np.concatenate(
    #     (
    #         ds_A['UNIT_VECTOR_N'].value,
    #         ds_A['UNIT_VECTOR_E'].value,
    #         ds_A['UNIT_VECTOR_D'].value
    #     ),
    #     axis=1
    # )
    #
    # cp = np.cross(orbit_unit_vector, wind_unit_vector)
    #
    # v_H = -np.sign(cp[:, 2]) * ds_A['u_CROSS'].value.flatten()
    v_H = ds_A['u_CT'].flatten()

    panel.overlay_cross_track_vector(
        vector=v_H, unit_vector=500, vector_unit='m/s', alpha=0.3, color='darkblue',
        sc_coords=grace_coords, sc_ut=grace_dt, cs='GEO', edge='on', edge_alpha=0.7, edge_color='darkblue'
    )
    # # Overlay the satellite trajectory with ticks
    # panel1.overlay_sc_trajectory(sc_ut=sc_dt, sc_coords=sc_coords, cs='GEO')

    
    # Overlay swarm satellite trajectory
    grace_dt = ds_A['SC_DATETIME'].value.flatten()
    grace_lat = ds_A['SC_GEO_LAT'].value.flatten()
    grace_lon = ds_A['SC_GEO_LON'].value.flatten()
    grace_alt = ds_A['SC_GEO_ALT'].value.flatten()
    grace_coords = {'lat': grace_lat, 'lon': grace_lon, 'height': grace_alt}

    panel.overlay_sc_trajectory(
        sc_ut=grace_dt, sc_coords=grace_coords, cs='GEO', color='m',
        time_tick_label_rotation=90., time_tick_label_offset=-0.08)

    # Add sites
    panel.overlay_sites(
        site_ids=['TRO', 'ESR'], coords={'lat': [69.58, 78.15], 'lon': [19.23, 16.02], 'height': 0.},
            cs='GEO', marker='^', markersize=8, color='purple', alpha=1)
    
    # db.save_figure(file_name=f"test2_grace_mapping_{time_c.strftime('%Y%m%d_%H%M')}.png")
    db.show()


def test_grace_wind():
    # Set the starting and stopping time
    dt_fr = datetime.datetime(2015, 2, 14, 15)
    dt_to = datetime.datetime(2015, 2, 14, 23, 59)
    add_APEX = True  # if True, "SC_APEX_LAT" and "SC_APEX_LON" will be added, default is False

    # Create a dashboard object, equivalent to a datahub object, however, with the additional visulization control.
    db = dashboards.TSDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (12, 8)})

    # Dock the datasets. Different datasets store different types of data.
    # Dock the SWARM-A DNS-POD data
    ds_A = db.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='A', product_version='v02',
                   add_APEX=add_APEX)
    # Dock the SWARM-C DNS-POD data
    ds_B = db.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='B', product_version='v02',
                   add_APEX=add_APEX)

    # Assign variables from the datasets for visualization.
    u_A = db.assign_variable('u_CROSS', dataset=ds_A)
    u_B = db.assign_variable('u_CROSS', dataset=ds_B)
    u_A.visual.axis[1].label = r'$u$'
    u_A.visual.axis[2].label = 'GRACE-A'
    u_B.visual.axis[2].label = 'GRACE-B'

    glat_A = db.assign_variable('SC_GEO_LAT', dataset=ds_A)
    glat_B = db.assign_variable('SC_GEO_LAT', dataset=ds_B)
    glat_A.visual.axis[2].label = 'GRACE-A'
    glat_B.visual.axis[2].label = 'GRACE-B'

    glon_A = db.assign_variable('SC_GEO_LON', dataset=ds_A)
    glon_B = db.assign_variable('SC_GEO_LON', dataset=ds_B)
    lst_A = db.assign_variable('SC_GEO_LST', dataset=ds_A)

    glon_A.visual.axis[2].label = 'GRACE-A'
    glon_B.visual.axis[2].label = 'GRACE-C'
    # Dock the dataset for the geomagnetic activity indices.
    ds1 = db.dock(datasource_contents=['wdc', 'asysym'])
    sym_h = db.assign_variable('SYM_H', dataset=ds1)

    # Set the plotting layout
    db.set_layout([[sym_h], [u_A, u_B], [glat_A, glat_B], [glon_A, [lst_A]]])
    db.draw()
    # plt.savefig('swarm_example', dpi=300)
    plt.savefig('grace_2')
    # plt.savefig('2.png')
    # Extract the data array from variables:
    rho_n_A_array = u_A.value
    
    
if __name__ == "__main__":
    show_grace_wind_and_tec()
    # test_grace_wind()
    