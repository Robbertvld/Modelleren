# rangeWorkdays = range(14,19)
# rangeRooms = range(14,20)
"""
In deze file staan verschillende hulp functies met betrekking op het modelleer project 2019.

"""

"""
functie waarbij de lijst van ReqSkill moet worden ingevuld van de Task en de skills van een persoon. De functie geeft een boolean terug of deze taak door deze persoon kan worden gedaan.

voorbeeld:
OpdrachtUitvoeren(dfProjectTasks.iloc[0,rangeSkills],dfCrew.iloc[0,rangeSkills])
uitkomst: False
"""
import pandas as pd


def OpdrachtUitvoerenPersoonBool(eisen, persoon):
    for i in range(1, 14):  # de range van de skills
        result = (int(eisen[i - 1]) <=
                  int(persoon[i - 1]))
        if result == False:
            break
    return result


"""
de functie hieronder voegt de skills van personen samen en geeft de gezamelijke skills terug en het surplus.

voorbeeld: PersonenSamenvoegen(dfCrew.iloc[0,rangeSkills],dfCrew.iloc[2,rangeSkills])
uitkomst: [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]
"""


def PersonenSamenvoegen(persoon1, persoon2=[0] * 13, persoon3=[0] * 13, persoon4=[0] * 13, persoon5=[0] * 13, persoon6=[0] * 13):
    combinedSkill = []
    surplus = 0
    for i in range(1, 14):  # de range van de skills
        combinedSkill.append(int(1) if persoon1[i - 1] + persoon2[i - 1] + persoon3[i - 1] + persoon4[i - 1] + persoon5[i - 1] + persoon6[i - 1] > 0 else int(0))
        surplus = surplus + (persoon1[i - 1] + persoon2[i - 1] + persoon3[i - 1] + persoon4[i - 1] + persoon5[i - 1] + persoon6[i - 1] - 1
                             if persoon1[i - 1] + persoon2[i - 1] + persoon3[i - 1] + persoon4[i - 1] + persoon5[i - 1] + persoon6[i - 1] > 0 else int(0))
    combinedSkill.append(surplus)
    return combinedSkill


"""
voorbeeld: ZoekKamers(dfSprint1.iloc[0,14:20], dfSprint1)
['workspace A',
 'workspace B',
 'workspace C',
 'workshop A',
 'workshop B',
 'workshop C',
 'assembly A',
 'assembly B']
"""


def ZoekKamers(eisenKamers, dfSprint):
    lijstkamers = []
    for i in range(0, len(eisenKamers)):
        if list(eisenKamers)[i] == 1:
            if ("****" in list(dfSprint)[14 + i]):
                lijstkamers.append("assembly A")
                lijstkamers.append("assembly B")
            if ("***" in list(dfSprint)[14 + i] and not "****" in list(dfSprint)[14 + i]):
                lijstkamers.append("workshop A")
                lijstkamers.append("workshop B")
                lijstkamers.append("workshop C")
            if ("**" in list(dfSprint)[14 + i] and not "***" in list(dfSprint)[14 + i]):
                lijstkamers.append("workspace A")
                lijstkamers.append("workspace B")
                lijstkamers.append("workspace C")

            elif ("4" in list(dfSprint)[14 + i] or "5" in list(dfSprint)[14 + i]):
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

            elif ("technical" in list(dfSprint)[14 + i]):
                lijstkamers.append("technical A")
                lijstkamers.append("technical B")

    return lijstkamers


"""
voorbeeld:
ZoekOpdrachten(dfSprint1.iloc[0,rangeSkills], MinMaxPersonen= [1,2], dfCrewCombined)
[[9, 0, 20, 20, 20, 20],
 [10, 9, 20, 20, 20, 20],
 [10, 9, 0, 20, 20, 20],
 [11, 10, 20, 20, 20, 20],
 [11, 4, 20, 20, 20, 20], ....
"""


def ZoekOpdrachten(project, MinMaxPersonen, dfCrewCombined):
    crew = []
    for i in range(0, len(dfCrewCombined)):
        if (dfCrewCombined.Aantalpersonen[i] >= MinMaxPersonen[0] and dfCrewCombined.Aantalpersonen[i] <= MinMaxPersonen[0]):
            if (OpdrachtUitvoerenPersoonBool(project, dfCrewCombined.iloc[i, 0:13])):
                crew.append(list(dfCrewCombined.iloc[i, 14:20]))
    return crew


"""
Contains kijkt of een lijst met elementen een subset is van een andere lijst.
Dit wordt vooral gebruikt bij het zoeken naar een plek in het rooster waar een lijst met nullen (met lengte duration)
in het rooster past.

returnt false als het niet kan en twee getallen als het wel kan.
"""


def contains(sub, pri):
    M, N = len(pri), len(sub)
    i, LAST = 0, M - N + 1
    while True:
        try:
            found = pri.index(sub[0], i, LAST)  # find first elem in sub
        except ValueError:
            return False
        if pri[found:found + N] == sub:
            return [found, found + N - 1]
        else:
            i = found + 1


"""
Combineert twee lijsten. Hier vaak gebruikt met 1 en 0. Zodra index 1 0 bij de ene is en 1 bij de ander, wordt het 1,
zo gaat deze de hele lijst door en geeft deze het resultaat terug.
"""


def CombinatieLijst(lijst1, lijst2):
    lijstfinal = []
    if (len(lijst1) == len(lijst2)):
        for i in range(0, len(lijst1)):
            if((lijst1[i] == 0) & (lijst2[i] == 0)):
                lijstfinal.append(0)
            else:
                lijstfinal.append(1)
        return lijstfinal
    else:
        Exception("Lengte van de lijst klopt niet")
        return


"""
"Het toevoegen van de mogelijke combinaties aan het dataframe dfSprint"
"""


def ToevoegenMogelijkeCombinaties(rij, dfSprint, dfCrewCombined):
    from Class import MogelijkeCombinaties
    a = ZoekKamers(rij.iloc[14:20], dfSprint)
    b = ZoekOpdrachten(rij.iloc[range(1, 14)], rij.iloc[20:22], dfCrewCombined)
    c = pd.DataFrame(data=[[a] * len(b), b])
    return MogelijkeCombinaties(c.T, len(a) * len(b))


"""
Het sommeren van de overige uren van de crewleden, in een dataframe
"""


def somOverigeUren(crewlijst, weeknummers, dfKalenderCrew):

    resultaat = pd.DataFrame(columns=['crew', 'som'])
    for i in crewlijst:
        som = 0
        if (i == 20):
            break
        for weeknummer in weeknummers:
            for j in range(0 + 5 * (weeknummer - 1), 5 * weeknummer):
                som += dfKalenderCrew.iloc[j, :].DagRooster.dfRooster.iloc[0, i + 1]  # want kolom tijd wordt ook meegenomen
        resultaat = resultaat.append({'crew': i, 'som': int(som)}, ignore_index=True)
    if(type(resultaat) == 'NoneType'):
        Exception("Nonetype")
    return resultaat.sort_values(['som'], ascending=[False])
