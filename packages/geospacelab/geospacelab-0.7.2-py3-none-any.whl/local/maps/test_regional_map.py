import datetime

import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature as cfeature

import geospacelab.express.eiscat_dashboard as eiscat

import geospacelab.visualization.mpl.dashboards as dashboards
import geospacelab.visualization.mpl.geomap.geodashboards as geomap


def main():
    fig = plt.figure(figsize=[10, 5])

    lat0=90
    lon0=0

    ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.Orthographic(central_latitude=lat0, central_longitude=lon0))
    ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.Orthographic(central_latitude=lat0, central_longitude=lon0))
    fig.subplots_adjust(bottom=0.05, top=0.95,
                        left=0.04, right=0.95, wspace=0.02)

    # Limit the map to -60 degrees latitude and below.
    ax1.set_extent([-180, 180, 90, 60], ccrs.PlateCarree())

    ax1.add_feature(cfeature.LAND)
    ax1.add_feature(cfeature.OCEAN)

    ax1.gridlines()
    ax2.gridlines()

    ax2.add_feature(cfeature.LAND)
    ax2.add_feature(cfeature.OCEAN)

    # Compute a circle in axes coordinates, which we can use as a boundary
    # for the map. We can pan/zoom as much as we like - the boundary will be
    # permanently circular.
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.2
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)

    ax2.set_boundary(circle, transform=ax2.transAxes)

    plt.show()


def test_sector():
    import geospacelab.visualization.mpl.geomap.geopanels as geopanels
    import aacgmv2

    # db = geomap.GeoDashboard(dt_fr=dt_fr, dt_to=dt_to, figure_config={'figsize': (10, 10)})

    panel = geopanels.PolarSectorPanel(style='lon-fixed', lat_c=70, lon_c=15, boundary_zonal_lim=[-5, 35], boundary_meridional_lim=[64, 82])
    panel.overlay_coastlines(resolution='10m', alpha=0.5)
    panel.overlay_gridlines(lat_label_clock=6.4, lon_res=5, lat_res=5)

    aalats = np.linspace(45., 85., 17)
    aalons = np.linspace(0, 360., 2000)
    time_1 = datetime.datetime(2015, 2, 15, 20)
    for aalat in aalats:
        glats, glons, grs = aacgmv2.convert_latlon_arr(aalat, aalons, 250., time_1, method_code='A2G')
        panel().plot(glons, glats, transform=ccrs.Geodetic(), linewidth=1.5, color='m', linestyle=':')

    panel.overlay_sites(
        site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
        cs='GEO', marker='o', markersize=6, color='k', alpha=1, markerfacecolor='w', markeredgecolor='r', markeredgewidth=1.5)

    panel.overlay_sites(
        site_ids=['ESR'], coords={'lat': [78.15], 'lon': [16.02], 'height': 0.},
        cs='GEO', marker='o', markersize=6, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k', markeredgewidth=1.5)

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
        data_file_type=data_file_type, load_mode=load_mode, figure='off',
        figure_config={'figsize': (9, 6)})

    # select beams before assign the variables
    # dashboard.dataset.select_beams(field_aligned=False)
    dashboard.check_beams()
    ds_eiscat = dashboard.datasets[0]
    glats = ds_eiscat['GEO_LAT'].value[2, :]
    glons = ds_eiscat['GEO_LON'].value[2, :]
    alts = ds_eiscat['HEIGHT'].value[2, :]
    inds = np.where((alts > 200) & (alts < 500))[0]
    panel().plot(glons[:], glats[:], '-', linewidth=0.5, color='k', transform=ccrs.Geodetic())
    panel().plot(glons[inds], glats[inds], '-', linewidth=3, color='k', transform=ccrs.Geodetic())

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
        data_file_type=data_file_type, load_mode=load_mode, figure='off',
        figure_config={'figsize': (9, 8)})
    dashboard.check_beams()
    dashboard.status_mask(bad_status=[1, 2, 3])
    dashboard.residual_mask(residual_lim=10)
    ds_eiscat = dashboard.datasets[0]
    glats = ds_eiscat['GEO_LAT'].value[2, :]
    glons = ds_eiscat['GEO_LON'].value[2, :]
    alts = ds_eiscat['HEIGHT'].value[2, :]
    inds = np.where((alts > 200) & (alts < 500))[0]
    panel().plot(glons[:], glats[:], '-', linewidth=0.5, color='g', transform=ccrs.Geodetic())
    panel().plot(glons[inds], glats[inds], '-', linewidth=3, color='g', transform=ccrs.Geodetic())

    glats = ds_eiscat['GEO_LAT'].value[0, :]
    glons = ds_eiscat['GEO_LON'].value[0, :]
    alts = ds_eiscat['HEIGHT'].value[0, :]
    inds = np.where((alts > 200) & (alts < 500))[0]
    panel().plot(glons[:], glats[:], '-', linewidth=0.5, color='r', transform=ccrs.Geodetic())
    panel().plot(glons[inds], glats[inds], '-', linewidth=3, color='r', transform=ccrs.Geodetic())

    glats = ds_eiscat['GEO_LAT'].value[1, :]
    glons = ds_eiscat['GEO_LON'].value[1, :]
    alts = ds_eiscat['HEIGHT'].value[1, :]
    inds = np.where((alts > 200) & (alts < 500))[0]
    panel().plot(glons[:], glats[:], '-', linewidth=0.5, color='b', transform=ccrs.Geodetic())
    panel().plot(glons[inds], glats[inds], '-', linewidth=3, color='b', transform=ccrs.Geodetic())
    panel.figure.savefig('EISCAT_beam_map_20150215.png', format='png', dpi=300)
    plt.show()



if __name__ == '__main__':
    test_sector()