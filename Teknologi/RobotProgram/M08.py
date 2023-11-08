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

    #dytt ned sperren på kameraskinnen
    chewie.drive_gyro_dist(100, 0, 50)
    chewie.vri_grader(-100)
    chewie.drive_gyro_dist(200, -95, 100)
    chewie.drive_gyro_dist(200, -90, 300)

    endprepos()

    chewie.drive_gyro_dist(50, -88, 100)
    chewie.drive_gyro_dist(50, -90, 40)
    chewie.drive_gyro_dist(300, -90, -300)

    #hent ekspert
    chewie.vri_grader(80)
    chewie.drive_gyro_dist(200, -60 ,100)