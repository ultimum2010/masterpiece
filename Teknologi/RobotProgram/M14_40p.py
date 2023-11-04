#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.parameters import Stop
from chewbacca import Direction
from pybricks.tools import wait

chewie = Chewbacca()

def dispense_publikum():
    chewie.work_motor_L(1500, 375) #Gir 5 tenner bevegelse på tannstaget. x = 5 * 1/8 * 20/12 * 360
    chewie.work_motor_R(1500, -110)
    chewie.work_motor_R(1500, 110)
    wait(100)

def dispense_publikum_fort():
    chewie.work_motor_L(1500, 2625)
    chewie.work_motor_R(1500, -110)
    chewie.work_motor_R(1500, 110)
    wait(100)

def startPrepos():
    chewie.__motor_work_L__.control.limits(1500, 4000, 30)
    chewie.__motor_work_R__.control.limits(1500, 4000, 30)

    chewie.__motor_work_L__.run(-1500)
    chewie.__motor_work_R__.run(1500)


def endPrepos():
    l_not_stalled = True
    r_not_stalled = True

    while l_not_stalled or r_not_stalled:
        if chewie.__motor_work_L__.control.stalled():
            chewie.__motor_work_L__.stop()
            l_not_stalled = False

        if chewie.__motor_work_R__.control.stalled():
            chewie.__motor_work_R__.stop()
            r_not_stalled = False

    chewie.__motor_work_L__.control.limits(1500, 4000, 100)
    chewie.__motor_work_R__.control.limits(1500, 4000, 100)

    chewie.__motor_work_L__.run_angle(1500, 315)
    chewie.__motor_work_R__.run_angle(1500, -40)


def run(chewbacca):
    global chewie
    chewie = Chewbacca()
    #chewie = chewbacca

    chewie.gyro.reset_angle(0)

    startPrepos() 
    #kjøring til mål
    chewie.drive_gyro_dist(100, 0, 100)
    chewie.drive_gyro_dist(200, 20, 620)
    endPrepos()

    #dispensing av publikum
    for i in range(1):
        dispense_publikum_fort()
    wait(500)

    chewie.__motor_work_R__.stop()

    chewie.__motor_work_L__.run_angle(-1500, 800)

    chewie.drive_gyro_dist(-200, 15, -645)

    chewie.__driveBase__.stop()
    chewie.__motor_work_L__.stop()
