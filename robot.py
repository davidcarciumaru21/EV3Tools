from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.parameters import Color
from errors import *
from ev3Drivebase import *
import time
        
class Robot:
    def __init__(self, wheelDiameter: int, axleTrack: int, motors: dict, sensors: dict, driveBaseName: str):
        self.wheelDiameter = float(wheelDiameter)
        self.axleTrack = float(axleTrack)
        self.motors = motors
        self.sensors = sensors
        self.driveBaseName = driveBaseName
        self.errorLog = []
        self.init()
        self.ev3 = EV3Brick()  
        self.ev3.screen.clear()

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
        
    """
    def displayFace(self, face: object, displayTime: float):
        try:
            self.ev3.screen.load_image(face) 
        except:
            raise UnknownFace(f"{face} is not a valid face to display", "400")
        try:
            time.sleep(displayTime) 
        except:
            raise UnknownTimeArgument(f"{displayTime} is not a valid time to sleep", "401")
        self.ev3.screen.clear() 
        
    def displayFaceForever(self, face: object):
        try:
            self.ev3.screen.load_image(face) 
        except:
            raise UnknownFace(f"{face} is not a valid face to display", "400")

    """

    def displayText(self, x: int, y: int, text: str, color: object, backgroundColor = None):
        try:
            self.ev3.screen.draw_text(x, y, text, color, backgroundColor)
        except:
            raise UnableToWriteText(f"Unable to display {text}, it could be an error also from x: {x}, y: {y}, color: {color} or background color: {backgroundColor}", "402")
        
    def writeText(self, x: int, y: int, text: str, color: object, t: float, backgroundColor = None):
        try:
            self.ev3.screen.draw_text(x, y, text, color, backgroundColor)
        except:
            raise UnableToWriteText(f"Unable to display {text}, it could be an error also from x: {x}, y: {y}, color: {color}or background color: {backgroundColor}", "402")
        try:
            time.sleep(t)
        except:
            raise UnknownTimeArgument(f"{t} is not a valid time to sleep", "401")
        self.ev3.screen.clear()
    
    def clearScreen(self):
        self.ev3.screen.clear()
        
    def turnOnlights(self, color: object):
        self.ev3.light.on(color)
    
    def turnOffLights(self):
        self.ev3.light.off()