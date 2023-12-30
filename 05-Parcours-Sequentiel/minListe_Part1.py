# ------------------------------------------------------------------
# PROGRAMME QUI .....
# ------------------------------------------------------------------

# ---------
# IMPORTS
# ---------
import random

# ---------
# FONCTIONS
# ---------

def genListe(lgListe):
    """
    Fonction qui renvoie une liste de longueur lg_liste avec des nombres entiers aléatoires compris entre -50 et 50.
    Le paramètre lg_liste attendu en entrée doit être un nombre entier
    """
    liste=[]                                # Création d'une variable de type liste vide
    for k in range(0,lgListe):              # Boucle qui s'effectue lgListe fois
        liste.append((random.random()*200)-100)   # Ajout à la liste d'un nombre réel aléatoire compris entre -100 et 100
    return (liste)                          # Renvoi de la liste créée au programme principal

def trouveMin(liste):
    """
    Fonction qui renvoie l'indice du minimum d'une liste.
    Le paramètre d'entrée attendu est une liste de valeurs numériques réelles.
    """
    min=liste[0]
    ind=0
    for i in range (1,len(liste)):
        if liste[i]<min:
            min=liste[i]
            ind=i
    return ind

# ----------------------------------------------------------------------------
# PROGRAMME PRINCIPAL
# ----------------------------------------------------------------------------

nbElem=int(input("nombre d'éléments dans la liste ?")) # Demande à l'utilisateur de saisir un nombre (string par défaut avec input, convertie ensuite en entier)
maListe=genListe(nbElem)                               # Appel de la fonction genListe avec comme argument en entrée nbElem
print (maListe)                                        # Affiche dans la console la liste générée

indiceMini=trouveMin(maListe)
print ("Le minimum est à la position",indiceMini,"de la liste")
