#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca

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


def run(en_Chewbacca_som_kommer_fra_utsiden):
    global chewie
    chewie = Chewbacca()
    #chewie = en_Chewbacca_som_kommer_fra_utsiden
    
    startprepos()

    chewie.drive_gyro_dist(100, 0, 110)
    chewie.vri_grader(-95)
    chewie.drive_gyro_dist(600, -95, 1300)

    endprepos()

    chewie.drive_gyro_dist(300, -110, 400)