import random

def choisir_mot():
    with open("liste_mot.txt", "r") as fichier:
        mots = fichier.readlines()
    return random.choice(mots).strip()

def afficher_pendu(erreurs):
    etapes = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]
    print(etapes[erreurs])

def jouer():
    mot = choisir_mot()
    lettres_trouvee = set()
    lettres_ratees = set()
    erreurs = 0

    while erreurs < 6 and set(mot) != lettres_trouvee:
        print("\nMot à deviner : " + " ".join([lettre if lettre in lettres_trouvee else "_" for lettre in mot]))
        afficher_pendu(erreurs)
        lettre = input("Proposez une lettre : ").lower()

        if lettre in lettres_trouvee or lettre in lettres_ratees:
            print("Vous avez déjà proposé cette lettre.")
        elif lettre in mot:
            lettres_trouvee.add(lettre)
        else:
            lettres_ratees.add(lettre)
            erreurs += 1

    if set(mot) == lettres_trouvee:
        print(f"Félicitations ! Vous avez trouvé le mot : {mot}")
    else:
        afficher_pendu(erreurs)
        print(f"Vous avez perdu. Le mot était : {mot}")

if __name__ == "__main__":
    jouer()