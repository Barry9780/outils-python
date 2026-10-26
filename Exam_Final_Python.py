#Exo: 1

def ecrire_fichier(nom_fichier):
    # ouvrons le fichier en ajout
    f = open(nom_fichier, "a", encoding="utf-8")

    print("Entrez des lignes vide pour arrêter")
    while True:
        #Lire une ligne au clavier
        ligne = input("> ")
        #Verifions si la ligne est vide
        if ligne == "":
            break
        #Ecrivons la ligne dans le fichier
        f.write(ligne + "\n")
    #Fermons apres le fichier
    f.close()
    print("Le texte est enregistré")


def lire_fichier(nom_fichier):
    try:
         # ouvrons le fichier en lecture
        f = open(nom_fichier, "r", encoding="utf-8")
        #Affissons le contenu du fichier
        print(f.read())
        #Fermons apres le fichier
        f.close()
        # Si le fichier n'existe pas
    except FileNotFoundError:
        print("Le fichier est introuvable")

#Demander a entrer le nom du fichier
def main():
    nom = input("Entrer le nom du fichier : ")

    print("1 - Écrire")
    print("2 - Lire")
    choix = input("Choix : ")

    if choix == "1":
        ecrire_fichier(nom)
    elif choix == "2":
        lire_fichier(nom)
    else:
        print("Votre choix est invalide")


main()

#Exo : 2

#Importons sys pour lire  l'argument du fichier
import sys

def generer_notes(fichier):
    # Lire le fichier ligne par ligne et retourne une note à la fois
    for ligne in fichier:
        # Enlevons les espaces unitiles
        ligne = ligne.strip()
        #Ignorer les lignes vides
        if ligne == "":
            continue
        # Separer le nom et la note
        parties = ligne.split()
        #Retournons la note une par une
        yield int(parties[1])


def calculer_moyenne(notes):
    #Initialisons le nobre de note et la somme des note a 0
    sommeNote = 0 
    nbreNote = 0

    for note in notes:
        sommeNote += note
        nbreNote += 1

    if compteur == 0:
        return None
    return sommeNote / nbreNote


def main():
    #Ouvrons le fichier passer en argument
    f = open(sys.argv[1], "r", encoding="utf-8")
    notes = generer_notes(f)
    moyenne = calculer_moyenne(notes)
    f.close()
 
    if moyenne is None:
        print("Il y'a aucune note")
    else:
        print("La Moyenne est :", moyenne)


main()

#Exo : 3

#A)
def erreur_index():
    try:
        #Declarons une liste avec 3 elements
        a = [1, 2, 3]
        print(a[4])
    except IndexError:
        #Affichage du message d'erreur
        print("Il y'a erreur d'index")
        raise
    finally:
        print("J'ai compris la gestion des exceptions")

#B)def erreur_type():
    try:
        #L'addition est impossible
        x = 1 + "Djarama"
        print(x)
    except TypeError:
        print("L'erreur de type")
        raise
    finally:
        print("J'ai compris la gestion des exceptions")
#Exo :4
        class Animal:
    def parler(self):
        return "bruit"

class Chien(Animal):
    def parler(self):
        return "wouf"

class Chat(Animal):
    def parler(self):
        return "miaou"


animaux = [Chien(), Chat(), Animal()]

#Appeler la main methode
for a in animaux:
    print(a.parler())
