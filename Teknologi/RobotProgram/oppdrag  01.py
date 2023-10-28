#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()
#kjør til instalasjon
chewie.drive_gyro_dist (200, 25, 370)
#robbot svinger men stopper ikke.
chewie.vri_grader(200, 45)