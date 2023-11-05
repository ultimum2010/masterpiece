#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.parameters import Port, Stop, Direction, Button, Color



def run(en_Chewbacca_som_kommer_fra_utsiden):
    global chewie
    chewie = Chewbacca()
    #chewie = en_Chewbacca_som_kommer_fra_utsiden
    
    chewie.gyro.reset_angle(0)

    gamle_limits_R = chewie.motor_R.control.limits()
    gamle_limits_L = chewie.motor_L.control.limits()
    chewie.motor_R.control.limits(800, 625, 100)
    chewie.motor_L.control.limits(800, 625, 100)

    chewie.drive_gyro_dist(100, 0, 100)

    chewie.motor_L.hold()
    #chewie.motor_R.run_angle(10000, 180, then = Stop.COAST)

    while chewie.gyro.angle() < 65:
        chewie.motor_R.run(1000)
    
    chewie.motor_R.stop()

    chewie.drive_gyro_dist(400, 100, 625)

    chewie.motor_R.hold()

    while chewie.gyro.angle() > 15:
        chewie.motor_L.run(350)

    chewie.motor_L.stop()

    chewie.drive_gyro_dist(200, 0, 300, False)
    chewie.drive_gyro_dist(100, 20, 350)

    chewie.motor_R.control.limits(gamle_limits_R[0], gamle_limits_R[1], gamle_limits_R[2])
    chewie.motor_L.control.limits(gamle_limits_L[0], gamle_limits_L[1], gamle_limits_L[2])