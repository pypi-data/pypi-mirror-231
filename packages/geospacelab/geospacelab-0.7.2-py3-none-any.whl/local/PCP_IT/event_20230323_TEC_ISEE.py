import datetime
import numpy as np
import pathlib
import pickle

from geospacelab.datahub import DataHub
from geospacelab.visualization.mpl import create_figure
from geospacelab.visualization.mpl.dashboards import TSDashboard
from geospacelab.visualization.mpl.geomap.geodashboards import GeoDashboard
import geospacelab.toolbox.utilities.pydatetime as dttool
import solar_terminator as st

file_dir_root = pathlib.Path(__file__).parent.resolve()


def show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=None,):
    fig = create_figure(figsize=(10, 6))

    db_tec = fig.add_dashboard(dashboard_class=GeoDashboard, dt_fr=dt_fr_tec, dt_to=dt_to_tec)
    ds_tec = db_tec.dock(datasource_contents=['isee', 'gnss', 'tecmap'])
    tec = db_tec.assign_variable('TEC_MAP', dataset_index=0)
    dts = db_tec.assign_variable('DATETIME', dataset_index=0).value.flatten()
    glat = db_tec.assign_variable('GEO_LAT', dataset_index=0).value
    glon = db_tec.assign_variable('GEO_LON', dataset_index=0).value

    db_tec.set_layout(2, 4, left=0.05, right=0.9, bottom=0.05, top=0.95, wspace=0.19, )
    ind = 0

    dts_tec = time_list

    for row in range(2):
        for col in range(4):
            time_c = dts_tec[ind]
            # Create a TEC panel in row and col
            panel = db_tec.add_polar_map(
                row_ind=row, col_ind=col,
                style='mlt-fixed', cs='AACGM', mlt_c=0.,
                pole='N', ut=time_c, boundary_lat=30,
            )
            # Overlay the coastlines
            panel.overlay_coastlines()
            # Overlay the gridlines
            panel.overlay_gridlines(lat_label_clock=1.7, lon_label_separator=5, lat_label_config={'color': 'k', 'fontsize': 6, 'alpha': 0.9})

            # Extract the grace data
            ind_t_c = np.where(dts == time_c)[0]
            if not list(ind_t_c):
                return
            tec_ = tec.value[ind_t_c[0], :, :]
            pcolormesh_config = tec.visual.plot_config.pcolormesh
            # Set the colormap scale.
            pcolormesh_config.update(c_lim=[2, 16])
            # import geospacelab.visualization.mpl.colormaps as cm
            # pcolormesh_config.update(cmap='jet') # colomap code can be selected from the matplotlib colormap code list
            # Overlay the TEC map
            ipc = panel.overlay_pcolormesh(tec_, coords={'lat': glat, 'lon': glon, 'height': 250.}, cs='GEO',
                                             **pcolormesh_config, regridding=True, grid_res=.5)
            # Add the colorbar on the right side
            if ind == len(dts_tec) - 1:
                panel.add_colorbar(ipc, c_label="TECU", c_scale='linear', left=1.15, bottom=0.35, width=0.07, height=1.5)

            # Overlay the solar terminator at 110 and 300 km
            az_list = np.arange(-87.5, 87.5, 1.)
            alt = 110.
            lons, lats = st.terminator(time_c, alt, az_list=az_list)
            coords = {'lat': lats, 'lon': lons, 'height': alt}
            panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1.5, linestyle='-', color='purple')
            alt = 300.
            lons, lats = st.terminator(time_c, alt, az_list=az_list)
            coords = {'lat': lats, 'lon': lons, 'height': alt}
            panel.overlay_line(ut=time_c, coords=coords, cs='GEO', linewidth=1.5, linestyle='-', color='k')

            # Overlay the TRO site in an open circle
            panel.overlay_sites(
                site_ids=['TRO'], coords={'lat': [69.58], 'lon': [19.23], 'height': 0.},
                cs='GEO', marker='o', markersize=4, color='k', alpha=1, markerfacecolor='w', markeredgecolor='k')

            panel.add_label(x=0.0, y=0.95, label="({:c})".format(97+ind), fontsize=12)
            panel.add_title(0.5, 1.1, title="{:s}".format(time_c.strftime("%y-%m-%d/%H:%M:%S")), fontsize=12)
            
            ind += 1
    # Save the figure and show
    db_tec.save_figure(file_name=file_name, file_dir=file_dir_root)
    db_tec.show()
    pass


def figure_4():
    dt_fr_tec = datetime.datetime(2023, 3, 23, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 24, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 23, 20, ),
        datetime.datetime(2023, 3, 23, 21, ),
        datetime.datetime(2023, 3, 23, 22, ),
        datetime.datetime(2023, 3, 23, 23, ),
        datetime.datetime(2023, 3, 24, 0, ),
        datetime.datetime(2023, 3, 24, 1, ),
        datetime.datetime(2023, 3, 24, 2, ),
        datetime.datetime(2023, 3, 24, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_4.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)
    

def figure_S1():
    dt_fr_tec = datetime.datetime(2023, 3, 24, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 25, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 24, 20, ),
        datetime.datetime(2023, 3, 24, 21, ),
        datetime.datetime(2023, 3, 24, 22, ),
        datetime.datetime(2023, 3, 24, 23, ),
        datetime.datetime(2023, 3, 25, 0, ),
        datetime.datetime(2023, 3, 25, 1, ),
        datetime.datetime(2023, 3, 25, 2, ),
        datetime.datetime(2023, 3, 25, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_S1.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)
    

def figure_S2():
    dt_fr_tec = datetime.datetime(2023, 3, 25, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 26, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 25, 20, ),
        datetime.datetime(2023, 3, 25, 21, ),
        datetime.datetime(2023, 3, 25, 22, ),
        datetime.datetime(2023, 3, 25, 23, ),
        datetime.datetime(2023, 3, 26, 0, ),
        datetime.datetime(2023, 3, 26, 1, ),
        datetime.datetime(2023, 3, 26, 2, ),
        datetime.datetime(2023, 3, 26, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_S2.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)
    
    
def figure_S3():
    dt_fr_tec = datetime.datetime(2023, 3, 26, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 27, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 26, 20, ),
        datetime.datetime(2023, 3, 26, 21, ),
        datetime.datetime(2023, 3, 26, 22, ),
        datetime.datetime(2023, 3, 26, 23, ),
        datetime.datetime(2023, 3, 27, 0, ),
        datetime.datetime(2023, 3, 27, 1, ),
        datetime.datetime(2023, 3, 27, 2, ),
        datetime.datetime(2023, 3, 27, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_S3.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)
    
    
def figure_S4():
    dt_fr_tec = datetime.datetime(2023, 3, 27, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 28, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 27, 20, ),
        datetime.datetime(2023, 3, 27, 21, ),
        datetime.datetime(2023, 3, 27, 22, ),
        datetime.datetime(2023, 3, 27, 23, ),
        datetime.datetime(2023, 3, 28, 0, ),
        datetime.datetime(2023, 3, 28, 1, ),
        datetime.datetime(2023, 3, 28, 2, ),
        datetime.datetime(2023, 3, 28, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_S4.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)
    
    
def figure_S5():
    dt_fr_tec = datetime.datetime(2023, 3, 28, 15, )
    dt_to_tec = datetime.datetime(2023, 3, 29, 15, 59)
    
    time_list = [
        datetime.datetime(2023, 3, 28, 20, ),
        datetime.datetime(2023, 3, 28, 21, ),
        datetime.datetime(2023, 3, 28, 22, ),
        datetime.datetime(2023, 3, 28, 23, ),
        datetime.datetime(2023, 3, 29, 0, ),
        datetime.datetime(2023, 3, 29, 1, ),
        datetime.datetime(2023, 3, 29, 2, ),
        datetime.datetime(2023, 3, 29, 3, ),
    ]
    
    file_name = "event_20230323_ISEE_TECs_Figure_S5.png"
    
    show_TEC(dt_fr_tec, dt_to_tec, time_list, file_name=file_name)   
    

if __name__ == "__main__":
    figure_4()
    figure_S1()
    figure_S2()
    figure_S3()
    figure_S4()
    figure_S5()
    
