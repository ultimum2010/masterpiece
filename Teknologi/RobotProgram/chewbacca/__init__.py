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

    


    def __init__(self) -> None:
        self.brain = EV3Brick()
        self.motor_R = Motor(self.PORT_RIGHT_MOTOR)
        self.motor_L = Motor(self.PORT_LEFT_MOTOR)
        self.motor_work_R = Motor(self.PORT_RIGHT_WORK_MOTOR)
        self.motor_work_L = Motor(self.PORT_LEFT_WORK_MOTOR)
        self.driveBase = DriveBase(self.motor_L, self.motor_R, self.WHEEL_DIAMETER, self.WHEEL_DISTANSE)
        self.color_R = ColorSensor(self.RIGHT_COLOR_SENSOR)
        self.color_L = ColorSensor(self.LEFT_COLOR_SENSOR)
        self.gyro = GyroSensor(self.GYRO_SENSOR)


    def trippteller(self):
        Trippteller = self.motor_R + self.motor_L / 2
        return Trippteller



    def p_ctrl(self, target, current, kP):
        error = target - current
        controlSignal = kP * error

        return controlSignal

    def beep(self):
        self.brain.speaker.beep()
        wait(1000)


    def drive_gyro_dist(self, speed, target_angle, target_distance):
        reached_goal = False
        self.driveBase.reset()

        while not reached_goal:
            gyrovinkel = self.gyro.angle()
            svinge_hastighet = self.p_ctrl(target_angle, gyrovinkel, 1)
            self.driveBase.drive(speed, svinge_hastighet)

            distance = self.driveBase.distance()
            reached_goal = distance >= target_distance

        self.driveBase.stop()


    def line_follower(self, fargesensor: ColorSensor, driveBase: DriveBase, speed, kP, distance):
        while True:
            svart_hvit = 55
            lysstyrke = fargesensor.reflection()
            retning =  self.p_ctrl(svart_hvit, lysstyrke, kP)
            driveBase.drive(speed, retning)

    

