from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



class Chewbacca:

    WHEEL_DIAMETER = 88.5
    WHEEL_DISTANSE = 98.4

    PORT_RIGHT_MOTOR = Port.D
    PORT_LEFT_MOTOR = Port.A
    PORT_RIGHT_WORK_MOTOR = Port.C
    PORT_LEFT_WORK_MOTOR = Port.B

    RIGHT_COLOR_SENSOR = Port.S1
    LEFT_COLOR_SENSOR = Port.S3
    GYRO_SENSOR = Port.S4

    brain: EV3Brick

    motor_R: Motor
    motor_L: Motor
    motor_work_R: Motor
    motor_work_L: Motor

    drive: DriveBase

    color_R: ColorSensor
    color_L: ColorSensor
    gyro: GyroSensor


    def __init__(self) -> None:
        self.brain = EV3Brick()
        self.motor_R = Motor(self.PORT_RIGHT_MOTOR)
        self.motor_L = Motor(self.PORT_LEFT_MOTOR)
        self.motor_work_R = Motor(self.PORT_RIGHT_WORK_MOTOR)
        self.motor_work_L = Motor(self.PORT_LEFT_WORK_MOTOR)
        self.drive = DriveBase(self.motor_L, self.motor_R, self.WHEEL_DIAMETER, self.WHEEL_DISTANSE)
        self.color_R = ColorSensor(self.RIGHT_COLOR_SENSOR)
        self.color_L = ColorSensor(self.LEFT_COLOR_SENSOR)
        self.gyro = GyroSensor(self.GYRO_SENSOR)

    def beep(self):
        self.brain.speaker()