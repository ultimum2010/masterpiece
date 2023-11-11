#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()
# Vi bruker masterprogram og derfor må vi ha neste linje for at masterprogram skal kjøre dette oppdraget
def run(chewbacca):
# Vi må bruker Chewbacca for å kunne kjøre med motorer.
    global chewie
    chewie = Chewbacca()
    # vi må bruke den "chewbacca" fra linje 10 som kommer fra masterprogram. 
    #chewie = chewbacca
 
    chewie.gyro.reset_angle(0)
    # 200 er fart, 15 er antall grader den skal snu 
    # og 750 er hvor langt den skal kjøre.  
    chewie.drive_gyro_dist(200, 15, 750)
    # på neste linje kjører den tilbake fordi det er minus i fart, så den går bakover 
    chewie.drive_gyro_dist(-400, 15, -700)
    chewie.beep()
