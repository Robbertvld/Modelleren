"""
Importeren van een excelsheet waarbij één sprint wordt uitgekozen met behulp van de containingstring
"""
import pandas as pd


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

    dfSprint['Voltooid'] = False
    dfSprint['Eis'] = ""
    dfSprint['Eis'] = dfSprint['Task'].apply(lambda Task: Task[:-1] + 'A' if Task.endswith('B') else 'no')
    dfSprint['Moment Voltooid'] = ""
    dfSprint['Dag Voltooid'] = ""

    return dfSprint


"""
importeert de additional tasks van een excel bestand en returnt twee verschillende bestanden (csv),
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

    dfSprintAddprep = pd.DataFrame(dfSprintAdd[dfSprintAdd['Task'].str.contains('prep')]).reset_index(drop=True)
    dfSprintAddpost = pd.DataFrame(dfSprintAdd[dfSprintAdd['Task'].str.contains('post')]).reset_index(drop=True)

    return [dfSprintAddprep, dfSprintAddpost]


"""
importeert de sheet voor de crew en returnt een dataframe voor de crew

"""


def Crew():
    dfCrew = pd.read_excel('MODPRdataset.xlsx', sheet_name='Crew')
    dfCrew = dfCrew.fillna(0)
    dfCrew.replace("x", 1, inplace=True)
    return dfCrew


"""
importeren van de rooms
"""


def Rooms():
    dfRooms = pd.read_excel('MODPRdataset.xlsx', sheet_name='Rooms')
    dfRooms = dfRooms.fillna(1)

    return dfRooms
