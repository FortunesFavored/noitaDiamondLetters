from itertools import permutations
import timeit
commonLetters = ["O","E","T","U","Y","R","I","N","S","H","A","W","D","L","G","F","K", "M","V","C","P"]
diamondPosition = ['0,1','1,0','0,0','-1,0','-1,1','-1,2','0,-1','1,-1','-1,-1','0,2','3,0','1,1','-2,1','2,-1','2,1','1,2','-2,0','2,0','1,-2','0,3','0,-2',]

class letterGenerator:


    def __init__(self):
        self.commonLetters = commonLetters
        self.diamondPositions = diamondPosition
        self.LetterPermutations = permutations(self.commonLetters, 7)
        pass

    # def MapGenerator(self):
    #     e = initial
    #     while e < len(self.eyeData[location]):
    #         yield self.eyeData[location][e]
    #         e += step

newLetterGen = letterGenerator()


start = timeit.default_timer()
for i in list(newLetterGen.LetterPermutations):
    pass

end = timeit.default_timer()

print(end - start)
