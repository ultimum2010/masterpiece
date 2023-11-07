#!/usr/bin/env pybricks-micropython
from chewbacca import Chewbacca
from chewbacca import Direction

chewie = Chewbacca()
# Når vi skulle fordele oppgaver i laget, så var det noen som fant ut av hvordan roboten skulle kjøre
#  og noen andre fant ut hva roboten skulle gjøre. 
# I dette programmet ønsker vi at roboten skal kjøre frem til M07 og tilbake. 
# Vi bruker masterprogram og derfor må vi ha neste linje for at masterprogram skal kjøre dette oppdraget
def run(chewbacca):
#  Noen på laget skrev Chewbacca som er et program som vet hvordan den skal styre motorer. 
# Vi må bruker Chewbacca for å kunne kjøre med motorer.
    global chewie
    chewie = Chewbacca()
    # Hvordan bruker vi Chewbacca?
    # vi må bruke den "chewbacca" fra linje 10 som kommer fra masterprogram. 
    # Vi må lage noe som peker på "chewbacca" koden, og det er "chewie". "chewie" er en variabel
    #chewie = chewbacca

    chewie.gyro.reset_angle(0)
    #kjøring til vendepunkt
    # Chewbacca vet hvordan man skal kjøre med gyro
    # Vi får chewbacca til å kjøre til vendepunktet ved at vi forteller hvor fort, hvor langt 
    # og hvor mange grader den skal kjøre. 200 er fart, 15 er antall grader den skal snu 
    # og 750 er hvor langt den skal kjøre. 
    # hold musepeker over drive_gyro_dist så får du opp svaret. 
    chewie.drive_gyro_dist(200, 15, 750)
    # på neste linje kjører den tilbake fordi det er minus i fart, så den går bakover 
    chewie.drive_gyro_dist(-400, 15, -700)
    chewie.beep()