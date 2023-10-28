#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()

#kjøring til mål
chewie.drive_gyro_dist(100, 0, 100)
chewie.drive_gyro_dist(100, 22, 620)

#dispensing av publikum
chewie.work_motor_L(70, 700)
chewie.work_motor_R(30, 100)
chewie.work_motor_R(30, -100)