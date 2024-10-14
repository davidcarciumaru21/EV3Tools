#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Direction
from errors import *
from ev3Drivebase import *
from robot import *

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
robot.move("forward", 100)
robot.move("backward", 100)
robot.moveToOrientation(90)
robot.startMoving(100, 100)
robot.setMovementMotorsTo("hold")
robot.setMovementMotorsTo("stop")
robot.moveBySpeeds(100, 100, 100)
robot.driveBySpeeds(100, 100)