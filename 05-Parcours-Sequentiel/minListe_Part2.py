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

altitudes=[0, 200, 500, 1100, 1800, 2250, 2680, 5070, 6800, 8900, 9800, 11000, 13500, 15120, 17210, 19500, 20100, 21250, 23620, 24865]
temperatures=[15, 13.7, 11.7, 7.9, 3.4, 0.5, -2.3, -17.7, -28.9, -42.5, -48.3, -56, -56.2, -56.5, -56.3, -56, -56.1, -53, -50.1, -48]

indiceMini=trouveMin(temperatures)
print ("C'est à",altitudes[indiceMini],"m d'altitude que la température est la plus basse:",temperatures[indiceMini],"°C")
