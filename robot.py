#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

class PortError(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class LackOfInput(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnknownOrientation(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"
        
class UnknownSpeed(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class UnknownStopMethod(Exception):
    def __init__(self, message: str, errorCode: str):
        self.message = message
        self.errorCode = errorCode
        super().__init__(message)

    def __str__(self):
        return f"{self.message} (Error Code: {self.errorCode})"

class Ev3DriveBase(DriveBase):
    def __init__(self, leftMotor: Motor, rightMotor: Motor, wheelDiameter: float, axleTrack: float):
        super().__init__(leftMotor, rightMotor, wheelDiameter, axleTrack)
        self.leftMotor = leftMotor
        self.rightMotor = rightMotor
        
    def move(self, orientation: str, degrees: int):
        if orientation == "forward":
            self.straight(degrees)
        elif orientation == "backward":
            self.straight(-degrees)
        else:
            raise UnknownOrientation(f"{orientation} is not a valid orientation", "300")
    
    def moveToOrientation(self, orientation: int):
        try:
            self.turn(orientation)
        except:
            raise UnknownOrientation(f"{orientation} is not a valid orientation", "300")
        
    def startMoving(self, speed: int, orientation: int):
        try: 
            orientation = int(orientation)
        except:
            raise UnknownOrientation(f"{orientation} is not a valid orientation", "300")
        try:
            speed = int(speed)
        except:
            raise UnknownSpeed(f"{speed} is not a valid speed", "301")
            
        self.drive(speed, orientation)

    def setMovementMotorsTo(self, stopOrStall: str):
        try:
            if stopOrStall == "stop":
                self.leftMotor.stop()
                self.rightMotor.stop()
            elif stopOrStall == "hold":
                self.leftMotor.hold()
                self.rightMotor.hold()
            else:
                raise UnknownStopMethod(f"{stopOrStall} is not a valid stop method", "302")
        except:
            raise UnknownStopMethod(f"Error in stopping or holding motors", "302")

    """    
    def moveBySpeeds(self, degrees: int, speed1: int, speed2: int):
        def runLeftMotor():
            self.leftMotor.run_angle(degrees, speed1)
    
        def runRightMotor():
            self.rightMotor.run_angle(degrees, speed2)
    
        leftThread = _thread.start_new_thread(runLeftMotor, ())
        rightThread = _thread.start_new_thread(runRightMotor, ())

    def driveBySpeeds(self, speed1: int, speed2: int):
        def runLeftMotor():
            self.leftMotor.run(degrees, speed1)
    
        def runRightMotor():
            self.rightMotor.run(degrees, speed2)
    
        leftThread = _thread.start_new_thread(runLeftMotor, ())
        rightThread = _thread.start_new_thread(runRightMotor, ())
    """
        
class Robot:
    def __init__(self, wheelDiameter: int, axleTrack: int, motors: dict, sensors: dict, driveBaseName: str):
        self.wheelDiameter = float(wheelDiameter)
        self.axleTrack = float(axleTrack)
        self.motors = motors
        self.sensors = sensors
        self.driveBaseName = driveBaseName
        self.errorLog = []
        self.init()

    def init(self):
        try:
            for key, value in self.motors.items():
                if value is not None:
                    try:
                        setattr(self, key, value)
                    except:
                        self.errorLog.append(PortError(f"Motor {key} couldn't be initialized", "100"))
        except:
            raise LackOfInput("Motors couldn't be found", "200")

        try:
            for key, value in self.sensors.items():
                if value is not None:
                    try:
                        setattr(self, key, value)
                    except:
                        self.errorLog.append(PortError(f"Sensor {key} couldn't be initialized", "101"))
        except:
            raise LackOfInput("Sensors couldn't be found", "201")

        if self.errorLog:
            for error in self.errorLog:
                print(error)
            raise self.errorLog[0]

    def declareDriveBase(self, leftMotor: Motor, rightMotor: Motor,
                         straightSpeed=100, straightAcceleration=100, turnRate=100, turnAcceleration=100):
        setattr(self, self.driveBaseName, Ev3DriveBase(leftMotor, rightMotor, self.wheelDiameter, self.axleTrack))
        self.drivebase = getattr(self, self.driveBaseName)
        self.drivebase.settings(straightSpeed, straightAcceleration, turnRate, turnAcceleration)

motors = {
    'leftMotor': Motor(Port.A, Direction.CLOCKWISE),
    'rightMotor': Motor(Port.B, Direction.CLOCKWISE),
    'mediumMotor': Motor(Port.C, Direction.CLOCKWISE),
}

sensors = {
    'colorSensor': ColorSensor(Port.S1),
    'ultrasonicSensor': UltrasonicSensor(Port.S2),
    'gyroSensor': GyroSensor(Port.S3),
}

robot = Robot(56, 152, motors, sensors, "d")
robot.declareDriveBase(robot.leftMotor, robot.rightMotor)
