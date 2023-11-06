#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.tools import wait



def run(en_Chewbacca_som_kommer_fra_utsiden):
    chewie = Chewbacca()
    #chewie = en_Chewbacca_som_kommer_fra_utsiden
    
    # de neste 3 linjene gjør slik at roboten kjører til installasjonen
    chewie.gyro.reset_angle(0)
    chewie.motor_R.run_angle(70, 130)
    chewie.drive_gyro_dist(100, 50, 470)
    # her måtte det programmeres slik at tannhjulet treffer med sikkerhet
    chewie.motor_L.run_angle(40, 70)
    # nå skal roboten kjøre tannhjulet rundt ved bruk av høyre motor
    chewie.__motor_work_R__.run_angle(1500, 2000)
    chewie.drive_gyro_dist(-150, 50, -250)
    chewie.drive_gyro_dist(-200, 90, -300)