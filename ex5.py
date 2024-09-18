#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

gold = code_medals.count('G')
silver = code_medals.count('S')
bronze = code_medals.count('B')

if len(code_medals) != gold + silver + bronze :
    print("Ceci est une chaine invalide.")
else :
    print(f"{country}:\n- {gold} Or\n- {silver} Argent\n- {bronze} Bronze") 
