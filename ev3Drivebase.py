from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from errors import *

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
            
     
    def moveBySpeeds(self, degrees: int, speed1: int, speed2: int):
    
        try:
            self.leftMotor.run_angle(speed1, degrees, wait=False)  
        except: 
            raise UnknownSpeed(f"Unknown speed {speed1} or degrees {degrees}", "500")
        try:
            self.rightMotor.run_angle(speed2, degrees, wait=True) 
        except:
            raise UnknownSpeed(f"Unknown speed {speed2} or degrees {degrees}", "501")
            
    def driveBySpeeds(self, speed1: int, speed2: int):
    
        try:
            self.leftMotor.run(speed1)
        except:
            raise UnknownSpeed(f"Unknown speed {speed1}", "500")
        try:
            self.rightMotor.run(speed2)
        except:
            raise UnknownSpeed(f"Unknown speed {speed2}", "501")