
taches = []

while True:
    print("=== GESTION DES TACHES ===")
    print("1. Ajouter une tache")
    print("2. Afficher les taches")
    print("3. Rechercher une tache")
    print("0. Quitter")
    choix = input("Votre choix : ")

    if choix == "1":
        titre = input("Titre de la tache : ")
        if titre == "":
            print("Le titre ne peut pas etre vide.")
        else:
            taches.append(titre)
            print("Tache ajoutee avec succes.")

    elif choix == "2":
        if len(taches) == 0:
            print("Aucune tache pour le moment.")
        else:
            for i in range(len(taches)):
                print(f"{i+1}. {taches[i]}")

    elif choix == "3":
        mot = input("Mot-cle : ")
        trouve = False
        for t in taches:
            if mot in t:
                print(t)
                trouve = True
        if not trouve:
            print("Aucune tache trouvee.")

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("Choix invalide.")