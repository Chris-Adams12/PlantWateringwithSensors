########################################################################
# Chris Adams
# 07/04/22
# This file holds the plant class for use with moisture sensors
########################################################################

class Plant:

    def __init__(self, *args):

        if len(args) == 4:
            self.name = args[0]
            self.pumpPin = args[1]
            self.sensorPin = args[2]
            self.valvePos = args[3]
        elif len(args) == 3:
            self.name = args[0]
            self.pumpPin = args[1]
            self.sensorPin = args[2]
        elif len(args) == 2:
            self.name = args[0]
            self.pumpPin = args[1]
        elif len(args) == 1:
            self.name = args[0]
        else:
            print("Invalid number of parameters")


    def setName(self, name):
        self.name = name

    def setPumpPin(self, pin):
        self.pumpPin = pin

    def setSensorPin(self, pin):
        self.sensorPin = pin

    def setValvePos(self, valvePos):
        self.valvePos = valvePos

    def getName(self):
        return self.name

    def getPumpPin(self):
        return self.pumpPin

    def getSensorPin(self):
        return self.sensorPin

    def getValvePos(self):
        return self.valvePos

    def getVarList(self):
        print("name\npumpPin\nsensorPin\nvalvePos\n")