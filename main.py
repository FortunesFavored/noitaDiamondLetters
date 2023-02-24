import json
from pprint import pprint
from eyeFuncs import EyeFunctions
from vernierEye import VeneirEyes


file = open("cleanEyeData.json")

eyeData = json.load(file)

eyeClass = EyeFunctions(eyeData)

# print(eyeClass.genEyes(eyeClass.locations["east1"]))
# print(sum(1 for _ in eyeClass.genEyes(eyeClass.locations["east1"])))

east1 = eyeClass.createDiamondWalkHeatMap("east1",0,1)
east2 = eyeClass.createDiamondWalkHeatMap("east2",0,1)
east3 = eyeClass.createDiamondWalkHeatMap("east3",0,1)
east4 = eyeClass.createDiamondWalkHeatMap("east4",0,1)
east5 = eyeClass.createDiamondWalkHeatMap("east5",0,1)
west1 = eyeClass.createDiamondWalkHeatMap("west1",0,1)
west2 = eyeClass.createDiamondWalkHeatMap("west2",0,1)
west3 = eyeClass.createDiamondWalkHeatMap("west3",0,1)
west4 = eyeClass.createDiamondWalkHeatMap("west4",0,1)


decryptEast1 = VeneirEyes(east1[1])
decryptEast2 = VeneirEyes(east2[1])
decryptEast3 = VeneirEyes(east3[1])
decryptEast4 = VeneirEyes(east4[1])
decryptEast5 = VeneirEyes(east5[1])
decryptWest1 = VeneirEyes(west1[1])
decryptWest2 = VeneirEyes(west2[1])
decryptWest3 = VeneirEyes(west3[1])
decryptWest4 = VeneirEyes(west4[1])

# msg = "CsbswkwhrxikijbswihzmxroygwitaivirgkoaluwmiymxvdgfwlgdxnieiuyqhgkxwlvvhwykwaktajlrrjynfgqzsprxxrqulgjbgpkiepmjksumalxkiumlrytmpzwzkqyqIstmmhqgphcsbswkwhrxiwbroivbtyxyewcfdwuqvuiuxrugumizptaymfbbfgwzhlpvzhhglqgaioiecrojlpniazstldhthinmklrciwnruwqnioimmjyahvgltjmglhlrgxgfi"
# msg = msg.upper()
# decryptMsg = VeneirEyes(msg)
# print(decryptMsg.decryptMsg())
# print(decryptMsg.key)

# msg2 = "CsbswkwhrxikijbswihzmxroygwitaivirgkoaluwmiymxvdgfwlgdxnieiuyqhgkxwlvvhwykwaktajlrrjynfgqzsprxxrqulgjbgpkiepmjksumalxkiumlrytmpzwzkqyqIstmmhqgphcsbswkwhrxiwbroivbtyxyewcfdwuqvuiuxrugumizptaymfbbfgwzhlpvzhhglqgaioiecrojlpniazstldhthinmklrciwnruwqnioimmjyahvgltjmglhlrgxgfi"
# msg2 = msg2.upper()
# decryptMsg2 = VeneirEyes(msg2)
# print(decryptMsg2.decryptMsg())
# print(decryptMsg2.key)


print("Basic East1:", east1[1])
print("Basic East2:", east2[1])
print("Basic East3:", east3[1])
print("Basic East4:", east4[1])
print("Basic East5:", east5[1])
print("Basic West1:", west1[1])
print("Basic West2:", west2[1])
print("Basic West3:", west3[1])
print("Basic West4:", west4[1])
print("\n")
print("Moded East1:",decryptEast1.decryptMsg())
print("Moded East2:",decryptEast2.decryptMsg())
print("Moded East3:",decryptEast3.decryptMsg())
print("Moded East4:",decryptEast4.decryptMsg())
print("Moded East5:",decryptEast5.decryptMsg())
print("Moded West1:",decryptWest1.decryptMsg())
print("Moded West2:",decryptWest2.decryptMsg())
print("Moded West3:",decryptWest3.decryptMsg())
print("Moded West4:",decryptWest4.decryptMsg())
