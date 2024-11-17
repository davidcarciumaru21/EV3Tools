#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Color
import time

###### Codul Erorilor ######

class MotorInitializationError(Exception):
    def __init__(self, motorName: str):
        message = f"Motor '{motorName}' failed to initialize. Ensure the motor is properly connected."
        super().__init__(message)

class SensorInitializationError(Exception):
    def __init__(self, sensorName: str):
        message = f"Sensor '{sensorName}' failed to initialize. Ensure the sensor is properly connected."
        super().__init__(message)

class InvalidOrientationError(Exception):
    def __init__(self, orientation: str):
        message = f"Invalid orientation '{orientation}'. Use 'forward' or 'backward'."
        super().__init__(message)

class InvalidSpeedError(Exception):
    def __init__(self, speed: str):
        message = f"Invalid speed '{speed}'. Ensure the speed is a valid integer."
        super().__init__(message)

class InvalidStopMethodError(Exception):
    def __init__(self, method: str):
        message = f"Invalid stop method '{method}'. Use 'stop' or 'hold'."
        super().__init__(message)

class DisplayError(Exception):
    def __init__(self, x: int, y: int, text: str):
        message = f"Unable to display '{text}' at position ({x}, {y}). Check the screen and parameters."
        super().__init__(message)

class InvalidDurationError(Exception):
    def __init__(self, duration: str):
        message = f"Invalid duration '{duration}'. Duration should be a positive number."
        super().__init__(message)

###### Codul pentru functionare robotulu ######

class Ev3DriveBase(DriveBase):
    """facem aceasta clasa pentru a adauga functionalitati drivebaseu-lui obiectului robot"""
    def __init__(self, leftMotor: Motor, rightMotor: Motor, wheelDiameter: float, axleTrack: float, errorLog):
        super().__init__(leftMotor, rightMotor, wheelDiameter, axleTrack)
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        self.errorLog = errorLog

    def move(self, orientation: str, degrees: int):
        try:
            if orientation == "forward":
                self.straight(degrees)
            elif orientation == "backward":
                self.straight(-degrees)
            else:
                raise InvalidOrientationError(orientation)
        except Exception as e:
            self.errorLog.append(e)

    def moveToOrientation(self, orientation: int):
        try:
            self.turn(orientation)
        except:
            self.errorLog.append(InvalidOrientationError(orientation))

    def startMoving(self, speed: int, orientation: int):
        try:
            self.drive(int(speed), int(orientation))
        except Exception as e:
            self.errorLog.append(e)

    def setMovementMotorsTo(self, stopOrStall: str):
        try:
            if stopOrStall == "stop":
                self.leftMotor.stop()
                self.rightMotor.stop()
            elif stopOrStall == "hold":
                self.leftMotor.hold()
                self.rightMotor.hold()
            else:
                raise InvalidStopMethodError(stopOrStall)
        except Exception as e:
            self.errorLog.append(e)

    def moveBySpeeds(self, degrees: int, speed1: int, speed2: int):
        try:
            self.leftMotor.run_angle(speed1, degrees, wait=False)
            self.rightMotor.run_angle(speed2, degrees, wait=True)
        except:
            self.errorLog.append(InvalidSpeedError(f"Left motor speed '{speed1}' or right motor speed '{speed2}' caused an error."))

    def driveBySpeeds(self, speed1: int, speed2: int):
        try:
            self.leftMotor.run(speed1)
            self.rightMotor.run(speed2)
        except:
            self.errorLog.append(InvalidSpeedError(f"Speeds '{speed1}' or '{speed2}' caused an error."))


class Robot:
    def __init__(self, wheelDiameter: int, axleTrack: int, motors: dict, sensors: dict, driveBaseName: str):
        # Pentru a se crea un obiect robot avem envoie de un dictionar cu motoare si unul cu senzori plus numele drivebaseului si anumite lungimi
        self.wheelDiameter = float(wheelDiameter)
        self.axleTrack = float(axleTrack)
        self.motors = motors
        self.sensors = sensors
        self.driveBaseName = driveBaseName
        self.errorLog = []
        self.ev3 = EV3Brick()
        self.ev3.screen.clear()
        self.init()

    def init(self):
        # Se atribuie fiecarui nume de motor portul pe care se alfa un anumit motor specificat
        for key, motor in self.motors.items():
            try:
                setattr(self, key, motor)
            except:
                self.errorLog.append(MotorInitializationError(key))
        for key, sensor in self.sensors.items():
            try:
                setattr(self, key, sensor)
            except:
                self.errorLog.append(SensorInitializationError(key))

        if self.errorLog:
            for i in self.errorLog:
                print(i)
                
            # Daca exista mai multe erori o va ridica mereu pe prima
            raise self.errorLog[0]

    def declareDriveBase(self, leftMotor: Motor, rightMotor: Motor, straightSpeed=100, straightAcceleration=100, turnRate=100, turnAcceleration=100):
        # Facem obiectul drivebase ce corespunde obiecului robot
        self.drivebase = Ev3DriveBase(leftMotor, rightMotor, self.wheelDiameter, self.axleTrack, self.errorLog)
        self.drivebase.settings(straightSpeed, straightAcceleration, turnRate, turnAcceleration)

    def displayText(self, x: int, y: int, text: str, color: object, backgroundColor = None):
        try:
            self.ev3.screen.draw_text(x, y, text, color, backgroundColor)
        except:
            self.errorLog.append(DisplayError(x, y, text))

    def writeText(self, x: int, y: int, text: str, color: object, t: float, backgroundColor = None):
        try:
            self.ev3.screen.draw_text(x, y, text, color, backgroundColor)
            time.sleep(t)
        except:
            self.errorLog.append(DisplayError(x, y, text))
        self.ev3.screen.clear()

    def clearScreen(self):
        self.ev3.screen.clear()

    def turnOnLights(self, color: object):
        try:
            self.ev3.light.on(color)
        except:
            self.errorLog.append(DisplayError(None, None, f"Failed to turn on light with color {color}"))

    def turnOffLights(self):
        try:
            self.ev3.light.off()
        except:
            self.errorLog.append(DisplayError(None, None, "Failed to turn off light"))