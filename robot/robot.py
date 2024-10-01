#!/usr/bin/env pybricks-micropython
# *******************IMPORTS*******************

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, GyroSensor
from pybricks.parameters import Port, Direction
from colorama import Fore, Style
from errors import PortError

# *******************ROBOT*******************

class Robot:

    """With the help of this class, programming an ev3 robot i getting easer and easer,
    cause of the fucntionalities implemented in this class.
    For example, you can se what's wrong with your cable managemnt,
    this functionality being specific to this library."""

    def __init__(self, wheelDiameter: float, axleTrack: float,
                 motors: dict,
                 sensors: dict):

        #! The sensors and motors properties can be switched while running the code
        #! We recomand you to run the init method after making a switch

        self.wheelDiameter = wheelDiameter  # ! esential constant for the robot
        self.axleTrack = axleTrack  # ! esential constant for the robot
        self.motors = motors
        self.sensors = sensors
        self.errorLog = []  # In this list, every error is stored at the verify block
        self.init()  # The verifing procces takes place

    # ***The verification and setting of a motor or of sensor to a specifc port***
    def init(self):
        # This code part is working with the seting and verifying of the motors
        try:
            for key, value in self.motors.items():
                if value is not None:
                    try:
                        setattr(self, key, value)
                    except:
                        self.errorLog.append(PortError(
                                f"{Fore.RED} Motor {Style.RESET_ALL}{Fore.BLUE}{key} {Style.RESET_ALL}{Fore.RED},
                                couldn't be initialized {Style.RESET_ALL}", "100"))
        except:
            raise LackOfInput( f"{Fore.RED} Motors couldn't be found, {Style.RESET_ALL}", "200")

        # This code part is working with the seting and verifying of the sensors
        try:
            for key, value in self.sensors.items():
                if value is not None:
                    try:
                        setattr(self, key, value)  
                    except:
                        self.errorLog.append(PortError(
                                f"{Fore.RED} Sensor {Style.RESET_ALL}{Fore.BLUE}{key}{Style.RESET_ALL}{Fore.RED},
                                couldn't be initialized {Style.RESET_ALL}", "101"))
        except:
            raise LackOfInput( f"{Fore.RED} Sensors couldn't be found, {Style.RESET_ALL}", "201")
        # Printing the error, if there are any
        if self.errorLog:
            for error in self.errorLog:
                print(error)