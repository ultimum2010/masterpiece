#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from pybricks.tools import wait
from pybricks.parameters import Button

import M14_40p
import M07

chewie = Chewbacca()

# init konstanter her
PROGNR_MAX = 9
PROGNR_MIN = -2

# init variabler her
prognr = 0

while True:

    #oppdater skjerm
    if prognr == -2:
        chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/farge.png")
    elif prognr == -1:
        chewie.brain.screen.load_image("/home/robot/RobotProgram/chewbacca/menybilder/gyro.png")
    elif prognr == 0:
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

    #sjekker om opp er trykt
    if Button.RIGHT in knapp_verdi:
        prognr = prognr + 1

    else:
        #sjekker om ned er trykt
        if Button.LEFT in knapp_verdi:
            prognr = prognr - 1

        else:
            #sjekker om midten er trykt
            if Button.CENTER in knapp_verdi:
                if prognr == -2:
                    pass
                elif prognr == -1:
                    pass
                elif prognr == 0:
                    pass
                elif prognr == 1:
                    M07.run(chewie)
                elif prognr == 2:
                    M14_40p.run(chewie)
                elif prognr == 3:
                    pass
                elif prognr == 4:
                    pass
                elif prognr == 5:
                    pass
                elif prognr == 6:
                    pass
                elif prognr == 7:
                    pass
                elif prognr == 8:
                    pass
                elif prognr == 9:
                    pass
                prognr = prognr + 1

    #ikke la prognr bli større enn max eller mindre en min
    prognr = min(PROGNR_MAX, prognr)
    prognr = max(PROGNR_MIN, prognr)

    #vent til knapp er ute
    while chewie.brain.buttons.pressed() != []:
        #sitt fast her til ingen knapper er trykt
        pass #Ingen ting å gjøre. Best å vente litt til.