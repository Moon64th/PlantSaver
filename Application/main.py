from Application.dcBot import dcbot
from Application.plant import *
import tracemalloc

from Application.timer import createTimer

allPlants = PlantColection()

def main():
    sf = input("Enter Software to use (Discord/Console) to close the program tipe: close:")
    if sf.upper() == "DISCORD":
        tracemalloc.start()
        dcbot(allPlants,main)
    elif sf.upper() == "CONSOLE":
        tracemalloc.start()
        sf2 = input("Create new plant(y/n)?")
        while sf2.upper() == "Y":
            newPlant = createplant()
            allPlants.add_plants(newPlant)
            sf2 = input("Create a nother new plant(y/n)?")
        for plant in allPlants:
            print(plant.name)
            createTimer(plant)
    elif sf.upper() == "CLOSE":
        return
    else:
        print("Chosen Software does not match any! try again!")
        main()
main()