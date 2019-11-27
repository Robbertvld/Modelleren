"""
het verzamelen van data van alle gezamelijke skills tot aan 7 personen.
Hierin wordt ook toegevoegd hoeveel personen erin de combinatie zitten.

Het resultaat is een file 'CrewCombined.csv'. Dit zodat de code niet steeds opnieuw moet worden gerund.
"""
import numpy as np
import pandas as pd
import Hulpfuncties


def MakeCrewCombined(dfCrew):
    rangeSkills = range(1, 14)
    dfCrewCombined = []
    for i in range(0, len(dfCrew)):
        t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills])
        t.append(i)
        t.append(20)
        t.append(20)
        t.append(20)
        t.append(20)
        t.append(20)
        t.append(1)

        dfCrewCombined.append(t)

        for j in range(0, len(dfCrew)):  # combinaties met twee mensen
            if i == j:
                break
            t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills], dfCrew.iloc[j, rangeSkills])
            t.append(i)
            t.append(j)
            t.append(20)
            t.append(20)
            t.append(20)
            t.append(20)
            t.append(2)

            dfCrewCombined.append(t)

            for k in range(0, len(dfCrew)):
                if i == k or k == j:
                    break

                t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills], dfCrew.iloc[j, rangeSkills], dfCrew.iloc[k, rangeSkills])
                t.append(i)
                t.append(j)
                t.append(k)
                t.append(20)
                t.append(20)
                t.append(20)
                t.append(3)

                dfCrewCombined.append(t)

                for l in range(0, len(dfCrew)):
                    if l == k or l == i or l == j:
                        break
                    t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills], dfCrew.iloc[j, rangeSkills],
                                                         dfCrew.iloc[k, rangeSkills], dfCrew.iloc[l, rangeSkills])
                    t.append(i)
                    t.append(j)
                    t.append(k)
                    t.append(l)
                    t.append(20)
                    t.append(20)
                    t.append(4)
                    dfCrewCombined.append(t)

                    for m in range(0, len(dfCrew)):
                        if m == l or m == k or m == j or m == i:
                            break
                        t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills], dfCrew.iloc[j, rangeSkills],
                                                             dfCrew.iloc[k, rangeSkills], dfCrew.iloc[l, rangeSkills],
                                                             dfCrew.iloc[m, rangeSkills])
                        t.append(i)
                        t.append(j)
                        t.append(k)
                        t.append(l)
                        t.append(m)
                        t.append(20)
                        t.append(5)
                        dfCrewCombined.append(t)

                        for n in range(0, len(dfCrew)):
                            if n == m or n == l or n == k or n == j or n == i:
                                break
                            t = Hulpfuncties.PersonenSamenvoegen(dfCrew.iloc[i, rangeSkills], dfCrew.iloc[j, rangeSkills],
                                                                 dfCrew.iloc[k, rangeSkills], dfCrew.iloc[l, rangeSkills],
                                                                 dfCrew.iloc[m, rangeSkills], dfCrew.iloc[n, rangeSkills])
                            t.append(i)
                            t.append(j)
                            t.append(k)
                            t.append(l)
                            t.append(m)
                            t.append(n)
                            t.append(6)
                            dfCrewCombined.append(t)
    # het dataframe dfCrewCombined is een dataframe met alle skills van de medewerkers gezamelijk.
    # Zodra er bij een van de personen '20' staat, betekent dit dat er geen persoon voor die plek is toegevoegd.
    # in het dataframe staan combinaties met twee personen tot zeven ('vo) personen.

    # het maken van het dataframe dfCrewCombined en het wegschrijven in csv.
    ar = np.array(dfCrewCombined, dtype=np.int16)
    dfCrewCombined = pd.DataFrame(ar, columns=['Skill1', 'Skill2', 'Skill3', 'Skill4', 'Skill5', 'Skill6', 'Skill7', 'Skill8',
                                               'Skill9', 'Skill10', 'Skill11', 'Skill12', 'Skill13', 'Surplus', 'persoon1', 'persoon2',
                                               'persoon3', 'persoon4', 'persoon5', 'persoon6', 'Aantalpersonen'])

    # creeren van de kolom 'sum' zodat we weten hoeveel skill de crew gecombineerd heeft
    dfCrewCombined['sum'] = dfCrewCombined.iloc[:, 0:13].sum(axis=1)

    # sorteren op de kolommen sum en surplus (overschot aan skills) zodat er zo min mogelijk overbodige skills worden gebruikt
    dfCrewCombined = dfCrewCombined.sort_values(['Aantalpersonen', 'sum', 'Surplus'], ascending=[True, True, True])
    dfCrewCombined = dfCrewCombined.reset_index(drop=True)

    dfCrewCombined.to_csv('CrewCombined.csv', encoding='utf-8', index=False)  # schrijven naar csv
