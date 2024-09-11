# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ?"))

n_filter = water_quantity * 0.2
n_light = water_quantity * 0.6
kg_chlorine = water_quantity * 0.1 

print(f"Voici les matériaux requis pour l'assainissement de {water_quantity}L d'eau:\n", "-", n_filter, "filtres" ,"\n","-", n_light, "lampes UV" ,"\n","-", kg_chlorine,"kg de chlorine")
