import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib

from geospacelab import preferences as pref
import geospacelab.visualization.mpl as mpl

# pref.user_config['visualization']['mpl']['style'] = 'dark'  # or 'light'

import geospacelab.visualization.mpl.dashboards as dashboards
from geospacelab.visualization.mpl.dashboards import TSDashboard
from geospacelab.visualization.mpl.geomap.geodashboards import GeoDashboard
import geospacelab.observatory.earth.geodesy as gd
from geospacelab.observatory.orbit.utilities import LEOToolbox

fd_root = pathlib.Path('/home/lei/01-Work/01-Project/OY20-ISSI_IT/Event_201603/')


def overview_1(dt_fr, dt_to):
    fig = mpl.create_figure(figsize=(16, 9))
    
    db_1 = fig.add_dashboard(dashboard_class=TSDashboard, dt_fr=dt_fr, dt_to=dt_to)
    
    ds_A_dns = db_1.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='A', product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_B_dns = db_1.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='B', product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_A_wnd = db_1.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='A', product_version='v02',
                   add_APEX=False)
    ds_B_wnd = db_1.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='B', product_version='v02',
                   add_APEX=False)
    
    ds_A = ds_A_dns.interp_evenly()
    ds_B = ds_B_dns.interp_evenly()
    ds_sym = db_1.dock(datasource_contents=['wdc', 'asysym'])
    ds_ae = db_1.dock(datasource_contents=['wdc', 'ae'])
    ds_sm = db_1.dock(datasource_contents=['supermag', 'indices'])
    
    calc_diff_AB_by_time(ds_A, ds_B)
    D = calc_d_between_A_and_B(ds_A, ds_B)
    
    rho_scale = 1e12
    rho_unit = r'$\times 10^{-12}$ kg$\cdot$m$^{-3}$'
    rho_A = ds_A['rho_n']
    rho_B = ds_B['rho_n']
    rho_A.visual.axis[1].data_scale = rho_scale
    rho_A.visual.axis[1].unit = rho_unit
    rho_A.visual.axis[1].label = r'$\rho$'
    rho_A.visual.axis[2].label = 'GRACE-A'
    rho_A.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}
    rho_B.visual.axis[1].data_scale = rho_scale
    rho_B.visual.axis[1].unit = rho_unit
    rho_B.visual.axis[2].label = 'GRACE-B'
    rho_B.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}
    diff_rho = ds_A['DIFF_rho_n_ABS']
    diff_rho.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.5, 'color': 'grey'}
    diff_rho_perc = ds_A['PERC_DIFF_rho_n']
    
    u_H_A = ds_A_wnd['u_CT']
    u_H_A.visual.axis[1].lim = [-600, 800]
    u_H_B = ds_B_wnd['u_CT']
    u_H_B.visual.axis[1].lim = [-600, 800]
    u_H_A.visual.axis[2].label = 'GRACE-A'
    u_H_A.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}
    u_H_B.visual.axis[2].label = 'GRACE-B'
    u_H_B.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}

    glat_A = db_1.assign_variable('SC_GEO_LAT', dataset=ds_A)
    glat_B = db_1.assign_variable('SC_GEO_LAT', dataset=ds_B)
    glat_A.visual.axis[2].label = 'GRACE-A'
    glat_B.visual.axis[2].label = 'GRACE-B'

    glon_A = db_1.assign_variable('SC_GEO_LON', dataset=ds_A)
    glon_B = db_1.assign_variable('SC_GEO_LON', dataset=ds_B)
    alt_A = db_1.assign_variable('SC_GEO_ALT', dataset=ds_A)
    alt_A.label = 'h'
    alt_A.visual.axis[1].lim = [360, 410]
    alt_A.visual.axis[1].unit = 'km'
    alt_A.visual.plot_config.line = {'linestyle': '', 'marker': '.'} 
    lst_A = db_1.assign_variable('SC_GEO_LST', dataset=ds_A)
    lst_A.visual.plot_config.line = {'linestyle': '', 'marker': '.'} 
    lst_A.visual.axis[1].label = 'LST'
    lst_A.visual.axis[1].unit = 'h'

    glon_A.visual.axis[2].label = 'GRACE-A'
    glon_B.visual.axis[2].label = 'GRACE-B'

    # Dock the dataset for the geomagnetic activity indices.
    sym_h = db_1.assign_variable('SYM_H', dataset=ds_sym)
    sym_h.visual.axis[1].label = 'SYM-H' 
    sme = db_1.assign_variable('SME', dataset=ds_sm)
    sme.visual.axis[1].label = 'SME'

    D = ds_A['d_AB']
    panel_layouts = [[sym_h, [sme]], [rho_A, rho_B,], [u_H_A, u_H_B], [glat_A], [alt_A, [lst_A], [D]]]
    db_1.set_layout(panel_layouts=panel_layouts, left=0.08, right=0.92, top=0.92, bottom=0.08      )
    db_1.draw()
    
    fd_res = fd_root / "GRACE"
    fd_res.mkdir(parents=True, exist_ok=True)
    fn_res = 'GRACE_overview_' + dt_fr.strftime("%Y%m%d_%H%M") + '-' + dt_to.strftime("%Y%m%d_%H%M") + '.png'
    fig.savefig(fd_res / fn_res, dpi=300)
    db_1.show()
    
def overview_with_maps():
    fig = mpl.create_figure(figsize=(12, 10))
    
    dt_fr_1 = datetime.datetime(2016, 3, 14, 0)
    dt_to_1 = datetime.datetime(2016, 3, 21, 0)
    db_1 = fig.add_dashboard(dashboard_class=TSDashboard, dt_fr=dt_fr_1, dt_to=dt_to_1)
    
    ds_A_dns = db_1.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='A', product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_B_dns = db_1.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='B', product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_A_wnd = db_1.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='A', product_version='v02',
                   add_APEX=False)
    
    ds_A = ds_A_dns.interp_evenly()
    ds_B = ds_B_dns.interp_evenly()
    ds_sym = db_1.dock(datasource_contents=['wdc', 'asysym'])
    ds_ae = db_1.dock(datasource_contents=['wdc', 'ae'])
    ds_sm = db_1.dock(datasource_contents=['supermag', 'indices'])
    
    calc_diff_AB_by_time(ds_A, ds_B)
    D = calc_d_between_A_and_B(ds_A, ds_B)
    
    rho_A = ds_A['rho_n']
    rho_B = ds_B['rho_n']
    rho_A.visual.axis[1].label = r'$\rho$'
    rho_A.visual.axis[2].label = 'GRACE-A'
    rho_A.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}
    rho_B.visual.axis[2].label = 'GRACE-B'
    rho_B.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.8}
    diff_rho = ds_A['DIFF_rho_n_ABS']
    diff_rho.visual.plot_config.line = {'linestyle': '-', 'marker': '', 'alpha': 0.5, 'color': 'grey'}
    diff_rho_perc = ds_A['PERC_DIFF_rho_n']
    
    u_H = ds_A_wnd['u_CT']
    u_H.visual.axis[1].lim = [-600, 800]

    glat_A = db_1.assign_variable('SC_GEO_LAT', dataset=ds_A)
    glat_B = db_1.assign_variable('SC_GEO_LAT', dataset=ds_B)
    glat_A.visual.axis[2].label = 'GRACE-A'
    glat_B.visual.axis[2].label = 'GRACE-B'

    glon_A = db_1.assign_variable('SC_GEO_LON', dataset=ds_A)
    glon_B = db_1.assign_variable('SC_GEO_LON', dataset=ds_B)
    alt_A = db_1.assign_variable('SC_GEO_ALT', dataset=ds_A)
    alt_A.unit = 'km'
    alt_A.label = 'h'
    alt_A.visual.axis[1].lim = [360, 410]
    alt_A.visual.plot_config.line = {'linestyle': '', 'marker': '.'} 
    lst_A = db_1.assign_variable('SC_GEO_LST', dataset=ds_A)

    glon_A.visual.axis[2].label = 'GRACE-A'
    glon_B.visual.axis[2].label = 'GRACE-C'

    # Dock the dataset for the geomagnetic activity indices.
    sym_h = db_1.assign_variable('SYM_H', dataset=ds_sym)
    sym_h.visual.axis[1].label = 'SYM-H' 
    sme = db_1.assign_variable('SME', dataset=ds_sm)
    sme.visual.axis[1].label = 'SME'

    D = ds_A['d_AB']
    panel_layouts = [[sym_h, [sme]], [rho_A, rho_B,], [u_H], [glat_A], [alt_A, [D]]]
    
    dt_fr_2 = datetime.datetime(2016, 3, 14, 12)
    dt_to_2 = datetime.datetime(2016, 3, 20, 0)
    db_2 = fig.add_dashboard(dashboard_class=GeoDashboard, dt_fr=dt_fr_2, dt_to=dt_to_2)
    db_2.set_layout(1, 2, wspace=0.4, top=0.4, bottom=0.03)
    
    ds_A_dns = db_2.dock(datasource_contents=['tud', 'grace', 'dns_acc'], sat_id='A', product_version='v02',
                                  add_APEX=False, add_AACGM=False)
    ds_A_wnd = db_1.dock(datasource_contents=['tud', 'grace', 'wnd_acc'], sat_id='A', product_version='v02',
                   add_APEX=False)
    
    ds_leo = LEOToolbox(dt_fr_2, dt_to_2)
    ds_leo.clone_variables(ds_A_dns)
    ds_leo.search_orbit_nodes()

    nodes_N = ds_leo.northern_nodes['INDEX']
    nodes_S = ds_leo.southern_nodes['INDEX']
    cs = 'GEO'
    dt_0 = ds_A_dns['SC_DATETIME'].flatten()[nodes_N[0]]
    for ind_N in nodes_N:
        pole = 'N'
        dt_c = ds_A_dns['SC_DATETIME'].flatten()[ind_N]
        dt_c_0 = ds_A_dns['SC_DATETIME'].flatten()[ind_N]
        dt_1 = dt_c - datetime.timedelta(minutes=30)
        dt_2 = dt_c + datetime.timedelta(minutes=30)
        grace_data = ds_A_dns['rho_n'].flatten()
        grace_dt = ds_A_dns['SC_DATETIME'].flatten()
        grace_lat = ds_A_dns['SC_GEO_LAT'].flatten()
        grace_lon = ds_A_dns['SC_GEO_LON'].flatten()
        grace_alt = ds_A_dns['SC_GEO_ALT'].flatten()

        ind_t_c = np.where((grace_dt> dt_1) & (grace_dt < dt_2))[0]
        if not list(ind_t_c):
            plt.clf()
            continue

        grace_coords = {'lat': grace_lat[ind_t_c], 'lon': grace_lon[ind_t_c], 'height': grace_alt[ind_t_c]}

        if cs == 'GEO':
            panel = db_2.add_polar_map(row_ind=0, col_ind=0, style='lst-fixed', cs=cs, lst_c=0., pole=pole, ut=dt_c,
                                     boundary_lat=0, mirror_south=True)
        elif cs == 'AACGM':
            panel = db_2.add_polar_map(row_ind=0, col_ind=0, style='mlt-fixed', cs='AACGM', mlt_c=0., pole=pole, ut=dt_c,
                                     boundary_lat=55, mirror_south=True)

        panel.overlay_sc_trajectory(sc_ut=grace_dt[ind_t_c], sc_coords=grace_coords, cs='GEO', color='m',
                                    time_minor_tick=False, time_tick_label_rotation=90.,
                                    time_tick_label_offset=0.09)

        c_lim = [1e-14, 5e-12]
        ilc = panel.overlay_sc_coloured_line(
            grace_data[ind_t_c], sc_coords=grace_coords, sc_ut=grace_dt[ind_t_c], cs='GEO', line_width=8,
            c_scale='linear', c_lim=c_lim
        )

        u_dts = ds_A_wnd['SC_DATETIME'].value.flatten()
        ind_t_c = np.where((u_dts> dt_1) & (u_dts < dt_2))[0]
        if not list(ind_t_c):
            plt.clf()
            continue
        u_dt = u_dts[ind_t_c]
        u_lat = ds_A_wnd['SC_GEO_LAT'].value.flatten()[ind_t_c]
        u_lon = ds_A_wnd['SC_GEO_LON'].value.flatten()[ind_t_c]
        u_alt = ds_A_wnd['SC_GEO_ALT'].value.flatten()[ind_t_c]
        u_coords = {'lat': u_lat, 'lon': u_lon, 'height': u_alt}

        u_H = ds_A_wnd['u_CT'].flatten()[ind_t_c]

        panel.overlay_cross_track_vector(
            vector=u_H, unit_vector=200, vector_unit='m/s', alpha=0.3, color='k', vector_width=2,
            sc_coords=u_coords, sc_ut=u_dt, cs='GEO', edge='on', edge_alpha=0.8, edge_color='orange'
        )
        panel.add_colorbar(ilc, c_label=r'$\rho_n$')
        panel.overlay_coastlines()
        panel.overlay_gridlines(lat_label_clock=8, lon_label_separator=5)
        panel.add_title(0.5, 1.12, r"GRACE-A, Northern Hemisphere, " + dt_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=12)
        
        ################################
        pole = 'S'
        ind_11 = np.where(np.array(nodes_S)>ind_N)[0]
        dts = ds_A_dns['SC_DATETIME'].flatten()
        if list(ind_11):
            if (dts[nodes_S[ind_11[0]]] - dts[ind_N]).total_seconds() < 110 * 60:
                ind_c = nodes_S[ind_11[0]]
            else:
                fig.clf()
                continue
        else:
            fig.clf()
            continue
        dt_c = ds_A_dns['SC_DATETIME'].flatten()[ind_c]
        dt_1 = dt_c - datetime.timedelta(minutes=30)
        dt_2 = dt_c + datetime.timedelta(minutes=30)
        grace_data = ds_A_dns['rho_n'].flatten()
        grace_dt = ds_A_dns['SC_DATETIME'].flatten()
        grace_lat = ds_A_dns['SC_GEO_LAT'].flatten()
        grace_lon = ds_A_dns['SC_GEO_LON'].flatten()
        grace_alt = ds_A_dns['SC_GEO_ALT'].flatten()

        ind_t_c = np.where((grace_dt> dt_1) & (grace_dt < dt_2))[0]
        if not list(ind_t_c):
            plt.clf()
            continue

        grace_coords = {'lat': grace_lat[ind_t_c], 'lon': grace_lon[ind_t_c], 'height': grace_alt[ind_t_c]}

        if cs == 'GEO':
            panel = db_2.add_polar_map(row_ind=0, col_ind=1, style='lst-fixed', cs=cs, lst_c=0., pole=pole, ut=dt_c,
                                     boundary_lat=0, mirror_south=True)
        elif cs == 'AACGM':
            panel = db_2.add_polar_map(row_ind=0, col_ind=1, style='mlt-fixed', cs='AACGM', mlt_c=0., pole=pole, ut=dt_c,
                                     boundary_lat=55, mirror_south=True)

        panel.overlay_sc_trajectory(sc_ut=grace_dt[ind_t_c], sc_coords=grace_coords, cs='GEO', color='m',
                                    time_minor_tick=False, time_tick_label_rotation=0.,
                                    time_tick_label_offset=0.09)

        c_lim = [1e-14, 5e-12]
        ilc = panel.overlay_sc_coloured_line(
            grace_data[ind_t_c], sc_coords=grace_coords, sc_ut=grace_dt[ind_t_c], cs='GEO', line_width=8,
            c_scale='linear', c_lim=c_lim
        )

        u_dts = ds_A_wnd['SC_DATETIME'].value.flatten()
        ind_t_c = np.where((u_dts> dt_1) & (u_dts < dt_2))[0]
        if not list(ind_t_c):
            plt.clf()
            continue
        u_dt = u_dts[ind_t_c]
        u_lat = ds_A_wnd['SC_GEO_LAT'].value.flatten()[ind_t_c]
        u_lon = ds_A_wnd['SC_GEO_LON'].value.flatten()[ind_t_c]
        u_alt = ds_A_wnd['SC_GEO_ALT'].value.flatten()[ind_t_c]
        u_coords = {'lat': u_lat, 'lon': u_lon, 'height': u_alt}

        u_H = ds_A_wnd['u_CT'].flatten()[ind_t_c]

        panel.overlay_cross_track_vector(
            vector=u_H, unit_vector=200, vector_unit='m/s', alpha=0.3, color='k', vector_width=2,
            sc_coords=u_coords, sc_ut=u_dt, cs='GEO', edge='on', edge_alpha=0.8, edge_color='orange'
        )
        panel.add_colorbar(ilc, c_label=r'$\rho_n$')
        panel.overlay_coastlines()
        panel.overlay_gridlines(lat_label_clock=8, lon_label_separator=5)
        panel.add_title(0.5, 1.12, r"Southern Hemisphere, " + dt_c.strftime("%Y-%m-%d %H:%M UT"), fontsize=12)
        
        ################################
        db_1.set_layout(panel_layouts=panel_layouts, left=0.08, right=0.9, top=0.98, bottom=0.51)
        db_1.draw()
        # db_omni.add_vertical_line(time_c, color='r', linewidth=2, linestyle='-')
        # db_omni.add_shading(dt_fr, time_c, alpha=0.15)
        db_1.add_panel_labels()
        db_1.add_vertical_line(dt_c_0, color='r', linewidth=2, linestyle='-')
        db_1.add_shading(dt_0, dt_c_0, alpha=0.1)
        db_1.add_panel_labels()
        
        fp_res_rec = fd_res / "overview_with_maps"
        fp_res_rec.mkdir(exist_ok=True)
        fp_res_rec = fp_res_rec / ("overview_with_maps_" + dt_c_0.strftime("%Y-%m-%d_%H%M") + ".jpg")
        print(dt_c_0)
        fig.savefig(fp_res_rec, format='JPEG')

        db_1.clear()
        db_1.clear()
        fig.clf()
        
    
def calc_diff_AB_by_time(ds_A, ds_B):
    rho_A = ds_A['rho_n']
    rho_B = ds_B['rho_n']
    lat_A = ds_A['SC_GEO_LAT']
    lat_B = ds_B['SC_GEO_LAT']
    diff_rho = rho_A.clone()
    diff_rho_abs = rho_A.clone()
    diff_rho.value = (rho_B.value - rho_A.value) / np.sign(lat_B.value - lat_A.value)
    diff_rho_abs.value = np.abs(rho_B.value - rho_A.value)
    diff_rho.label = r'$\Delta\rho_n$'
    diff_rho_abs.label = r'$|\Delta\rho_n|$'
    ds_A['DIFF_rho_n'] = diff_rho
    ds_A['DIFF_rho_n_ABS'] = diff_rho_abs

    diff_rho_perc = rho_A.clone()
    diff_rho_perc.value = np.abs(rho_B.value - rho_A.value) / rho_A.value * 100
    diff_rho_perc.label = r'$|\Delta\rho_n|/\rho_n^A$*100'
    diff_rho_perc.unit = '%'
    diff_rho_perc.unit_label = None
    ds_A['PERC_DIFF_rho_n_ABS'] = diff_rho_perc
    
    diff_rho_perc = rho_A.clone()
    diff_rho_perc.value = (rho_B.value - rho_A.value) / np.sign(lat_B.value - lat_A.value) / rho_A.value * 100
    diff_rho_perc.label = r'$\Delta\rho_n/\rho_n^A$*100'
    diff_rho_perc.unit = '%'
    diff_rho_perc.unit_label = None
    ds_A['PERC_DIFF_rho_n'] = diff_rho_perc

def calc_d_between_A_and_B(ds_A, ds_B):
    ds_A = ds_A
    ds_B = ds_B

    glat_1 = ds_A['SC_GEO_LAT'].value
    glon_1 = ds_A['SC_GEO_LON'].value
    alt_1 = ds_A['SC_GEO_ALT'].value

    glat_2 = ds_B['SC_GEO_LAT'].value
    glon_2 = ds_B['SC_GEO_LON'].value
    alt_2 = ds_B['SC_GEO_ALT'].value

    r = 6371 + np.nanmean(alt_1.flatten())

    d = gd.calc_great_circle_distance(glat_1, glon_1, glat_2, glon_2, r=r)

    D = ds_A.add_variable(var_name='d_AB', value=d)
    D.label = 'D_AB'
    D.unit = 'km'
    D.visual.axis[1].unit = 'km'
    D.visual.axis[1].lim = [250, 350]
    D.visual.plot_config.style = '1noE'
    return D    
    
if __name__ == "__main__":
    dt_fr_1 = datetime.datetime(2016, 3, 14, 0)
    dt_to_1 = datetime.datetime(2016, 3, 21, 0)
    dt_fr_2 = datetime.datetime(2016, 3, 14, 12)
    dt_to_2 = datetime.datetime(2016, 3, 15, 10)
    overview_1(dt_fr_2, dt_to_2)
    # overview_with_maps()