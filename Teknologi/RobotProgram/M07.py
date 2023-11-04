#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()

def run(chewbacca):
    global chewie
    chewie = Chewbacca()
    #chewie = chewbacca

    chewie.gyro.reset_angle(0)
    #kjøring til vendepongt
    chewie.drive_gyro_dist(200, 15, 750)
    #vi hører beepet:)  
    chewie.drive_gyro_dist(-400, 15, -700)
    chewie.beep()