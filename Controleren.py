"""
Het controleren van het inplannen
"""


def EvaluateProgram(dfTasks, dfRoosterVoor, dfRoosterNa):
    urenTeGaan, totaal, som, count = [0, 0, 0, 0]
    for i in range(0, 5):  # deze kan worden verhoogt zodra er meer dagen worden ingevuld.
        urenTeGaan += sum(dfRoosterVoor.iloc[i, :].DagRooster.dfRooster.iloc[0, :].tolist()[1:])
        totaal += sum(dfRoosterNa.iloc[i, :].DagRooster.dfRooster.iloc[0, :].tolist()[1:])
    for i in range(0, len(dfTasks)):
        som += dfTasks.loc[i, 'MinReqCrew'] * dfTasks.loc[i, 'Frequency'] * dfTasks.loc[i, 'Duration']
        if (dfTasks.Voltooid[i] == False):
            count += 1
    print("Het aantal uur dat nog over is: " + str(totaal))
    print("Van het totaal aantal uren: " + str(urenTeGaan))
    print("Het aantal uur dat moest worden ingepland: " + str(som))
    print("Het aantal opdrachten dat niet zijn ingepland: " + str(count))
