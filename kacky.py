import requests
import os

os.system("cls")

purple = "\033[38;5;141m"
orange = "\033[38;5;208m"
reset = "\033[0m"

DASHBOARDURL = "https://api.kacky.info/dashboard"
dashboard = requests.get(DASHBOARDURL).json()["servers"]
allMaps = list(reversed(range(-200, -150)))

def reformatList(allMaps, currentMap):
    return allMaps[allMaps.index(currentMap):] + allMaps[:allMaps.index(currentMap)]

def findNearestMap(currentMap, targetMap):
    mapList = reformatList(allMaps, currentMap)
    count = 0

    for map in mapList:
        if map == targetMap:
            return count
        else:
            count += 1

def getServerClosestToMap(map):
    closestServer = 0
    closestDistance = 999
    for server in dashboard:
        distance = findNearestMap(server["maps"][0]["number"], map)
        if distance < closestDistance:
            closestDistance = distance
            closestServer = server["serverNumber"]
    return (closestServer, closestDistance * 10)
                                                                         
print(purple)
print(" ")
print(" ")
print(" ")
print("          ██╗  ██╗██╗  ██╗ █████╗     ████████╗██╗███╗   ███╗██╗███╗   ██╗ ██████╗       By Byro")
print("          ██║ ██╔╝██║ ██╔╝██╔══██╗    ╚══██╔══╝██║████╗ ████║██║████╗  ██║██╔════╝       Version 1.0")
print("          █████╔╝ █████╔╝ ╚█████╔╝       ██║   ██║██╔████╔██║██║██╔██╗ ██║██║  ███╗")
print("          ██╔═██╗ ██╔═██╗ ██╔══██╗       ██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║      Built for kackiest Kacky 8")
print("          ██║  ██╗██║  ██╗╚█████╔╝       ██║   ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝      Maps: -151 to -200")
print("          ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝        ╚═╝   ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝       Use it well!")
print(" ")
print(" ")


map = input("          What map (-151 to -200): ")
if int(map) >= -200 and int(map) <= -150:
    result = getServerClosestToMap(int(map))
    print(" ")
    print(f"          Server {orange + str(result[0]) + purple} will play {orange + '#' + str(map) + purple} in abount {orange + str(result[1]) + purple} minutes.")
else:
    print(" ")
    print("Invalid map number, must be between -200 and -150.")