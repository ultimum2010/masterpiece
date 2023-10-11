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

    global brain#: EV3Brick

    global motor_R#: Motor
    global motor_L#: Motor
    global motor_work_R#: Motor
    global motor_work_L#: Motor

    global drive#: DriveBase

    global color_R#: ColorSensor
    global color_L#: ColorSensor
    global gyro#: GyroSensor


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
        self.brain.speaker.beep()
        wait(1000)



    def trippteller(self):
        Trippteller = self.motor_R + self.motor_L / 2
        return Trippteller



    def p_ctrl(self, target, current, kP):
        error = target - current
        controlSignal = kP * error

        return controlSignal




    def line_follower(self, fargesensor: ColorSensor, driveBase: DriveBase, speed, kP, distance):
        while True:
            svart_hvit = 55
            lysstyrke = fargesensor.reflection()
            retning =  self.p_ctrl(svart_hvit, lysstyrke, kP)
            driveBase.drive(speed, retning)

    

