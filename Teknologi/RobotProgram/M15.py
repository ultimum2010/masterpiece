#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.parameters import Stop
from pybricks.tools import wait


def startprepos():
    chewie.__motor_work_L__.control.limits(1500, 4000, 35)

    chewie.__motor_work_L__.run(10000)


def endprepos():
    l_not_stalled = True

    while l_not_stalled:
        if chewie.__motor_work_L__.control.stalled():
            chewie.__motor_work_L__.stop()
            l_not_stalled = False

    chewie.__motor_work_L__.control.limits(1500, 4000, 100)
    chewie.__motor_work_L__.run_angle(120, -50)


def run1(en_Chewbacca_som_kommer_fra_utsiden):
    global chewie
    chewie = Chewbacca()
    #chewie = en_Chewbacca_som_kommer_fra_utsiden
    
    chewie.gyro.reset_angle(0)


    startprepos()

    chewie.drive_gyro_dist(200, 0, 300)
    chewie.drive_gyro_dist(100, 108, 380)

    endprepos()
    
    chewie.vri_grader(40)
    chewie.__driveBase__.stop()
    chewie.drive_gyro_dist(150, 135, 180)
    chewie.vri_grader(-50)
    chewie.drive_gyro_dist(400, 90, 100)
    chewie.drive_gyro_dist(600, 93, 400)
    chewie.drive_gyro_dist(600, 100, 55)
    chewie.drive_gyro_dist(600, 110, 750)
