import time
from datetime import date, timezone, datetime
import pytz
from datetime import datetime

while True :
    heure = datetime.now()
    currentTime = heure.strftime("%H:%M:%S")
    print("Heure :", currentTime)
    print("Date :", date.today())

    argent = 3  # voir avec la classe argent pour metre en lien
    print("votre argent est de :", argent, "€\n")

    print("Appuyez sur b pour rentrer dans la boutique.")
    print("Appuyez sur i pour rentrer dans votre inventaire.")
    print("Appuyez sur m pour accéder au menu des monstres.")
    print("Appuyez sur q pour quitter.")

while True :
    choix_menu = input ()
    if choix_menu == 'b':



