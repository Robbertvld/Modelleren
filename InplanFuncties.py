def InplannenOSHA(urenPerWeek, dfKalenderCrew, dfAdd, OSHA, dfCrew):
    """
    Het inplannen van osha voor de resterende uren naast de standaard 2,5 uur in de week (normaal dus nog 15 uur), op woensdag in de eerste week en 9 en 10.
    """
    duur = dfAdd.loc[dfAdd['Task'].str.contains("OSHA"), 'DurationExp.1'] - 25  # totale uren berekenen, naast de 2,5 uur per week (daarom de min 25)
    duur = duur.tolist()[0]

    for crew in OSHA:
        dfCrew['Uren'].iloc[crew] -= (duur + 25)  # het totaal aantaal uren aanpassen.
    # voor sprint 1 en 2. In de andere weken is het 2,5 uur standaard en in de andere weken iets meer.
    weken = [1, 9, 10]
    for week in weken:  # het inplannen wordt op woensdag gedaan
        for crew in OSHA:
            dfKalenderCrew.iloc[(week - 1) * 5 + 3, :].DagRooster.dfRooster.iloc[1:int((urenPerWeek * 2 + 2)), crew + 1] = "OSHA"
            dfKalenderCrew.iloc[(week - 1) * 5 + 3, :].DagRooster.dfRooster.iloc[0, crew + 1] = dfKalenderCrew.iloc[(week - 1) * 5 + 3, :].DagRooster.dfRooster.iloc[0, crew + 1] - urenPerWeek
        duur -= urenPerWeek  # uur aanpassen voor de rest van de weken (totaal is 40 uur)
        if (urenPerWeek > duur):  # mocht het minder dan het aantal uren per week zijn, wordt het restant gebruikt
            urenPerWeek = duur

    dfAdd.loc[dfAdd['Task'].str.contains("OSHA"), 'Voltooid'] = True  # het veranderen van de kalender
    dfAdd.at[dfAdd.index[dfAdd['Task'].str.contains("OSHA")].tolist()[0], 'Crew'] = OSHA

    return [dfKalenderCrew, dfAdd]
