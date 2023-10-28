#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()

#kjøring til vendepongt
chewie.drive_gyro_dist(200, 20, 750)
#Vi prøver å få roboten til å gå tilbake, men den vil ikke gjøre det. 
#vi hører beepet:)  
chewie.drive_gyro_dist(-600, 20, -750)
chewie.beep()