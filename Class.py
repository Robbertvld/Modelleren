# -----------------------------------------------------------------------
# De classes van het programma modelleren
# -----------------------------------------------------------------------


class MogelijkeCombinaties:
    def __init__(self, dfMogelijkheden, aantalMogelijkheden):
        self.dfMogelijkheden = dfMogelijkheden
        self.aantalMogelijkheden = aantalMogelijkheden


class Rooster:
    def __init__(self, dfRooster):
        self.dfRooster = dfRooster
