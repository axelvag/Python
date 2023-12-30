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

def trouveMin(liste):
    """
    Fonction qui renvoie l'indice du minimum d'une liste.
    Le paramètre d'entrée attendu est une liste de valeurs numériques réelles.
    """
    assert type(liste)==list, 'La variable envoyée à la fonction trouveMin doit être obligatoirement de type liste !'
    assert (type(liste[0])==float or type(liste[0])==int), 'Les éléments de la liste doivent être des nombres réels !'
    min=liste[0]
    ind=0
    for i in range (1,len(liste)):
        assert (type(liste[i])==float or type(liste[i])==int), 'Les éléments de la liste doivent être des nombres réels !'
        if liste[i]<min:
            min=liste[i]
            ind=i
    return ind

# ----------------------------------------------------------------------------
# PROGRAMME PRINCIPAL
# ----------------------------------------------------------------------------

indiceMini=trouveMin(maListe)
print ("Le minimum est à la position",indiceMini,"de la liste")
