from joueur import Joueur
from item import Item
from monstre import Monstre
joueur_test = Joueur("Louis", 0, 1, 0, 0, 0)

joueur_test.print_nom_monstre()

salameche = Monstre("Salameche", 10, "Attaque", "images/Salameche.png")
bulbizarre = Monstre("Bulbizarre", 10, "Defense", "images/Bulbizarre.png")

joueur_test.ajouter_monstre(salameche)

print(salameche.get_stats())
print(bulbizarre.get_stats())

epee = Item(1, "epee")
bouclier = Item(1, "bouclier")
soupe = Item(1, "soupe")
bottes = Item(1, "bottes")
bottes2 = Item(2, "bottes")
bottes3 = Item(4, "bottes")

joueur_test.ajouter_item(epee)
joueur_test.ajouter_item(bouclier)
joueur_test.ajouter_item(soupe)
joueur_test.ajouter_item(bottes)
joueur_test.ajouter_item(bottes2)
joueur_test.ajouter_item(bottes3)


joueur_test.tout_sauvegarder()