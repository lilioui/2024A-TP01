#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")

gold = code_medals.count('G')
silver = code_medals.count('S')
bronze = code_medals.count('B')

if len(code_medals) != gold + silver + bronze :
    print("Veuillez entrer un code de medaille valide.")
else :
    print(f"{country}:\n- {gold} OR\n- {silver} Argent\n- {bronze} Bronze") 


