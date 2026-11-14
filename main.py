
livres = []

while True:
    print("\n--- MENU ---")
    print("1. Ajouter un livre")
    print("2. Afficher les livres")
    print("3. Rechercher un livre")
    print("0. Quitter")
    
    choix = input("Ton choix : ")

    if choix == "1":
        titre = input("Titre du livre : ")
        if titre.strip() == "":
            print("Erreur : le titre ne peut pas être vide !")
        else:
            livres.append(titre)
            print("Livre ajouté !")

    elif choix == "2":
        if len(livres) == 0:
            print("Aucun livre pour le moment.")
        else:
            print("\nListe des livres :")
            for i in range(len(livres)):
                print(f"{i+1}. {livres[i]}")

    elif choix == "3":
        mot = input("Mot-clé à rechercher : ")
        trouves = []
        for livre in livres:
            if mot.lower() in livre.lower():
                trouves.append(livre)
        
        if len(trouves) == 0:
            print("Aucun livre trouvé.")
        else:
            print("Résultats :")
            for livre in trouves:
                print(f"- {livre}")

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide, réessaie.")