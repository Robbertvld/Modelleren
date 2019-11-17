"""
het maken van een lege kalender
"""
import pandas as pd
import numpy as np


def LegeKalender():
    data = pd.date_range("2020-01-06", periods=4 * 10 * 7, freq='D')

    columns = ['Datum', 'Sprint', 'Weeknummer', 'DagRooster', 'Werkdag']

    dfLegeKalender = pd.DataFrame(columns=columns)
    dfLegeKalender['Datum'] = data
    dfLegeKalender = dfLegeKalender.fillna(0)
    dfLegeKalender.replace("0", False, inplace=True)

    dfLegeKalender['Werkdag'] = dfLegeKalender['Datum'].apply(lambda Datum: Datum.isoweekday() in range(1, 6))
    dfLegeKalender = dfLegeKalender[dfLegeKalender['Werkdag']]
    dfLegeKalender = dfLegeKalender.reset_index(drop=True)

    return dfLegeKalender


def RoosterCrew(dfCrew):
    tijd = pd.date_range("09:00", "17:30", freq="30min").time
    tijd = np.delete(tijd, 13, axis=0)
    tijd = np.delete(tijd, 6, axis=0)

    columns = np.array(dfCrew['Crew members'])

    dfRooster = pd.DataFrame(columns=columns)
    dfRooster['Tijd'] = tijd
    dfRooster = dfRooster.fillna(0)
    dfRooster.replace("0", False, inplace=True)

    # volgorde veranderen
    kols = dfRooster.columns.tolist()
    kols_volg = kols[-1:] + kols[:-1]
    dfRooster = dfRooster[kols_volg]

    a = [7] * (len(dfRooster.iloc[1, :]) - 1)
    a.insert(0, 'urenTeGaan')

    n_rij = pd.DataFrame(a).T
    n_rij.columns = kols

    dfRooster = pd.concat([n_rij, dfRooster]).reset_index(drop=True)
    return dfRooster


def RoosterKamer(dfRooms):
    lijstkamers = dfRooms['Room'].iloc[0:10].tolist()
    tijd = pd.date_range("09:00", "17:30", freq="30min").time
    tijd = np.delete(tijd, 13, axis=0)
    tijd = np.delete(tijd, 6, axis=0)

    lijstkamers.append("office A1")
    lijstkamers.append("office A2")
    lijstkamers.append("office A3")
    lijstkamers.append("office A4")
    lijstkamers.append("office A5")
    lijstkamers.append("office B1")
    lijstkamers.append("office B2")
    lijstkamers.append("office B3")
    lijstkamers.append("office B4")
    lijstkamers.append("office C1")
    lijstkamers.append("office C2")
    lijstkamers.append("office C3")
    lijstkamers.append("office C4")

    dfRoosterKamer = pd.DataFrame(columns=lijstkamers)
    dfRoosterKamer['Tijd'] = tijd
    dfRoosterKamer = dfRoosterKamer.fillna(0)
    dfRoosterKamer.replace("0", False, inplace=True)

    # volgorde veranderen
    cols = dfRoosterKamer.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    dfRoosterKamer = dfRoosterKamer[cols]
    return dfRoosterKamer
