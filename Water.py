# External module imp
import RPi.GPIO as GPIO
import datetime
import time
import PlantsLinkedList
import Plant

class Water:
    
    def __init__(self, linkedList):
        self.plants = linkedList
        GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme
    
    

    def get_last_watered(self, index):
        try:
            f = open("{}_last_watered.txt".format(self.plants.findIndex(index).value.getName()), "r")
            return f.readline()
        except:
            return "NEVER!"


    # This is to get the status of the moisture sensors if setting up the system that way

    def get_status(self, pin=8):
        GPIO.setup(pin, GPIO.IN)
        return GPIO.input(pin)

    # This method makes checking if a plant needs watering easier later in the code (i.e. lines 78 & 82) by returning
    # a boolean value based on whether or not the soil is wet
    def isWet(self, pin):
        return get_status(pin) == 0


    def init_output(self, pin = 7):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        GPIO.output(pin, GPIO.HIGH)

    """
    This is for automatic watering with moisture sensors for one plant

    def auto_water(self, delay=5, pump_pin=7, water_sensor_pin=8):
        consecutive_water_count = 0
        init_output(pump_pin)
        print("Here we go! Press CTRL+C to exit")
        try:
            while 1 and consecutive_water_count < 10:
                time.sleep(delay)
                wet = get_status(pin=water_sensor_pin) == 0
                if not wet:
                    if consecutive_water_count < 5:
                        pump_on(pump_pin, 1)
                    consecutive_water_count += 1
                else:
                    consecutive_water_count = 0
        except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
            GPIO.cleanup()  # cleanup all GPI
    """

    # This method checks each plant's soil sensor and waters them if they need it
    def auto_water(self, delay=5):

        # e is assigned to the first node in the linked list
        e = self.plants.first

        # All the pump pins are initialized
        while e is not None:
            init_output(e.value.pumpPin)

        try:
            while 1:
                time.sleep(delay)

                # i is assigned to the first node in the linked list.
                i = self.plants.first

                # The program iterates through the whole linked list
                while i is not None:

                    # This variable exists to update the "Last watered" file
                    toWater = False

                    # pumpPin is declared and initialized as None value
                    pumpPin = None

                    # If the plant needs to be watered, the variable is changed and the correct pumpPin is assigned to
                    # the pumpPin variable
                    if not isWet(i.value.sensorPin):
                        toWater = True
                        pumpPin = i.value.pumpPin

                    # numSquirts (I know, gross) is set to 0
                    numSquirts = 0

                    # The plant is watered until the soil is wet or it's gotten 10 squirts.
                    while not isWet(i.value.sensorPin) and numSquirts < 10:
                        pump_on(pumpPin, 1)
                        numSquirts += 1

                        # After 5 squirts, wait 10 seconds to let the water soak in before testing the soil again
                        if numSquirts == 4:
                            time.sleep(10)

        # Stop program if CTRL+C is pressed
        except KeyboardInterrupt:
            GPIO.cleanup()



    def pump_on(self, pump_pin, delay=1):
        init_output(pump_pin)
        # f = open("last_watered.txt", "w")
        # f.write("Last watered {}".format(datetime.datetime.now()))
        # f.close()
        GPIO.output(pump_pin, GPIO.LOW)
        time.sleep(delay)
        GPIO.output(pump_pin, GPIO.HIGH)


    def updateTimeSinceWatered(self, index):
        # The name of the plant is made into a string
        nameString = str(self.plants.findIndex(index).value.getName())
        
        # If the file doesn't exist, create it
        f = open("{}_last_watered.txt".format(nameString), "a+")
        f.close()
        
        f = open("{}_last_watered.txt".format(nameString), "r+")
        fileContent = f.readlines()
        newHours = 1

        for line in fileContent:
            for i in line:
                if i.isdigit():
                    newHours += int(i)

        f.write(str(newHours))
        f.close()
        return newHours

    def resetTimeSinceWatered(self, plant):
        f = open("{}_last_watered.txt".format(plant.name), "w+")
        f.write(0)
        f.close()


    def waterPlants(self, plant):
        # moveValve(plant)
        pump_on(plant.pin, plant.seconds)
        

    # The pins connected to the relay are put into pinList
    # pinList = [2,3,4,17]

    # The pins are initialized
    # for i in pinList:
        #init_output(i)


