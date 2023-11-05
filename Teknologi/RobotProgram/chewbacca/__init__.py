from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Direction:
    LEFT = 0
    RIGHT = 1

class Chewbacca:
    LEFT = 0
    RIGHT = 1

    WHEEL_DIAMETER = 88.5
    WHEEL_DISTANSE = 98.4

    PORT_RIGHT_MOTOR = Port.D
    PORT_LEFT_MOTOR = Port.A
    PORT_RIGHT_WORK_MOTOR = Port.B
    PORT_LEFT_WORK_MOTOR = Port.C

    RIGHT_COLOR_SENSOR = Port.S1
    LEFT_COLOR_SENSOR = Port.S3
    GYRO_SENSOR = Port.S4

    


    def __init__(self) -> None:
        self.brain = EV3Brick()
        self.motor_R = Motor(self.PORT_RIGHT_MOTOR)
        self.motor_L = Motor(self.PORT_LEFT_MOTOR)
        self.__motor_work_R__ = Motor(self.PORT_RIGHT_WORK_MOTOR)
        self.__motor_work_L__ = Motor(self.PORT_LEFT_WORK_MOTOR)
        self.__driveBase__ = DriveBase(self.motor_L, self.motor_R, self.WHEEL_DIAMETER, self.WHEEL_DISTANSE)
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
        self.__driveBase__.reset()

        rygger = False
        if speed < 0:
            rygger = True
            speed = -1 * speed

        if target_distance < 0:
            rygger = True
            target_distance = -1 * target_distance

        if not rygger:
            #kjøres når du ikke rygger
            while not reached_goal:
                gyrovinkel = self.gyro.angle()
                svinge_hastighet = gyrovinkel - target_angle
                self.__driveBase__.drive(speed, svinge_hastighet)

                distance = self.__driveBase__.distance()
                reached_goal = distance >= target_distance

        else:
            #kjøres når du rygger
            while not reached_goal:
                gyrovinkel = self.gyro.angle()
                svinge_hastighet = gyrovinkel - target_angle
                self.__driveBase__.drive(speed * -1, svinge_hastighet)

                distance = self.__driveBase__.distance()
                reached_goal = distance <= target_distance * -1


        self.__driveBase__.stop()


    def line_follower(self, fargesensor: ColorSensor, driveBase: DriveBase, speed, kP, distance):
        while True:
            svart_hvit = 55
            lysstyrke = fargesensor.reflection()
            retning =  self.p_ctrl(svart_hvit, lysstyrke, kP)
            driveBase.drive(speed, retning)



    def work_motor_L(self, speed, target_rotation):
    
        self.__motor_work_L__.run_angle(speed, target_rotation)

    def work_motor_R(self,  speed, target_rotation):

        self.__motor_work_R__.run_angle(speed, target_rotation)

    def TestAvSide(self, side):
        if side == "right":
            print("rett")

        elif side == "left":
            print("galt")

        else:
            print("skjønte ikke hva du mente")

    def vri_grader(self, target_angle):
        self.__driveBase__.turn(target_angle)

    def straight(self, distance):
            self.__driveBase__.straight(distance)

    def gyro_svimmel(self):
        vinkelhastighet = self.gyro.speed()

        vinkelhastighet = abs(vinkelhastighet)

        if vinkelhastighet <= 1:
            self.brain.light.on(Color.GREEN)

        else:
            self.brain.light.on(Color.RED)

