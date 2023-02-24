from collections import deque

class VeneirEyes:

    # baseKey = ["U", "N", "D", "E", "C", "I", "P", "H", "E", "R", "E", "D"]
    baseKey = ["R", "U", "B", "E", "D", "O"]
    # ‘BDMAGICKEFHJLNOPQRSTUVWXYZ’
    modAlphabet = ["B","D","M","A","G","I","C","K","E","F","H","J","L","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # modAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    def __init__(self, msg, key = baseKey):
        self.msg = msg
        self.key = key

    def getLetter(self, initLetter, keyLetter):
        index = self.alphabet.index(keyLetter)
        currentModAlphabet = deque(self.modAlphabet)
        currentModAlphabet.rotate(-index)
        return  self.alphabet[list(currentModAlphabet).index(initLetter)]

    def decryptMsg(self):
        returnMsg = ""
        rotkey = deque(self.key)
        for l in self.msg:
            returnMsg += self.getLetter(l , list(rotkey)[0])
            rotkey.rotate(-1)
        return returnMsg