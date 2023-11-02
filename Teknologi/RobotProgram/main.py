#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.tools import wait

chewie = Chewbacca()

# init variabler her
prognr = 4


#oppdater skjerm
if prognr == 0:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/0.png")
elif prognr == 1:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/1.png")
elif prognr == 2:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/2.png")
elif prognr == 3:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/3.png")
elif prognr == 4:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/4.png")
elif prognr == 5:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/5.png")
elif prognr == 6:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/6.png")
elif prognr == 7:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/7.png")
elif prognr == 8:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/8.png")
elif prognr == 9:
    chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/9.png")


#les knapper
knapp_er_trykt = False
while not knapp_er_trykt:
    knapp_verdi = chewie.brain.buttons.pressed() 

    #er alle knapper ute
    if knapp_verdi:
        knapp_er_trykt = True