from PIL import Image
import unicodedata
import time
import random

films_file = "C:/Users/noaob/Desktop/IIM/A2/Python/Rendu Python/liste_films.txt"
images_path = Image.open("C:/Users/noaob/Desktop/IIM/A2/Python/Rendu Python/images_films/WTF.jpg")
images_path.show()

def get_films(films_file):
    with open(films_file, "r", encoding="utf-8") as f:
        films_list = [line.strip() for line in f if line.strip()]
    return films_list

films_list = get_films(films_file)

score = 0
scoreperdant = 0

def normaliser(texte):
    texte = texte.lower()
    texte = unicodedata.normalize('NFD', texte).encode('ascii', 'ignore').decode("utf-8")
    return texte.strip()

def instructions():
    print("Bienvenue dans WhatTheFilm(WTF) !")
    time.sleep(1)
    print("Vous devez entrer le nom d'un film à partir d'une image.")
    time.sleep(1)
    print("Vous avez 10 films à trouver.")
    time.sleep(1)
    print("Vous avez 3 erreurs possibles avant de perdre.")
    time.sleep(1)
    print("Bonne chance !")

def demmandezindice():
    indice = input("Voulez-vous un indice ? (oui/non) ")
    if indice.lower() == "oui":
        print("Voici un indice :")
        time.sleep(1)
        
        indices = [
            "Le film en haut à gauche commence par un F.",
            "Le film en haut au milieu commence par un P.",
            "Le film en haut à droite commence par un B.",
            "Le film au milieu à droite commence par un S.",
            "Le deuxième film au milieu en partant de la droite commence par un P.",
            "Le troisième film au milieu en partant de la droite commence par un C.",
            "Le film au milieu gauche commence par un O.",
            "Le film en bas à gauche commence par un I.",
            "Le film en bas au milieu commence par un E.",
            "Le film en bas à droite commence par un E."
        ]
        
        indice_choisi = random.choice(indices)
        print(indice_choisi)
    else:
        print("D'accord, bonne chance ! Vous n'aurez plus d'indice.")
        indice_affiche = True


instructions_affichees = False
indice_affiche = False

while True:

    if not instructions_affichees:
        instructions()
        instructions_affichees = True 

    reponse = input("Entrez le nom d'un film: ")

    reponse_normalisee = normaliser(reponse)
    
    films_normalises = [normaliser(film) for film in films_list]
    
    if reponse_normalisee in films_normalises:
        score += 1
        print(f"Bonne réponse : {reponse}! Votre score est de {score}/10")
        print(f"Vous aviez fait {scoreperdant}/3 erreurs.")
        
    else:
        scoreperdant += 1
        print(f"Ce film n'est pas dans la liste. Vous avez fait {scoreperdant}/3 erreurs.")
    
    if scoreperdant == 3:
        print("Vous avez perdu ! Veuillez recommencer.")
        print(f"Votre score etait de {score}/10.")
        score = 0
        scoreperdant = 0
        break

    if not scoreperdant == 2:
        demmandezindice()
        indice_affiche = True

    if score == 10:
        print("Vous avez gagné ! Félicitations ! Vous pouvez réessayer si vous le souhaitez.")
        score = 0
        scoreperdant = 0
        break
