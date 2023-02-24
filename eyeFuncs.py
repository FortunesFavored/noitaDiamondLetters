from letterMap import letterFreq, heatMapLetter

class EyeFunctions:
    locations = {
        "east1": "East1",
        "east2": "East2",
        "east3": "East3",
        "east4": "East4",
        "east5": "East5",
        "west1": "West1",
        "west2": "West2",
        "west3": "West3",
        "west4": "West4",
    }
    translatedMessage = {
        "east1": "",
        "east2": "",
        "east3": "",
        "east4": "",
        "east5": "",
        "west1": "",
        "west2": "",
        "west3": "",
        "west4": "",
    }

    diamondWalk = {
        0: 0,
        1: 1,
        2: 1,
        3: -1,
        4: -1,
    }

    letterFreq = letterFreq
    heatMapLetter = heatMapLetter

    def __init__(self, eyeData):
        self.eyeData = eyeData


    def genEyes(self, location, initial = 0, step=1):
        e = initial
        while e < len(self.eyeData[location]):
            yield self.eyeData[location][e]
            e += step

    def createDiamondWalkHeatMap(self,loc, initial=0, step=1):
        heatMap1 = {}
        msgAttempt = self.translatedMessage[loc]
        for trigram in self.genEyes(self.locations[loc],initial, step):
            x_pos, y_pos = 0,0
            for i in trigram:
                if i == 0:
                    pass
                elif i == 1:
                    y_pos += self.diamondWalk[i]
                elif i == 2:
                    x_pos += self.diamondWalk[i]
                elif i == 3:
                    y_pos += self.diamondWalk[i]
                elif i == 4:
                    x_pos += self.diamondWalk[i]
            xy_pos = f"{x_pos},{y_pos}"
            if xy_pos not in list(heatMap1.keys()):
                heatMap1[xy_pos] = 1
            else:
                heatMap1[xy_pos] += 1
            msgAttempt += self.heatMapLetter[xy_pos]
        return [heatMap1, msgAttempt]

