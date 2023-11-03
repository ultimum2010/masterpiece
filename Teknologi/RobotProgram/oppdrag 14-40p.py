#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.parameters import Stop
from chewbacca import Direction
from pybricks.tools import wait

chewie = Chewbacca()

def dispense_publikum():
    chewie.work_motor_R(600, 150)
    chewie.work_motor_R(600, -150)
    chewie.work_motor_R(600, 150)
    chewie.work_motor_R(600, -150)
    chewie.work_motor_L(400, 375) #Gir 5 tenner bevegelse på tannstaget. x = 5 * 1/8 * 20/12 * 360
    wait(100)


def preposisonering():
    chewie.__motor_work_R__.run_until_stalled(-200, Stop.BRAKE, 30)
    chewie.__motor_work_L__.run_until_stalled(-90, Stop.BRAKE, 37)
    chewie.work_motor_L(200, 420)

#kjøring til mål
# chewie.drive_gyro_dist(100, 0, 100)
# chewie.drive_gyro_dist(200, 22, 620)

#dispensing av publikum
preposisonering()

for i in range(6):
    dispense_publikum()

chewie.work_motor_L(400, 375)