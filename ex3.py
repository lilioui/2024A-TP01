# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

import math

speed = float(input("Quelle est la vitesse initiale (en m/s):"))
angle = float(input("Quel est l'angle du lancé (en degrés):"))
g = 9.81

distance = ((speed)**2) * (math.sin(math.radians(2*(angle)))) / g

print(round(distance, 2))