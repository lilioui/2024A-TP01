# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = input("Quel est le pourcentage de la batterie du bateau :")

if 50 < float(battery_level) <= 100:
    new_battery_level = float(battery_level) - 50
    distance = float(new_battery_level) * 2 + (25 * 0.5) + (15 * 1) + (5 * 2.5) + (5 * 6)
    print (f"La distance possible est de {distance} km")
elif 25 < float(battery_level) <= 50:
    new_battery_level = float(battery_level) - 25
    distance = float(new_battery_level) * 0.5 + (15 * 1) + (5 * 2.5) + (5 * 6)
    print (f"La distance possible est de {distance} km")
elif 10 < float(battery_level) <= 25:
    new_battery_level = float(battery_level) - 10
    distance = float(new_battery_level) * 1 + (5 * 2.5) + (5 * 6) 
    print (f"La distance possible est de {distance} km")
elif 5 < float(battery_level) <= 10:
    new_battery_level = float(battery_level) - 5
    distance = float(new_battery_level) * 2.5 + (5 * 6)
    print (f"La distance possible est de {distance} km")
elif 0 < int(battery_level) <= 5:
    new_battery_level = float(battery_level) - 0
    distance = float(new_battery_level) * 6
    print (f"La distance possible est de {distance} km")
elif float(battery_level) == 0:
    distance = 0
    print (f"La distance possible est de {distance} km")
else:
    print("Le pourcentage de la batterie doit être compris entre 0 et 100")
