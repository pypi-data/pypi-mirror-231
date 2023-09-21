import datetime
import numpy as np
import pathlib

import geospacelab.express.eiscat_dashboard as eiscat
import geospacelab.toolbox.utilities.pydatetime as dttool

import geospacelab.visualization.mpl.colormaps as cm
default_colormap = cm.cmap_jet_modified()

fp_res = pathlib.Path('/home/lei/01-Work/01-Project/OY21-Daedalus/PCP/results')


def test_esr_32m():
    dt_fr = datetime.datetime.strptime('20150215' + '1700', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20150215' + '2300', '%Y%m%d%H%M')

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
    # dashboard.dataset.select_beams(field_aligned=False)
    dashboard.check_beams()
    dashboard.status_mask(bad_status=[1, 2, 3])
    dashboard.residual_mask()
    n_e = dashboard.assign_variable('n_e')
    n_e.visual.axis[1].data = '@d.AACGM_LAT.value'
    n_e.visual.axis[1].label = 'MLAT'
    n_e.visual.axis[1].unit = 'deg'
    n_e.visual.axis[1].lim = [69.9, 72.9]
    n_e.visual.axis[2].lim = [9e9, 5e11]
    T_i = dashboard.assign_variable('T_i')
    T_i.visual.axis[1].data = '@d.AACGM_LAT.value'
    T_i.visual.axis[1].label = 'MLAT'
    T_i.visual.axis[1].unit = 'deg'
    T_i.visual.axis[1].lim = [69.9, 72.9]
    T_i.visual.axis[2].lim = [700, 2000]
    T_e = dashboard.assign_variable('T_e')
    T_e.visual.axis[1].data = '@d.AACGM_LAT.value'
    T_e.visual.axis[1].label = 'MLAT'
    T_e.visual.axis[1].unit = 'deg'
    T_e.visual.axis[1].lim = [69.9, 72.9]
    T_e.visual.axis[2].lim = [800, 2900]
    v_i = dashboard.assign_variable('v_i_los')
    v_i.visual.axis[1].data = '@d.AACGM_LAT.value'
    v_i.visual.axis[1].label = 'MLAT'
    v_i.visual.axis[1].unit = 'deg'
    v_i.visual.axis[1].lim = [69.9, 72.9]

    az = dashboard.assign_variable('AZ')
    el = dashboard.assign_variable('EL')

    layout = [[n_e], [T_e], [v_i]]
    dashboard.set_layout(panel_layouts=layout, row_height_scales=[5, 5, 5], left=0.12, right=0.87)

    dashboard.draw()
    # dashboard.add_title()


    dts_tec = [
        datetime.datetime(2015, 2, 15, 17, 20),
        datetime.datetime(2015, 2, 15, 18, 5),
        datetime.datetime(2015, 2, 15, 18, 55),
        datetime.datetime(2015, 2, 15, 19, 40),
        datetime.datetime(2015, 2, 15, 20, 25),
        datetime.datetime(2015, 2, 15, 21, 10),
        datetime.datetime(2015, 2, 15, 22, 0),
    ]

    # add vertical lines:
    for ind, dt in enumerate(dts_tec):
        dashboard.add_vertical_line(dt, top_extend=0.02, label='T{:d}'.format(ind + 1), linewidth=1)

    # dashboard.add_panel_labels(color='k', bbox_config={'facecolor': 'yellow', 'alpha': 0.9, 'edgecolor': 'none'})
    # dashboard.show()
    dashboard.save_figure("ESR_32m_v5", file_dir=fp_res)
    return dashboard


def test_tro_uhf():
    dt_fr = datetime.datetime.strptime('20150215' + '1700', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20150215' + '2300', '%Y%m%d%H%M')

    site = 'UHF'
    antenna = 'UHF'
    modulation = ''
    load_mode = 'AUTO'
    data_file_type = 'eiscat-hdf5'

    dashboard = eiscat.EISCATDashboard(
        dt_fr, dt_to,
        site=site, antenna=antenna, modulation=modulation,
        data_file_type=data_file_type, load_mode=load_mode,
        figure_config={'figsize': (9, 8)})
    dashboard.check_beams()
    dashboard.status_mask(bad_status=[1, 2, 3])
    dashboard.residual_mask(residual_lim=10)
    n_e = dashboard.assign_variable('n_e')
    n_e.visual.axis[1].lim = [80, 500]
    n_e.visual.axis[2].lim = [9e9, 5e11]
    T_i = dashboard.assign_variable('T_i')
    T_i.visual.axis[1].lim = [80, 500]
    T_i.visual.axis[2].lim = [1000, 2000]
    T_e = dashboard.assign_variable('T_e')
    T_e.visual.axis[1].lim = [80, 500]
    T_e.visual.axis[2].lim = [800, 2900]
    v_i = dashboard.assign_variable('v_i_los')
    v_i.visual.axis[1].lim = [80, 500]

    az = dashboard.assign_variable('AZ')
    el = dashboard.assign_variable('EL')

    import scipy.io as sio

    import geospacelab.cs as cs
    cmap = cm.cmap_jet_modified()

    fp_asc = '/home/lei/extra/AFEISCAT3/Data/ASC/keo/keo_lat_20150215.mat'
    mdata = sio.loadmat(fp_asc)
    ds_asc = dashboard.add_dataset(kind='UserDefined', visual='on')
    v_dt = ds_asc.add_variable('DATETIME', ndim=1)
    v_dt.value = dttool.convert_matlabdn_to_datetime(mdata['tl'].flatten())[:, np.newaxis]
    v_glat = ds_asc.add_variable('GEO_LAT', ndim=1)
    v_glat.value = np.tile(mdata['latbins'].flatten()[np.newaxis, :], (v_dt.value.shape[0], 1))
    v_glat.value = np.around(v_glat.value*100)/100

    lat_ = v_glat.value.flatten()
    lon_ = np.ones_like(lat_) * 19.23
    alt_ = np.ones_like(lat_) * 110
    cs_geo = cs.GEOCSpherical(coords={'lat': lat_, 'lon': lon_, 'height': alt_}, ut=v_dt.value[0, 0])
    cs_new = cs_geo.to_AACGM(append_mlt=False)
    v_mlat = ds_asc.add_variable('AACGM_LAT', ndim=1)
    v_mlat.value = cs_new['lat'].reshape(v_glat.value.shape)

    v_keo = ds_asc.add_variable('KEO_LAT', ndim=2)
    keo = mdata['latkeo']
    gc = keo[:, :, 1]
    ii = np.where(((keo[:, :, 0] > 0.3 * 255) & (keo[:, :, 0] > 1.2 * keo[:, :, 1]))
                  | ((keo[:, :, 2] > 0.3 * 255) & (keo[:, :, 2] > 1.2 * keo[:, :, 1])))
    gc[ii] = np.nan
    v_keo.value = gc.T
    v_keo.label = 'TRO-DC-G'
    v_keo.unit = '#'
    v_keo.depends = {
        0: {'UT': 'DATETIME'},
        1: {'GEO_LAT': 'GEO_LAT', 'AACGM_LAT': 'AACGM_LAT'}
    }
    default_axis_dict_2d = {
        1: {
            'data': '@d.AACGM_LAT.value',
            'lim': [64, 70],
            'scale': 'linear',
            'label': 'MLAT',
            'unit': r'$^\circ$',
        },
        2: {
            'data': '@v.value',
            'label': '@v.label',
            'unit': '@v.unit_label',
            'scale': 'linear'
        }
    }

    default_plot_config = {
        'line': {
            'linestyle': '',
            'linewidth': 1.5,
            'marker': '.',
            'markersize': 3,
        },
        'pcolormesh': {
            'cmap': cmap,
        }
    }
    v_keo.visual.plot_config.config(**default_plot_config)
    v_keo.visual.plot_config.style = '2P'
    # set axis attrs
    v_keo.visual.axis[1].config(**default_axis_dict_2d[1])

    v_keo.visual.axis[2].config(**default_axis_dict_2d[2])
    v_keo.visual.axis[2].lim = [10, 160]
    v_keo.visual.axis[0].mask_gap = False

    fp_mat = '/home/lei/extra/AFEISCAT3/SpaDaV/results/PCP-u63_20150215_1700-2300.mat'
    mdata = sio.loadmat(fp_mat, simplify_cells=True)
    u63N_md = mdata['dataset'][5]
    u63E_md = mdata['dataset'][6]

    ds_fpi = dashboard.add_dataset(kind='UserDefined')
    var = ds_fpi.add_variable(var_name='DATETIME_u63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(u63N_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='u63_N', ndim=1)
    var.value = u63N_md['val'][:, np.newaxis]
    var.error = u63N_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$u$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_u63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'b'}
    var.visual.plot_config.style = '1E'
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var = ds_fpi.add_variable(var_name='DATETIME_u63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(u63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='u63_E', ndim=1)
    var.value = u63E_md['val'][:, np.newaxis]
    var.error = u63E_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'$u$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_u63E'}}
    var.visual.plot_config.line = {'linewidth': 3, 'elinewidth': 1, 'ecolor': 'r'}
    var.visual.plot_config.style = '1E'
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    vi63N_md = mdata['dataset'][60]
    vi63E_md = mdata['dataset'][59]
    var = ds_fpi.add_variable(var_name='DATETIME_vi63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(vi63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='vi63_N', ndim=1)
    var.value = vi63E_md['val'][:, np.newaxis]
    var.error = vi63E_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$v_i$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_vi63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var = ds_fpi.add_variable(var_name='DATETIME_vi63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(vi63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='vi63_E', ndim=1)
    var.value = vi63N_md['val'][:, np.newaxis]
    var.error = vi63N_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'$v_i$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_vi63N'}}
    var.visual.plot_config.line = {'linewidth': 2,  'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    vi63N = ds_fpi['vi63_N']
    vi63E = ds_fpi['vi63_E']

    layout = [[n_e], [T_e], [T_i], [vi63N, vi63E]]
    dashboard.set_layout(panel_layouts=layout, row_height_scales=[ 5, 5, 5, 5], left=0.12, right=0.87)
    dashboard.draw()
    dashboard.add_horizontal_line(66.6, panel_index=0)
    # dashboard.add_title()
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
    # add top bars
    dts_topbar = [
        datetime.datetime(2015, 2, 15, 17, 30),
        datetime.datetime(2015, 2, 15, 18, 25),
        datetime.datetime(2015, 2, 15, 19, 20),
        datetime.datetime(2015, 2, 15, 20, 45),
        datetime.datetime(2015, 2, 15, 21, 15),
        datetime.datetime(2015, 2, 15, 21, 30),
        datetime.datetime(2015, 2, 15, 21, 38),
        datetime.datetime(2015, 2, 15, 21, 51),
        datetime.datetime(2015, 2, 15, 22, 23),
        datetime.datetime(2015, 2, 15, 23, 00),
    ]
    c1 = 'r'
    c2 = 'orange'
    c3 = 'g'
    color_codes = [c1, c2, c1, c2, c1, c2, c3, c2, c3]
    for ind, c in enumerate(color_codes):
        dt_1 = dts_topbar[ind]
        dt_2 = dts_topbar[ind+1]
        dashboard.add_top_bar(dt_1, dt_2, top=0.02, color=c, alpha=0.85)
    
    # add vertical lines:
    for ind, dt in enumerate(dts_tec):
        dashboard.add_vertical_line(dt, top_extend=0.02, label='T{:d}'.format(ind + 1), linewidth=1)
    # dashboard.add_panel_labels(color='k', bbox_config={'facecolor': 'yellow', 'alpha': 0.9, 'edgecolor': 'none'})

    dt_fr_1 = datetime.datetime(2015, 2, 15, 17, 20)
    dt_fr_2 = datetime.datetime(2015, 2, 15, 17, 30)
    dashboard.add_shading(dt_fr_1, dt_fr_2, color='grey', alpha=0.3)

    dashboard.save_figure("TRO_UHF_v5", file_dir=fp_res)
    dashboard.show()
    return dashboard


def show_fpi():
    # Figure 3 in the manuscript
    import scipy.io as sio
    dt_fr = datetime.datetime.strptime('20150215' + '1700', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20150215' + '2300', '%Y%m%d%H%M')

    site = 'UHF'
    antenna = 'UHF'
    modulation = ''
    load_mode = 'AUTO'
    data_file_type = 'eiscat-hdf5'

    dashboard = eiscat.EISCATDashboard(
        dt_fr, dt_to,
        site=site, antenna=antenna, modulation=modulation,
        data_file_type=data_file_type, load_mode=load_mode,
        figure_config={'figsize': (10, 12)})
    dashboard.check_beams()
    dashboard.status_mask(bad_status=[1, 2, 3])
    dashboard.residual_mask(residual_lim=10)
    n_e = dashboard.assign_variable('n_e')
    n_e.visual.axis[1].lim = [195, 505]
    n_e.visual.axis[2].lim = [9e9, 5e11]

    fp_mat = '/home/lei/extra/AFEISCAT3/SpaDaV/results/PCP-u63_20150215_1700-2300.mat'
    mdata = sio.loadmat(fp_mat, simplify_cells=True)
    u63N_md = mdata['dataset'][5]
    u63E_md = mdata['dataset'][6]

    ds_fpi = dashboard.add_dataset(kind='UserDefined')
    var = ds_fpi.add_variable(var_name='DATETIME_u63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(u63N_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='u63_N', ndim=1)
    var.value = u63N_md['val'][:, np.newaxis]
    var.error = u63N_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$u$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_u63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var = ds_fpi.add_variable(var_name='DATETIME_u63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(u63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='u63_E', ndim=1)
    var.value = u63E_md['val'][:, np.newaxis]
    var.error = u63E_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'$u$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_u63E'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    vi63N_md = mdata['dataset'][60]
    vi63E_md = mdata['dataset'][59]
    var = ds_fpi.add_variable(var_name='DATETIME_vi63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(vi63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='vi63_N', ndim=1)
    var.value = vi63E_md['val'][:, np.newaxis]
    var.error = vi63E_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$v_i$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_vi63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var = ds_fpi.add_variable(var_name='DATETIME_vi63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(vi63E_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='vi63_E', ndim=1)
    var.value = vi63N_md['val'][:, np.newaxis]
    var.error = vi63N_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'$v_i$'
    var.unit = 'm/s'
    var.depends = {0: {'UT': 'DATETIME_vi63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    # for tau_ni
    var_md = mdata['dataset'][18]
    var = ds_fpi.add_variable(var_name='DATETIME_tau_ni', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='ALT_tau_ni', ndim=1)
    var.value = np.tile(var_md['alt'][np.newaxis, :], ds_fpi['DATETIME_tau_ni'].value.shape)
    var = ds_fpi.add_variable(var_name='tau_ni', ndim=2)
    var.value = var_md['val'].T
    var.label = r'$\tau_{ni}$'
    var.unit = 'h'
    var.depends = {0: {'UT': 'DATETIME_tau_ni'}, 1: {'GEO_ALT': 'ALT_tau_ni'}}
    var.visual.plot_config.style = '2P'
    var.visual.plot_config.pcolormesh = {'cmap': default_colormap.reversed()}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].data = '@vd.1.GEO_ALT'
    var.visual.axis[1].lim = [195, 505]
    var.visual.axis[1].label = 'h'
    var.visual.axis[1].unit = 'km'
    var.visual.axis[2].data = '@v.value'
    var.visual.axis[2].lim = [1, 15]
    var.visual.axis[2].scale = 'log'
    var.visual.axis[2].label = '@v.label'
    var.visual.axis[2].unit = 'hour'
    var.visual.axis[2].data_scale = 1

    var_md = mdata['dataset'][30]
    var = ds_fpi.add_variable(var_name='DATETIME_ai63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='ai63_N', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$a_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63N'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var_md = mdata['dataset'][31]
    var = ds_fpi.add_variable(var_name='DATETIME_ai63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi.add_variable(var_name='ai63_E', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'a$_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63E'}}
    var.visual.plot_config.line = {'linewidth': 2, 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.plot_config.style = '1E'
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var_2d = dashboard.host_dataset['n_e']
    var = dashboard.host_dataset.add_variable(var_name='n_e_260', ndim=1)
    var.value = var_2d.value[:, 25] # 264km
    var.label = r'$n_e$ 260km'
    var.group = ''
    var.unit = r'm$^{-3}$'
    var.depends = {0: {'UT': 'DATETIME'}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'alpha': 1, 'linewidth': 2}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    var.visual.axis[1].ticks = [0, 1e11, 2e11, 3e11, 4e11]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [2e10, 4e11]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = 'EISCAT'

    var_2d = ds_fpi['tau_ni']
    var = ds_fpi.add_variable(var_name='tau_ni_260', ndim=1)
    var.value = var_2d.value[:, 189]
    var.label = r'$\tau_{ni}$ 260km'
    var.group = ''
    var.unit = r'hour'
    var.depends = {0: {'UT': 'DATETIME_tau_ni'}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'linewidth': 2}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    # var.visual.axis[1].ticks = [0, 3, 6, 9, 12]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [0.9, 18]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = 'EISCAT'

    ########################################################
    fp_mat = '/home/lei/extra/AFEISCAT3/SpaDaV/results/PCP-u63_iri_20150215_1700-2300.mat'
    mdata = sio.loadmat(fp_mat, simplify_cells=True)
    ds_fpi_2 = dashboard.add_dataset(kind='UserDefined')

    var_md = mdata['dataset'][30]
    var = ds_fpi_2.add_variable(var_name='DATETIME_ai63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_2.add_variable(var_name='ai63_N', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$a_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63N'}}
    var.visual.plot_config.style = '1E'
    var.visual.plot_config.line = {'linewidth': 1, 'linestyle': '--'}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var_md = mdata['dataset'][31]
    var = ds_fpi_2.add_variable(var_name='DATETIME_ai63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_2.add_variable(var_name='ai63_E', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'a$_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63E'}}
    var.visual.plot_config.style = '1E'
    var.visual.plot_config.line = {'linewidth': 1, 'linestyle': '--'}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    # for tau_ni
    var_md = mdata['dataset'][18]
    var = ds_fpi_2.add_variable(var_name='DATETIME_tau_ni', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_2.add_variable(var_name='ALT_tau_ni', ndim=1)
    var.value = np.tile(var_md['alt'][np.newaxis, :], ds_fpi['DATETIME_tau_ni'].value.shape)
    var = ds_fpi_2.add_variable(var_name='tau_ni', ndim=2)
    var.value = var_md['val'].T
    var.label = r'$\tau_{ni}$'
    var.unit = 'h'
    var.depends = {0: {'UT': 'DATETIME_tau_ni'}, 1: {'GEO_ALT': 'ALT_tau_ni'}}
    var.visual.plot_config.style = '2P'
    var.visual.plot_config.pcolormesh = {'cmap': default_colormap.reversed()}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].data = '@vd.1.GEO_ALT'
    var.visual.axis[1].lim = [195, 505]
    var.visual.axis[1].label = 'h'
    var.visual.axis[1].unit = 'km'
    var.visual.axis[2].data = '@v.value'
    var.visual.axis[2].lim = [1, 15]
    var.visual.axis[2].scale = 'log'
    var.visual.axis[2].label = '@v.label'
    var.visual.axis[2].data_scale = 1

    # for ne_c
    var_md = mdata['dataset'][44]
    var = ds_fpi_2.add_variable(var_name='DATETIME_ne_c', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_2.add_variable(var_name='ALT_ne_c', ndim=1)
    var.value = np.tile(var_md['alt'][np.newaxis, :], ds_fpi_2['DATETIME_ne_c'].value.shape)
    var = ds_fpi_2.add_variable(var_name='ne_c', ndim=2)
    var.value = var_md['val'].T
    var.label = r'$n_{e}$'
    var.unit = 'h'
    var.depends = {0: {'UT': 'DATETIME_ne_c'}, 1: {'GEO_ALT': 'ALT_ne_c'}}
    var.visual.plot_config.style = '2P'
    var.visual.plot_config.pcolormesh = {'cmap': default_colormap.reversed()}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].data = '@vd.1.GEO_ALT'
    var.visual.axis[1].lim = [195, 505]
    var.visual.axis[1].label = 'h'
    var.visual.axis[1].unit = 'km'
    var.visual.axis[2].data = '@v.value'
    var.visual.axis[2].lim = [1, 15]
    var.visual.axis[2].scale = 'log'
    var.visual.axis[2].label = '@v.label'
    var.visual.axis[2].data_scale = 1

    var_2d = ds_fpi_2['ne_c']
    var = ds_fpi_2.add_variable(var_name='n_e_260', ndim=1)
    var.value = var_2d.value[:, 189] # 264km
    var.label = r'$n_e$ 260km'
    var.group = ''
    var.unit = r'm$^{-3}$'
    var.depends = {0: {'UT': 'DATETIME_ne_c'}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'linewidth': 1, 'linestyle': '--'}
    # var.visual.plot_config.line = {'color': 'orange', 'alpha': 0.7, 'linewidth': 1}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    var.visual.axis[1].ticks = [0, 1e11, 2e11, 3e11, 4e11]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [2e10, 4e11]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'

    var_2d = ds_fpi_2['tau_ni']
    var = ds_fpi_2.add_variable(var_name='tau_ni_260', ndim=1)
    var.value = var_2d.value[:, 189]
    var.label = r'$\tau_{ni}$ 260km'
    var.group = ''
    var.unit = r'h'
    var.depends = {0: {'UT': 'DATETIME_tau_ni'}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'linewidth': 1, 'linestyle': '--'}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    # var.visual.axis[1].ticks = [0, 3, 6, 9, 12]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [0.9, 18]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = 'IRI'

    ###################################################################################
    fp_mat = '/home/lei/extra/AFEISCAT3/SpaDaV/results/PCP-u63_AT1730_20150215_1700-2300.mat'
    mdata = sio.loadmat(fp_mat, simplify_cells=True)
    ds_fpi_3 = dashboard.add_dataset(kind='UserDefined')

    var_md = mdata['dataset'][30]
    var = ds_fpi_3.add_variable(var_name='DATETIME_ai63N', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_3.add_variable(var_name='ai63_N', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Northward'
    var.group = r'$a_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63N'}}
    var.visual.plot_config.style = '1E'
    var.visual.plot_config.line = {'linewidth': 1, 'linestyle': (0, (1, 0.5))}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    var_md = mdata['dataset'][31]
    var = ds_fpi_3.add_variable(var_name='DATETIME_ai63E', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_3.add_variable(var_name='ai63_E', ndim=1)
    var.value = var_md['val'][:, np.newaxis]
    var.error = var_md['err'][:, np.newaxis]
    var.label = 'Eastward'
    var.group = r'a$_{IDRAG}$'
    var.unit = r'm/s$^2$'
    var.depends = {0: {'UT': 'DATETIME_ai63E'}}
    var.visual.plot_config.style = '1E'
    var.visual.plot_config.line = {'linewidth': 2, 'linestyle': (0, (1, 0.5)), 'elinewidth': 1, 'ecolor': 'k', 'barsabove': True}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].label = '@v.group'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = '@v.label'

    # for tau_ni
    var_md = mdata['dataset'][18]
    var = ds_fpi_3.add_variable(var_name='DATETIME_tau_ni', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_3.add_variable(var_name='ALT_tau_ni', ndim=1)
    var.value = np.tile(var_md['alt'][np.newaxis, :], ds_fpi['DATETIME_tau_ni'].value.shape)
    var = ds_fpi_3.add_variable(var_name='tau_ni', ndim=2)
    var.value = var_md['val'].T
    var.label = r'$\tau_{ni}$'
    var.unit = 'h'
    var.depends = {0: {'UT': 'DATETIME_tau_ni'}, 1: {'GEO_ALT': 'ALT_tau_ni'}}
    var.visual.plot_config.style = '2P'
    var.visual.plot_config.pcolormesh = {'cmap': default_colormap.reversed()}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].data = '@vd.1.GEO_ALT'
    var.visual.axis[1].lim = [195, 505]
    var.visual.axis[1].label = 'h'
    var.visual.axis[1].unit = 'km'
    var.visual.axis[2].data = '@v.value'
    var.visual.axis[2].lim = [1, 15]
    var.visual.axis[2].scale = 'log'
    var.visual.axis[2].label = '@v.label'
    var.visual.axis[2].data_scale = 1

    # for ne_c
    var_md = mdata['dataset'][44]
    var = ds_fpi_3.add_variable(var_name='DATETIME_ne_c', ndim=1)
    var.value = dttool.convert_matlabdn_to_datetime(var_md['tl'])[:, np.newaxis]
    var = ds_fpi_3.add_variable(var_name='ALT_ne_c', ndim=1)
    var.value = np.tile(var_md['alt'][np.newaxis, :], ds_fpi_3['DATETIME_ne_c'].value.shape)
    var = ds_fpi_3.add_variable(var_name='ne_c', ndim=2)
    var.value = var_md['val'].T
    var.label = r'$n_{e}$'
    var.unit = 'h'
    var.depends = {0: {'UT': 'DATETIME_ne_c'}, 1: {'GEO_ALT': 'ALT_ne_c'}}
    var.visual.plot_config.style = '2P'
    var.visual.plot_config.pcolormesh = {'cmap': default_colormap.reversed()}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].data = '@vd.1.GEO_ALT'
    var.visual.axis[1].lim = [195, 505]
    var.visual.axis[1].label = 'h'
    var.visual.axis[1].unit = 'km'
    var.visual.axis[2].data = '@v.value'
    var.visual.axis[2].lim = [1, 15]
    var.visual.axis[2].scale = 'log'
    var.visual.axis[2].label = '@v.label'
    var.visual.axis[2].data_scale = 1

    var_2d = ds_fpi_3['ne_c']
    var = ds_fpi_3.add_variable(var_name='n_e_260', ndim=1)
    var.value = var_2d.value[:, 189]  # 264km
    var.label = r'$n_e$ 260km'
    var.group = ''
    var.unit = r'm$^{-3}$'
    var.depends = {0: {'UT': ds_fpi_3['DATETIME_ne_c'].value[:]}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'linewidth': 2, 'linestyle': (0, (1, 0.5)), 'marker': None}
    # var.visual.plot_config.line = {'color': 'orange', 'alpha': 0.7, 'linewidth': 1}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    var.visual.axis[1].ticks = [0, 1e11, 2e11, 3e11, 4e11]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [2e10, 4e11]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = 'Background'

    var_2d = ds_fpi_3['tau_ni']
    var = ds_fpi_3.add_variable(var_name='tau_ni_260', ndim=1)
    var.value = var_2d.value[:, 189]
    var.label = r'$\tau_{ni}$ 260km'
    var.group = ''
    var.unit = r'hour'
    var.depends = {0: {'UT': ds_fpi_3['DATETIME_tau_ni'].value[:]}}
    var.visual.plot_config.style = '1noE'
    var.visual.plot_config.line = {'linewidth': 2, 'linestyle': (0, (1, 0.5)), 'marker': None}
    var.visual.axis[0].data_res = 300
    var.visual.axis[1].scale = 'log'
    # var.visual.axis[1].ticks = [0, 3, 6, 9, 12]
    # var.visual.axis[1].tick_labels = ['0', '1e11', '2e11', '3e11', '4e11']
    var.visual.axis[1].lim = [0.9, 18]
    var.visual.axis[1].label = '@v.label'
    var.visual.axis[1].unit = '@v.unit'
    var.visual.axis[2].label = 'Background'

    uN = ds_fpi['u63_N']
    uE = ds_fpi['u63_E']
    uN.visual.axis[1].ticks = [-400, -300, -200, -100, 0, 100, 200]
    vi63N = ds_fpi['vi63_N']
    vi63E = ds_fpi['vi63_E']
    tau_ni = ds_fpi['tau_ni']
    ai63N = ds_fpi['ai63_N']
    ai63E = ds_fpi['ai63_E']
    
    ne260 = dashboard.host_dataset['n_e_260']
    tau260 = ds_fpi['tau_ni_260']

    ai63N_2 = ds_fpi_2['ai63_N']
    ai63E_2 = ds_fpi_2['ai63_E']
    ne260_2 = ds_fpi_2['n_e_260']
    tau260_2 = ds_fpi_2['tau_ni_260']

    ai63N_3 = ds_fpi_3['ai63_N']
    ai63E_3 = ds_fpi_3['ai63_E']
    ne260_3 = ds_fpi_3['n_e_260']
    tau260_3 = ds_fpi_3['tau_ni_260']
    # layout = [[n_e, [ne260]], [tau_ni, [tau260]], [vi63N, vi63E], [uN, uE], [ai63N, ai63E]]

    ai63E.visual.axis[1].label = 'IDRAG_E'
    ai63E.visual.axis[1].lim = [-0.14, 0.05]
    ai63E.visual.axis[2].label = 'EISCAT'
    ai63E_2.visual.axis[2].label = 'IRI'
    ai63E_3.visual.axis[1].label = r'$a_{IDRAG\_E}$'
    ai63E_3.visual.axis[1].ticks = [-0.125, -0.1, -0.075, -0.05, -0.025, 0, 0.025]
    ai63E_3.visual.axis[2].label = 'Background'

    ai63N.visual.axis[1].label = 'IDRAG_N'
    ai63N.visual.axis[1].lim = [-0.14, 0.05]
    ai63N.visual.axis[2].label = 'EISCAT'
    ai63N_2.visual.axis[2].label = 'IRI'
    ai63N_3.visual.axis[2].label = 'Background'

    r_ai63E = ai63E.clone()
    r_ai63E.value = (ai63E.value - ai63E_3.value)/ai63E_3.value
    r_ai63E.error = np.abs(r_ai63E.value) * np.sqrt((ai63E.error/ai63E.value)**2 + (ai63E_3.error/ai63E_3.value)**2)
    r_ai63E.visual.plot_config.style = '1E'
    r_ai63E.visual.plot_config.line = {'color': 'k', 'linewidth': 3, 'elinewidth': 1.5, 'ecolor': 'k', 'barsabove': True}
    r_ai63E.visual.axis[1].label = r'$\Delta a_{IDRAG\_E}$'
    r_ai63E.visual.axis[1].unit = '%'
    r_ai63E.visual.axis[1].lim = [-50, 150]
    r_ai63E.visual.axis[1].data_scale = 100
    
    n_e.visual.axis[1].label_pos = [-0.12, 0.5]
    tau_ni.visual.axis[1].label_pos = [-0.12, 0.5]
    ne260_3.visual.axis[1].label_pos = [-0.12, 0.5]
    tau260_3.visual.axis[1].label_pos = [-0.12, 0.5]
    vi63N.visual.axis[1].label_pos = [-0.12, 0.5]
    uN.visual.axis[1].label_pos = [-0.12, 0.5]
    ai63E_3.visual.axis[1].label_pos = [-0.12, 0.5]
    r_ai63E.visual.axis[1].label_pos = [-0.12, 0.5]
    layout = [[n_e], [tau_ni], [ne260_3, ne260], [tau260_3, tau260], [vi63N, vi63E], [uN, uE], [ai63E_3, ai63E], [r_ai63E]]
    layout = [[uN, uE], [vi63N, vi63E], [n_e], [tau_ni], [ne260_3, ne260], [tau260_3, tau260], [ai63E_3, ai63E],
              [r_ai63E]]
    # layout = [[uN, uE], [n_e], [tau_ni], [vi63N, vi63E], [ai63N, ai63E]]
    dashboard.set_layout(panel_layouts=layout, row_height_scales=[8, 8, 5, 5, 5, 5, 5, 5], left=0.15, right=0.85, top=0.95, bottom=0.08)

    dashboard.draw()
    
    # add top bars
    dts_topbar = [
        datetime.datetime(2015, 2, 15, 17, 30),
        datetime.datetime(2015, 2, 15, 18, 25),
        datetime.datetime(2015, 2, 15, 19, 20),
        datetime.datetime(2015, 2, 15, 20, 45),
        datetime.datetime(2015, 2, 15, 21, 15),
        datetime.datetime(2015, 2, 15, 21, 30),
        datetime.datetime(2015, 2, 15, 21, 38),
        datetime.datetime(2015, 2, 15, 21, 51),
        datetime.datetime(2015, 2, 15, 22, 23),
        datetime.datetime(2015, 2, 15, 23, 00),
    ]
    c1 = 'r'
    c2 = 'orange'
    c3 = 'g'
    color_codes = [c1, c2, c1, c2, c1, c2, c3, c2, c3]
    for ind, c in enumerate(color_codes):
        dt_1 = dts_topbar[ind]
        dt_2 = dts_topbar[ind+1]
        # dashboard.add_top_bar(dt_1, dt_2, top=0.01, color=c, alpha=0.85)
        dashboard.add_top_bar(dt_1, dt_2, bottom=-1, top=0.01-1, color=c, alpha=0.85)

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
        if ind % 2 == 0:
            dashboard.add_vertical_line(dt, top_extend=0.01, label='T{:d}'.format(ind + 1), linewidth=1)
    dashboard.add_horizontal_line(260, panel_index=2, linewidth=2, linestyle='--')
    dashboard.add_horizontal_line(260, panel_index=3, linewidth=2, linestyle='--')
    dt_fr_1 = datetime.datetime(2015, 2, 15, 17, 20)
    dt_fr_2 = datetime.datetime(2015, 2, 15, 17, 30)
    dashboard.add_shading(dt_fr_1, dt_fr_2, color='grey', alpha=0.3)

    dashboard.add_panel_labels(position=(0.01, 0.87))
    dashboard.save_figure("fpi_u_v6", file_dir=fp_res)
    dashboard.show()


def test_tro_vhf():
    dt_fr = datetime.datetime.strptime('20150214' + '1700', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20150214' + '2300', '%Y%m%d%H%M')

    site = 'VHF'
    antenna = 'VHF'
    modulation = ''
    load_mode = 'AUTO'
    data_file_type = 'eiscat-hdf5'

    dashboard = eiscat.EISCATDashboard(
        dt_fr, dt_to,
        site=site, antenna=antenna, modulation=modulation,
        data_file_type=data_file_type, load_mode=load_mode)

    n_e = dashboard.assign_variable('n_e')
    T_i = dashboard.assign_variable('T_i')
    T_e = dashboard.assign_variable('T_e')
    v_i = dashboard.assign_variable('v_i_los')

    az = dashboard.assign_variable('AZ')
    el = dashboard.assign_variable('EL')

    layout = [[n_e], [T_e], [T_i], [v_i]]
    dashboard.set_layout(panel_layouts=layout, row_height_scales=[5, 5, 5, 5])
    dashboard.draw()


    dashboard.add_title()
    dashboard.add_panel_labels()
    # dashboard.show()
    dashboard.save_figure("TRO_vHF")
    return dashboard


def uhf_profiles():
    import matplotlib.pyplot as plt
    
    dt_fr = datetime.datetime.strptime('20150215' + '1700', '%Y%m%d%H%M')
    dt_to = datetime.datetime.strptime('20150215' + '2300', '%Y%m%d%H%M')

    site = 'UHF'
    antenna = 'UHF'
    modulation = ''
    load_mode = 'AUTO'
    data_file_type = 'eiscat-hdf5'

    dashboard = eiscat.EISCATDashboard(
        dt_fr, dt_to,
        site=site, antenna=antenna, modulation=modulation,
        data_file_type=data_file_type, load_mode=load_mode,
        figure_config={'figsize': (9, 8)})
    dashboard.check_beams()
    dashboard.status_mask(bad_status=[1, 2, 3])
    dashboard.residual_mask(residual_lim=10)
    dashboard.select_beams(field_aligned=True)
    n_e = dashboard.assign_variable('n_e')
    n_e.visual.axis[1].lim = [80, 500]
    n_e.visual.axis[2].lim = [9e9, 5e11]
    T_i = dashboard.assign_variable('T_i')
    T_i.visual.axis[1].lim = [80, 500]
    T_i.visual.axis[2].lim = [1000, 2000]
    T_e = dashboard.assign_variable('T_e')
    T_e.visual.axis[1].lim = [80, 500]
    T_e.visual.axis[2].lim = [800, 2900]
    v_i = dashboard.assign_variable('v_i_los')
    v_i.visual.axis[1].lim = [80, 500]

    az = dashboard.assign_variable('AZ')
    el = dashboard.assign_variable('EL')
    alt = dashboard.assign_variable('HEIGHT').value[0, :]

    dts = dashboard.assign_variable('DATETIME').value.flatten()

    dts_topbar = [
        datetime.datetime(2015, 2, 15, 17, 30),
        datetime.datetime(2015, 2, 15, 18, 25),
        datetime.datetime(2015, 2, 15, 19, 20),
        datetime.datetime(2015, 2, 15, 20, 45),
        datetime.datetime(2015, 2, 15, 21, 15),
        datetime.datetime(2015, 2, 15, 21, 30),
        datetime.datetime(2015, 2, 15, 21, 38),
        datetime.datetime(2015, 2, 15, 21, 51),
        datetime.datetime(2015, 2, 15, 22, 23),
        datetime.datetime(2015, 2, 15, 23, 00),
    ]
    c1 = 'r'
    c2 = 'orange'
    c3 = 'g'
    color_codes = [c1, c2, c1, c2, c1, c2, c3, c2, c3]

    n = n_e.value.shape[1]
    ne_pcp = np.empty((0, n))
    ne_ap = np.empty((0, n))
    ne_mix = np.empty((0, n))
    te_pcp = np.empty((0, n))
    te_ap = np.empty((0, n))
    te_mix = np.empty((0, n))
    ti_pcp = np.empty((0, n))
    ti_ap = np.empty((0, n))
    ti_mix = np.empty((0, n))
    for ind, dt in enumerate(dts_topbar):
        if ind == len(dts_topbar) - 1:
            continue
        ind_t = np.where((dts > dt) & (dts < dts_topbar[ind+1]))[0]
        if color_codes[ind] == c1:
            ne_pcp = np.vstack((ne_pcp, n_e.value[ind_t, :]))
            te_pcp = np.vstack((te_pcp, T_e.value[ind_t, :]))
            ti_pcp = np.vstack((ti_pcp, T_i.value[ind_t, :]))
        elif color_codes[ind] == c2:
            ne_mix = np.vstack((ne_mix, n_e.value[ind_t, :]))
            te_mix = np.vstack((te_mix, T_e.value[ind_t, :]))
            ti_mix = np.vstack((ti_mix, T_i.value[ind_t, :]))
        else:
            ne_ap = np.vstack((ne_ap, n_e.value[ind_t, :]))
            te_ap = np.vstack((te_ap, T_e.value[ind_t, :]))
            ti_ap = np.vstack((ti_ap, T_i.value[ind_t, :]))

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
    alts = np.tile(alt, (ne_pcp.shape[0], 1))
    var = ne_pcp
    c = c1
    ax1.errorbar(np.nanmean(var, axis=0), alt+1, xerr=np.nanstd(var, axis=0), color=c, )
    var = ne_ap
    c = c3
    ax1.errorbar(np.nanmean(var, axis=0), alt-1, xerr=np.nanstd(var, axis=0), color=c, )
    var = ne_mix
    c = c2
    ax1.errorbar(np.nanmean(var, axis=0), alt, xerr=np.nanstd(var, axis=0), color=c, )

    plt.ylim([98, 480])
    plt.xscale = 'log'
    plt.xlim(0, 2.5e11)
    ax1.set_ylabel('h (km)')


    var = te_pcp
    c = c1
    ax2.errorbar(np.nanmean(var, axis=0), alt+1, xerr=np.nanstd(var, axis=0), color=c, )
    var = te_ap
    c = c3
    ax2.errorbar(np.nanmean(var, axis=0), alt, xerr=np.nanstd(var, axis=0), color=c, )
    var = te_mix
    c = c2
    ax2.errorbar(np.nanmean(var, axis=0), alt-1, xerr=np.nanstd(var, axis=0), color=c, )

    ax2.xscale = 'linear'
    ax2.set_xlim(0, 3000)

    var = ti_pcp
    c = c1
    ax3.errorbar(np.nanmean(var, axis=0), alt+1, xerr=np.nanstd(var, axis=0), color=c, )
    var = ti_ap
    c = c3
    ax3.errorbar(np.nanmean(var, axis=0), alt, xerr=np.nanstd(var, axis=0), color=c, )
    var = ti_mix
    c = c2
    ax3.errorbar(np.nanmean(var, axis=0), alt-1, xerr=np.nanstd(var, axis=0), color=c, )

    ax3.xscale = 'linear'
    ax3.set_xlim(0, 2000)

    plt.show()
    pass

if __name__ == "__main__":
    # test_esr_32m()
    # test_tro_uhf()
    uhf_profiles()
    # show_fpi()
    # test_tro_vhf()
