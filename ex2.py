# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
water_quantity = input("Quelle quantité d'eau faut-il assainir ?")

expected_filter = int(float(water_quantity)*0.2)
expected_light = int(float(water_quantity)*0.6)
expected_chlorine = float(water_quantity)*0.1

print(f" Voici les éléments requis pour assainir {water_quantity}L d'eau:\n\t- Filtre(s) : {expected_filter}\n\t- Lampe(s) UV : {expected_light}\n\t- Chlore : {expected_chlorine:.1f}kg")
