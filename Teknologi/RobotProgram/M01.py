#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction


def run(chewbacca):
    global chewie
    chewie = Chewbacca()
    #chewie = chewbacca

    chewie = Chewbacca()
    #kjør til instalasjon
    chewie.drive_gyro_dist (200, 40, 410)
    #robbot svinger men stopper ikke.
    chewie.vri_grader(60)