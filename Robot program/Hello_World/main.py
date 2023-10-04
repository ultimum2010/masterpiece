#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
chewie = EV3Brick()
driveH = Motor(Port.D)
driveV = Motor(Port.A)
kjor = DriveBase(driveV, driveH, 88.5, 98.4)
gyro = GyroSensor(Port.S4)
#avansert = track_target()


# Write your program here.
#kjor.settings(200, 200, 90, 180)

#kjor.straight(30)
#kjor.turn(90)

#chewie.screen.draw_text(1, 1, a, text_color=Color.BLACK, background_color=None)

ØNSKET_RETNING = -90

for x in range(100):
    gyrovinkel = gyro.angle()
    svinge_hastighet = gyrovinkel - ØNSKET_RETNING
    kjor.drive(150, svinge_hastighet)
    chewie.screen.draw_text(10, 10, x, text_color=Color.BLACK, background_color=Color.WHITE)
    wait(100)
kjor.stop()
wait(1000)
chewie.speaker.beep(1000, 1000)
#chewie.screen.print("hello world")