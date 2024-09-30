#!/usr/bin/env pybricks-micropython
# *******************IMPORTS*******************

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor, GyroSensor
from pybricks.parameters import Port, Direction
from colorama import Fore, Style
from errors import PortError

# *******************ROBOT*******************


class Robot:

    """With the help of this class, programming an ev3 robot i getting easier and easer,
    cause of the fucntionalities implemented in this class(at the moment, NONE)"""

    def __init__(self, wheelDiameter: float, axleTrack: float,
                 motors=None,
                 sensors=None):

        # Declaring the motors that the robot can use
        """
        lf = left
        clf = central left
        crt = central right
        rt = cental right
        """
        if motors == None:
            motors = {
                "lf": None,
                "clf": Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE),
                "crt": Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE),
                "rt": Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
            }

        # Declaring ths sensors that the robot can use
        if sensors == None:
            sensors = {
                "color1": ColorSensor(Port.S1),
                "touch": TouchSensor(Port.S2),
                "gyro": GyroSensor(Port.S3),
                "colour2": None
            }

        #! The sensors and motors can be switched
        #! We recomand you to run the verify methound after making a switch

        self.wheelDiameter = wheelDiameter #! esential constant for the robot
        self.axleTrack = axleTrack #! esential constant for the robot
        self.motors = motors
        self.sensors = sensors
        self.errorLog = [] # In this list, every error is stored at the verify block
        
        self.verify() # The verifing procces takes place

        def verify(self):
            # verifing the motors
            for key, value in motors.items():
                try:
                    setattr(self, key, value)
                except:
                    self.errorLog.append(PortError(
                            f"{Fore.RED} Motor {Style.RESET_ALL}{Fore.BLUE}{chr(i + 65)} {Style.RESET_ALL}{Fore.RED},
                            couldn't be initialized {Style.RESET_ALL}", "100"))
            
            # verifing the sensors
            for key, value in sensors.items():
                try:
                    setattr(self, key, value)  
                except:
                    self.errorLog.append(PortError(
                            f"{Fore.RED} Sensor {Style.RESET_ALL}{Fore.BLUE}{i + 1} {Style.RESET_ALL}{Fore.RED},
                            couldn't be initialized {Style.RESET_ALL}", "101"))

            # Printing the error, if there are any
            if self.errorLog:
                for error in self.errorLog:
                    print(error)