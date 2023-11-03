#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.parameters import Stop
from chewbacca import Direction

chewie = Chewbacca()

chewie.__motor_work_L__.run_until_stalled(360, Stop.BRAKE, 25)

chewie.brain.speaker.beep(500, 200)