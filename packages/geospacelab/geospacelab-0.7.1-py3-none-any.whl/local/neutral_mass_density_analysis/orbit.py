import numpy as np
import datetime
import copy
import pickle
import pathlib

import geospacelab.observatory.orbit.sc_orbit as sco
import geospacelab.observatory.orbit.utilities as scu
import geospacelab.toolbox.utilities.pydatetime as mydt

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

fd_sc_root = pathlib.Path("/home/lei/extra/AFEISCAT3/Data/SC")


def get_daily_nodes(year, sat_id, force_save=False):

    # sco.OrbitPosition_SSCWS.list_satellites()

    file_name = f"Daily_Nodes_{sat_id.upper()}_{str(year)}.pickle"
    file_path = fd_sc_root / sat_id.upper() / file_name
    if not file_path.is_file():
        force_save = True
    if not force_save:
        with open(file_path, 'rb') as f:
            sc_data = pickle.load(f)
            return sc_data

    dt_fr = datetime.datetime(year, 1, 1, 0, 0, 0)
    dt_to = datetime.datetime(year, 12, 31, 23, 59, 59)

    ndays = mydt.get_diff_days(dt_fr, dt_to)

    sc_data = {'dataset': None, 'GEO_ALT_M': np.ones((ndays,)) * np.nan, 'GEO_ALT_H': np.ones((ndays,)) * np.nan,
               'GEO_ALT_L': np.ones((ndays,)) * np.nan,
               'DATETIME': np.array([dt_fr + datetime.timedelta(days=dd, hours=12) for dd in range(ndays)]),
               'ASC_LST': np.ones((ndays,)) * np.nan, 'DSC_LST': np.ones((ndays,)) * np.nan}

    try:
        ds_orbit = sco.OrbitPosition_SSCWS(dt_fr, dt_to, sat_id=sat_id, allow_download=True)
        ds_orbit.add_GEO_LST()

        ds_leo = scu.LEOToolbox(dt_fr, dt_to)
        ds_leo.clone_variables(ds_orbit)
        ds_leo.search_orbit_nodes()
        dts_leo = ds_leo['SC_DATETIME'].flatten()
        alts_leo = ds_leo['SC_GEO_ALT'].flatten()
        for dd in range(ndays):
            dt_fr_1 = mydt.get_start_of_the_day(dt_fr + datetime.timedelta(days=dd))
            dt_to_1 = mydt.get_end_of_the_day(dt_fr + datetime.timedelta(days=dd))
            dts_asc = ds_leo.ascending_nodes['DATETIME']
            ind_t = np.where((dts_asc >= dt_fr_1) & (dts_asc <= dt_to_1))[0]
            if not list(ind_t):
                continue
            lsts = ds_leo.ascending_nodes['GEO_LST'][ind_t]
            if list(np.where(np.diff(lsts)>1.)[0]):
                lsts = np.where(lsts>12., lsts - 24., lsts)
            lst_mean = np.mean(lsts)
            lst_mean = np.mod(lst_mean, 24.)
            sc_data['ASC_LST'][dd] = lst_mean

            dts_dsc = ds_leo.descending_nodes['DATETIME']
            ind_t = np.where((dts_dsc >= dt_fr_1) & (dts_dsc <= dt_to_1))[0]
            if not list(ind_t):
                continue
            lsts = ds_leo.descending_nodes['GEO_LST'][ind_t]
            if list(np.where(np.diff(lsts)>1.)[0]):
                lsts = np.where(lsts>12., lsts - 24., lsts)
            lst_mean = np.mean(lsts)
            lst_mean = np.mod(lst_mean, 24.)
            sc_data['DSC_LST'][dd] = lst_mean

            dts_1 = dts_asc[ind_t][int(len(ind_t) / 2)]

            ind_t_2 = np.where(
                (dts_leo >= dts_1 - datetime.timedelta(minutes=50)) &
                (dts_leo <= dts_1 + datetime.timedelta(minutes=50))
            )[0]
            alts = alts_leo[ind_t_2]
            sc_data['GEO_ALT_M'][dd] = (np.max(alts) + np.min(alts))/2.
            sc_data['GEO_ALT_H'][dd] = np.max(alts)
            sc_data['GEO_ALT_L'][dd] = np.min(alts)
    except Exception as e:
        print(e)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as f:
        pickle.dump(sc_data, f, protocol=pickle.HIGHEST_PROTOCOL)
    # sc_data['dataset'] = ds_leo
    return sc_data


def get_sc_nodes_multiple():
    yys = np.arange(2014, 2024, 1,).astype(int)
    for yy in yys:

        swarma_data = get_daily_nodes(yy, sat_id='swarma')
        swarmb_data = get_daily_nodes(yy, sat_id='swarmb')
        grace_data = get_daily_nodes(yy, sat_id='grace1')
        gracefo_data = get_daily_nodes(yy, sat_id='gracefo1')


def search_conjugate_nodes(sc_data_1, sc_data_2, delta_t=1.):

    dts = sc_data_1['DATETIME']
    lst_1_asc = sc_data_1['ASC_LST']
    lst_1_dsc = sc_data_1['DSC_LST']
    lst_2_asc = sc_data_2['ASC_LST']
    lst_2_dsc = sc_data_2['DSC_LST']

    t_1 = lst_1_asc
    t_2 = lst_2_asc
    ind_conj_1 = np.where(np.abs(t_2 - t_1) < delta_t / 2.)[0]
    ind_conj_2 = np.where(np.abs(np.abs(t_2 - t_1) - 24) < delta_t / 2.)[0]
    ind_conj_AA = np.sort(np.append(ind_conj_1, ind_conj_2))

    t_1 = lst_1_asc
    t_2 = lst_2_dsc
    ind_conj_1 = np.where(np.abs(t_2 - t_1) < delta_t / 2.)[0]
    ind_conj_2 = np.where(np.abs(np.abs(t_2 - t_1) - 24) < delta_t / 2.)[0]
    ind_conj_AD = np.sort(np.append(ind_conj_1, ind_conj_2))

    t_1 = lst_1_dsc
    t_2 = lst_2_asc
    ind_conj_1 = np.where(np.abs(t_2 - t_1) < delta_t / 2.)[0]
    ind_conj_2 = np.where(np.abs(np.abs(t_2 - t_1) - 24) < delta_t / 2.)[0]
    ind_conj_DA = np.sort(np.append(ind_conj_1, ind_conj_2))

    t_1 = lst_1_dsc
    t_2 = lst_2_dsc
    ind_conj_1 = np.where(np.abs(t_2 - t_1) < delta_t / 2.)[0]
    ind_conj_2 = np.where(np.abs(np.abs(t_2 - t_1) - 24) < delta_t / 2.)[0]
    ind_conj_DD = np.sort(np.append(ind_conj_1, ind_conj_2))

    ind_conj = np.unique(np.concatenate((ind_conj_AA, ind_conj_AD, ind_conj_DA, ind_conj_DD)))

    if ind_conj.shape[0] == 0:
        return [], [], [], []

    dts_conj = dts[ind_conj]
    dt0 = dts[0]
    sectime = [(dt - dt0).total_seconds() for dt in dts_conj]
    ind_t = np.where(np.diff(sectime) > 86400)[0]
    dts_conj_0 = np.array((dts_conj[0],))
    dts_conj_1 = np.array((dts_conj[-1],))
    if list(ind_t):
        dts_conj_0 = np.concatenate((dts_conj_0, dts_conj[np.array(ind_t)+1]))
        dts_conj_1 = np.concatenate((dts_conj[np.array(ind_t)], dts_conj_1))
    return ind_conj, dts_conj, dts_conj_0, dts_conj_1


def show_sc_nodes(yy_fr=2013, yy_to=2023, ):
    def append_data(sc_data, new_data):
        for key, value in new_data.items():
            sc_data[key] = np.append(sc_data[key], value)
        return sc_data

    def insert_nan(dts, lsts):

        diff_lst = np.diff(lsts)
        ind_t = np.where(diff_lst > 12.)[0]
        dts_insert = dts[ind_t] + datetime.timedelta(hours=1)
        lsts_insert = np.ones((len(ind_t), )) * np.nan
        dts = np.insert(dts, ind_t + 1, dts_insert)
        lsts = np.insert(lsts, ind_t + 1, lsts_insert)
        return dts, lsts

    def add_plots(sc_data, color=None, sat_label=None):
        dts = sc_data['DATETIME']
        lst_asc = sc_data['ASC_LST']
        lst_dsc = sc_data['DSC_LST']
        alt_M = sc_data['GEO_ALT_M']
        alt_H = sc_data['GEO_ALT_H']
        alt_L = sc_data['GEO_ALT_L']
        color = color
        dts_new, lst_new = insert_nan(dts, lst_asc)
        axs[0].plot(dts_new, lst_new, '-', color=color, label=sat_label + '-ASC')
        dts_new, lst_new = insert_nan(dts, lst_dsc)
        axs[0].plot(dts_new, lst_new, ':', color=color, label=sat_label + '-DSC')

        axs[1].fill_between(dts, alt_L, alt_H, color=color, alpha=0.2)
        axs[1].plot(dts, alt_M, '-', color=color, label=sat_label)
        pass

    def fill_between_dates(dts_0, dts_1, color=None):
        for dt_0, dt_1 in zip(dts_0, dts_1):
            y = [0, 24]
            x1 = [dt_0, dt_0]
            x2 = [dt_1, dt_1]
            axs[0].fill_betweenx(y, x1, x2, color=color, alpha=0.1, edgecolor=None)

            y = [0, 600]
            x1 = [dt_0, dt_0]
            x2 = [dt_1, dt_1]
            axs[1].fill_betweenx(y, x1, x2, color=color, alpha=0.1, edgecolor=None)

    swarma_data = None
    swarmb_data = None
    grace_data = None
    gracefo_data = None

    yys = np.arange(yy_fr, yy_to+1, 1,).astype(int)
    for yy in yys:

        if swarma_data is None:
            swarma_data = get_daily_nodes(yy, sat_id='swarma')
        else:
            new_data = get_daily_nodes(yy, sat_id='swarma')
            swarma_data = append_data(swarma_data, new_data)

        if swarmb_data is None:
            swarmb_data = get_daily_nodes(yy, sat_id='swarmb')
        else:
            new_data = get_daily_nodes(yy, sat_id='swarmb')
            swarmb_data = append_data(swarmb_data, new_data)

        if grace_data is None:
            grace_data = get_daily_nodes(yy, sat_id='grace1')
        else:
            new_data = get_daily_nodes(yy, sat_id='grace1')
            grace_data = append_data(grace_data, new_data)

        if gracefo_data is None:
            gracefo_data = get_daily_nodes(yy, sat_id='gracefo1')
        else:
            new_data = get_daily_nodes(yy, sat_id='gracefo1')
            gracefo_data = append_data(gracefo_data, new_data)


    fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(15, 10))

    # add_plots(swarma_data, color='r', sat_label='Swarm-A')
    add_plots(swarmb_data, color='b', sat_label='Swarm-B')
    # add_plots(grace_data, color='m', sat_label='GRACE-A')
    add_plots(gracefo_data, color='c', sat_label='GRACE-FO')

    delta_t = 1
    # ind_conj, dts_conj, dts_conj_0, dts_conj_1 = search_conjugate_nodes(swarma_data, swarmb_data, delta_t=delta_t)
    # fill_between_dates(dts_conj_0, dts_conj_1, color='r')

    # ind_conj, dts_conj, dts_conj_0, dts_conj_1 = search_conjugate_nodes(swarma_data, grace_data, delta_t=delta_t)
    # fill_between_dates(dts_conj_0, dts_conj_1, color='y')
    #
    # ind_conj, dts_conj, dts_conj_0, dts_conj_1 = search_conjugate_nodes(swarma_data, gracefo_data, delta_t=delta_t)
    # fill_between_dates(dts_conj_0, dts_conj_1, color='k')
    #
    # ind_conj, dts_conj, dts_conj_0, dts_conj_1 = search_conjugate_nodes(swarmb_data, grace_data, delta_t=delta_t)
    # fill_between_dates(dts_conj_0, dts_conj_1, color='g')
    #
    ind_conj, dts_conj, dts_conj_0, dts_conj_1 = search_conjugate_nodes(swarmb_data, gracefo_data, delta_t=delta_t)
    fill_between_dates(dts_conj_0, dts_conj_1, color='b')

    axs[0].legend(loc='upper center', bbox_to_anchor=(1.05, 1.0))
    axs[0].set_ylim([0, 24])
    axs[0].set_ylabel('LST (h)')
    axs[0].grid(True)
    axs[0].xaxis.set_minor_locator(AutoMinorLocator())
    axs[0].yaxis.set_minor_locator(AutoMinorLocator())

    axs[1].set_ylim(200, 600)
    axs[1].set_ylabel('h (km)')
    axs[1].set_xlabel('Date')
    axs[1].set_xlim([datetime.datetime(yy_fr, 1, 1), datetime.datetime(yy_to+1, 1, 1)])
    axs[1].grid(True)
    axs[1].legend(loc='upper center', bbox_to_anchor=(1.05, 1.0))
    axs[1].yaxis.set_minor_locator(AutoMinorLocator())
    plt.tight_layout()

    return fig


if __name__ == "__main__":

    # get_sc_nodes_multiple()
    # search_conjugate_nodes()
    fig = show_sc_nodes()
    plt.savefig('sc_nodes_2013-2023_1h_SB_vs_GF.png')
    plt.show()
    pass

    # swarm_data = get_daily_nodes(2014, sat_id='swarma')
    # grace_data = get_daily_nodes(2014, sat_id='grace1')
    #
    # import matplotlib.pyplot as plt
    # plt.plot(swarm_data['ASC_LST'], '.')
    # plt.plot(swarm_data['DSC_LST'], '.')
    # plt.plot(grace_data['ASC_LST'], 'o')
    # plt.plot(grace_data['DSC_LST'], 'o')
    # plt.show()