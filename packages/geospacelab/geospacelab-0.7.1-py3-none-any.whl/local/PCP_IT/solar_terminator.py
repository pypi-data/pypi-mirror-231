import datetime
import numpy as np

import solar_position as sp

import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature as cfeature

def terminator(ut, height, az_list=None):
    anti_subsolar, arc_length, arc_angle = sp.terminator(ut, height)
    factor = np.pi / 180.
    if az_list is None:
        az_list = np.arange(2.5, 360, 5.) * factor
    else:
        az_list = az_list * factor
    phi_1 = (90. - anti_subsolar[1]) * factor
    theta_1 = anti_subsolar[0] * factor
    alpha = arc_angle * factor

    phi_2_p_list = []
    phi_2_n_list = []
    theta_2_p_list = []
    theta_2_n_list = []
    for ind, az in enumerate(az_list):

        cos_phi_2 = np.cos(phi_1) * np.cos(alpha) + \
                    np.sin(phi_1) * np.sin(alpha) * np.cos(az)

        sin_phi_2_p = np.sqrt(1 - cos_phi_2 ** 2)
        sin_phi_2_n = - sin_phi_2_p

        cos_lamda_p = (np.cos(alpha) - np.cos(phi_1) * cos_phi_2) / np.sin(phi_1) / sin_phi_2_p
        sin_lamda_p = np.sin(az) * np.sin(alpha) / sin_phi_2_p

        sin_lamda_n = np.sin(az) * np.sin(alpha) / sin_phi_2_n
        cos_lamda_n = (np.cos(alpha) - np.cos(phi_1) * cos_phi_2) / np.sin(phi_1) / sin_phi_2_n

        phi_2_p = np.sign(sin_phi_2_p) * (np.pi / 2 - np.arcsin(cos_phi_2))
        phi_2_n = np.sign(sin_phi_2_n) * (np.pi / 2 - np.arcsin(cos_phi_2))

        lamda_p = np.sign(sin_lamda_p) * (np.pi / 2 - np.arcsin(cos_lamda_p))
        lamda_n = np.sign(sin_lamda_n) * (np.pi / 2 - np.arcsin(cos_lamda_n))

        phi_2_p_list.append(phi_2_p / factor)
        theta_2_p_list.append(np.mod((theta_1 + lamda_p), 2 * np.pi) / factor)

        phi_2_n_list.append(phi_2_n / factor)
        theta_2_n_list.append(np.mod((theta_1 + lamda_n), 2 * np.pi) / factor)
        pass
    lats = 90. - np.array(phi_2_p_list)
    lons = np.array(theta_2_p_list)
    return lons, lats


def main():
    fig = plt.figure(figsize=[10, 5])
    ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.NorthPolarStereo())
    ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.NorthPolarStereo(),
                          sharex=ax1, sharey=ax1)
    fig.subplots_adjust(bottom=0.05, top=0.95,
                        left=0.04, right=0.95, wspace=0.02)

    # Limit the map to -60 degrees latitude and below.
    ax1.set_extent([-180, 180, 90, 0], ccrs.PlateCarree())

    ax1.add_feature(cfeature.LAND)
    ax1.add_feature(cfeature.OCEAN)
    ax1.add_feature(cfeature.COASTLINE)
    ax2.add_feature(cfeature.COASTLINE)
    ax1.gridlines()
    ax2.gridlines()


    ax2.add_feature(cfeature.LAND)
    ax2.add_feature(cfeature.OCEAN)

    ut = datetime.datetime(2015, 3, 23, 0)
    height = 300
    lons, lats = terminator(ut, height)
    plt.plot(lons, lats, transform=ccrs.Geodetic())

    ut = datetime.datetime(2015, 3, 23, 0)
    height = 10
    lons, lats = terminator(ut, height)
    plt.plot(lons, lats, transform=ccrs.Geodetic())

    # Compute a circle in axes coordinates, which we can use as a boundary
    # for the map. We can pan/zoom as much as we like - the boundary will be
    # permanently circular.
    theta = np.linspace(0, 2*np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)

    ax2.set_boundary(circle, transform=ax2.transAxes)

    plt.show()


if __name__ == "__main__":
    main()