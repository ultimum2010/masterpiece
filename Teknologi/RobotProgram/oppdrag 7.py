#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()

#kjøring til vendepongt
chewie.drive_gyro_dist(100, 10, 700)