from datetime import *

class PlantColection:
    def __init__(self):
        self.plants = []

    def __iter__(self):
        return iter(self.plants)

    def add_plants(self, plants):
        self.plants.append(plants)

    def __getitem__(self, index):
        return self.plants[index]

class Plant:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __iter__(self):
        return iter([self.name, self.time])

def createplant():
    print("Create a new Plant:")
    name = input("Enter name for your Plant: ")
    print("Time for the notification")
    time = int(input("Enter when to water your plant (min):"))

    return Plant(name=name,time=time)
