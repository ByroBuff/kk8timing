import requests
import os

purple = "\033[38;5;141m"
orange = "\033[38;5;208m"
reset = "\033[0m"

DASHBOARDURL = "https://api.kacky.info/spreadsheet"
dashboard = requests.get(DASHBOARDURL).json()

while True:   
    os.system("cls")                                                               
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
    for server in dashboard:
        if server["kacky_id"] == map:
            print(" ")
            print(f"          Server {orange + str(server['server']) + purple} will play {orange + str(server['kacky_id']) + purple} in abount {orange + str(server['upcomingIn']) + purple} minutes.")
            break
    else:
        print("          Invalid map number, must be between -200 and -150.")

    print(" ")
    print(" ")
    print(" ")
    input("          Press enter to restart...")