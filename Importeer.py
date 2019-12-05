"""
Importeren van een excelsheet waarbij één sprint wordt uitgekozen met behulp van de containingstring
"""
import pandas as pd
import numpy as np


def dfSprint(containingString='S1'):

    dfProjectTasks = pd.read_excel('MODPRdataset.xlsx', sheet_name='Project tasks')
    dfProjectTasks = dfProjectTasks.fillna(0)
    dfProjectTasks.replace("x", 1, inplace=True)
    dfProjectTasks = dfProjectTasks[dfProjectTasks['Task'] != 0]

    dfSprint = pd.DataFrame(dfProjectTasks[dfProjectTasks['Task'].str.contains(containingString)],
                            columns=list(dfProjectTasks)).reset_index(drop=True)

    dfSprint.loc[:, 'Crew'] = [20] * len(dfSprint)
    dfSprint['Crew'] = dfSprint['Crew'].astype(object)

    dfSprint.loc[:, 'Mogelijkheden'] = [20] * len(dfSprint)
    dfSprint['Mogelijkheden'] = dfSprint['Mogelijkheden'].astype(object)

    dfSprint.loc[:, 'AantalMogelijkheden'] = [20] * len(dfSprint)
    dfSprint['AantalMogelijkheden'] = dfSprint['AantalMogelijkheden'].astype(int)

    dfSprint['MaxReqCrew'].replace(0, 6, inplace=True)
    dfSprint['Counter'] = 0
    dfSprint.at[dfSprint.Task.str.contains("A"), "Counter"] = 1

    dfSprint['Voltooid'] = False
    dfSprint['Eis'] = ""
    dfSprint['Eis'] = dfSprint['Task'].apply(lambda Task: Task[:-1] + 'A' if Task.endswith('B') else 'no')
    dfSprint['Moment Voltooid'] = ""
    dfSprint['Dag Voltooid'] = ""

    return dfSprint


"""
importeert de additional tasks van een excel bestand en returnt twee verschillende dataframes,
een voor prep en een voor post
"""


def AdditionalTasks(containingString='S1'):
    dfAdditionalTasks = pd.read_excel('MODPRdataset.xlsx', sheet_name='Additional tasks')
    dfAdditionalTasks = dfAdditionalTasks.fillna(0)
    dfAdditionalTasks.replace("x", 1, inplace=True)
    dfAdditionalTasks = dfAdditionalTasks[dfAdditionalTasks['Task'] != 0].reset_index(drop=True)
    dfAdditionalTasks['aantal keer'].replace(0, 1, inplace=True)
    dfSprintAdd = pd.DataFrame(dfAdditionalTasks[dfAdditionalTasks['Task'].str.contains(containingString)]).reset_index(drop=True)
    dfSprintAdd['Voltooid'] = False
    dfSprintAdd.loc[:, 'Crew'] = [20] * len(dfSprintAdd)
    dfSprintAdd['Crew'] = dfSprintAdd['Crew'].astype(object)

    dfSprintAdd['DurationExp.1'] = dfSprintAdd['DurationExp.1'] + 0.5 * np.ceil(2.33 * 2 * dfSprintAdd['DurationStd.1'])
    dfSprintAdd['DurationExp.2'] = dfSprintAdd['DurationExp.2'] + 0.5 * np.ceil(2.33 * 2 * dfSprintAdd['DurationStd.2'])
    dfSprintAdd['DurationExp.3'] = dfSprintAdd['DurationExp.3'] + 0.5 * np.ceil(2.33 * 2 * dfSprintAdd['DurationStd.3'])

    dfSprintAddprep = pd.DataFrame(dfSprintAdd[dfSprintAdd['Task'].str.contains('prep')]).reset_index(drop=True)
    dfSprintAddpost = pd.DataFrame(dfSprintAdd[dfSprintAdd['Task'].str.contains('post')]).reset_index(drop=True)

    return [dfSprintAddprep, dfSprintAddpost]


def SprintAdditional(containingString='S1'):
    """
    importeren van het dataframe voor de add tasks, niet de prep en post.
    """
    dfAdditionalTasks = pd.read_excel('MODPRdataset.xlsx', sheet_name='Additional tasks')
    dfAdditionalTasks = dfAdditionalTasks.fillna(0)
    dfAdditionalTasks.replace("x", 1, inplace=True)
    dfAdditionalTasks = dfAdditionalTasks[dfAdditionalTasks['Task'] != 0].reset_index(drop=True)
    dfAdditionalTasks['aantal keer'].replace(0, 1, inplace=True)
    dfSprintAdd = pd.DataFrame((dfAdditionalTasks.loc[~dfAdditionalTasks['Task'].str.contains(containingString)])).reset_index(drop=True)
    dfSprintAdd = pd.DataFrame((dfSprintAdd[dfSprintAdd['Sprint'] == int(containingString[1])])).reset_index(drop=True)
    dfSprintAdd['Voltooid'] = False
    dfSprintAdd.loc[:, 'Crew'] = [20] * len(dfSprintAdd)
    dfSprintAdd['Crew'] = dfSprintAdd['Crew'].astype(object)
    dfSprintAdd['DurationExp.1'] = dfSprintAdd['DurationExp.1'] + 0.5 * np.ceil(2.33 * 2 * dfSprintAdd['DurationStd.1'])

    return dfSprintAdd


"""
importeert de sheet voor de crew en returnt een dataframe voor de crew

"""


def Crew():
    dfCrew = pd.read_excel('MODPRdataset.xlsx', sheet_name='Crew')
    dfCrew = dfCrew.fillna(0)
    dfCrew.replace("x", 1, inplace=True)
    dfCrew['Uren'] = dfCrew.iloc[:, 14:19].sum(axis=1) * 70
    return dfCrew


"""
importeren van de rooms
"""


def Rooms():
    dfRooms = pd.read_excel('MODPRdataset.xlsx', sheet_name='Rooms')
    dfRooms = dfRooms.fillna(1)

    return dfRooms
