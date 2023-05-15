from tkinter import *
import time
from datetime import date, timezone, datetime
import pytz
from datetime import datetime

heure = datetime.now()
currentTime = heure.strftime("%H:%M:%S")

fenetre = Tk()

texte_a_afficher = "Heure :" + currentTime

label = Label(fenetre, text=(texte_a_afficher) )

label.pack()

fenetre.mainloop()