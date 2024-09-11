# TODO: Créer un script permettant le formattage du livre des records des JO.

country = input("De quelle nationalité est l'athlète ? ")
athlete = input("Quel est son nom ? ")
date = input("Date du record ? ")
sport = input("Dans quelle discipline ? ")
category = input("Dans une categorie specifique ? ")
record= input("Quel est le record ? ")

print("Nouveau Record :\n--------------------","\n",date,"\n",sport, "-",category,"\n",athlete, country, "-", record)