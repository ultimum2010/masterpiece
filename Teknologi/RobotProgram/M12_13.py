#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.tools import wait

def run(en_Chewbacca_som_kommer_fra_utsiden):
    #chewie = Chewbacca()
    chewie = en_Chewbacca_som_kommer_fra_utsiden
    
    wait(500)
    chewie.gyro.reset_angle(0)
    chewie.motor_R.run_angle(70, 130)
    chewie.drive_gyro_dist(100, 50, 350)