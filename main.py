########################################################################
# Chris Adams
# 04/01/22
# This file demos the PlantsLinkedList
########################################################################

import PlantsLinkedList
import Plant
import Water
import WaterQueue
from datetime import datetime, timedelta
import schedule
import time
import sendText

plantsList = PlantsLinkedList.LinkedList()
water = Water.Water(plantsList)


# Gets the information for a new plant and enters it into plantsList
def addPlant():

    print("Enter the name of the plant: ")
    plant = Plant.Plant(input())

    print("What pin is the pump connected to for this ", plant.getName(), "?: ")
    plant.setPumpPin(input())

    print("What pin is the soil sensor connected to for this ", plant.getName(), "?: ")
    plant.setSensorPin(input())

    print("What valve setting is this ", plant.getName(), " at? If not applicable, type 'na'")
    if input == "na":
        print("\nNo valve setting being used\n")
    else:
        plant.setValvePos(input())

    # The new plant is added to plantsList
    plantsList.add(plant)
    
    print("{} Added!".format(plant.getName()))
    
    water.resetTimeSinceWatered(plant)


# For adding a plant with all the variables already known with valve
def addPlant(name, pumpPin, sensorPin, valvePos):
    plant = Plant.Plant(name, pumpPin, sensorPin, valvePos)
    plantsList.add(plant)
    print("{} Added!".format(plant.getName()))

# For adding a plant with all the variables already known without valve
def addPlant(name, pumpPin, sensorPin):
    plant = Plant.Plant(name, pumpPin, sensorPin)
    plantsList.add(plant)
    print("{} Added!".format(plant.getName()))



# The text files with the time since the last watering are updated
# and the required plants are queued to be watered
def updateTimeSheets():
    i=0
    while i != plantsList.count():
        numHours = water.updateTimeSinceWatered(i)



def waterPlants():
    water.auto_water()


def runProgram():

    updateTimeSheets()
    # waterPlants()
    sendText()



# Testing
#Commands at start of testing
#plantsList.list()
#print("list printed")

addPlant("Rose", 15, 5, 2)

plantsList.list()
print("list printed")



runProgram()


print(water.get_last_watered(0))


if plantsList.findName("Rose"):
    print("Found Rose")

print(plantsList.findName("Rose").value.getName())
