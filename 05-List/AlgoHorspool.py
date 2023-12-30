# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:44:25 2021

@author: 33782
"""
from collections import Counter

def identiqueDG_1(texte, motif, i):         # i est la position dans le texte à laquelle on calque le début du motif
    """
    fonction qui renvoi True si le motif est dans le texte sinon False
    """
    debut = -1
    k = len(motif)
    for _ in motif:
        if texte[i:i+k] == motif:
            return True
        else:
            i += k
    return False
    
def identiqueDG_2(texte, motif, i):
    """
    fonction similaire à identiqueDG_1 pour renvoyer un entier égal au décalage vers la droite à appliquer au motif par rapport au texte en cas d’échec lors de la comparaison
    """
    longueur = len(motif)
    for _ in range (longueur):
        if motif[longueur-1] != texte[i]:
            return longueur
        i = i-1
        longueur = longueur-1
    return 1

def identiqueDG_3(texte, motif, dicoMC, i):
    """
    fonction similaire à identiqueDG_2 mais qui calcule et renvoie le décalage du motif vers la droite à appliquer
    """
    nbr = 0
    while len(texte) > i:
        for lettre in reversed(motif):
            if texte[i] != lettre:
                if texte[i] not in motif:
                    return len(motif)
                else:
                    decalage = dicoMC[texte[i]] - nbr
                    if decalage < 0:
                        return 1
                    else:
                        return decalage
            else:
                nbr += 1
            i = i-1
        
def decalageMC(motif):
    """
    fonction qui établie un dictionnaire de décalage lié au motif pour l'algorithme de Horspool
    """
    dicoMC = {}
    m = len(motif)
    j = 0
    for lettre in motif-1:
        for double in motif-1:
            if double == lettre:
                lettre = [double]
        dicoMC.update({lettre:0})
        dicoMC[lettre] = m-j-1
        j += 1
    return dicoMC
        
def horspool(texte,motif):
    """
    fonction de horspool qui renvoie le nbr de comparaisons effectuées et le nbr d'occurences du motif dans le texte avec leur positions 
    """
    compteur = texte.count(motif)
    position = texte.counter.most_common(motif,0)
    nbrcomparaison = 0
    m = len(motif)
    n = len(texte)
    if m > n: 
        return -1
    skip = []
    for k in range(texte): 
        skip.append(m)
        nbrcomparaison += 1
    for k in range(m - 1): 
        skip[ord(motif[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and texte[i] == motif[j]:
            j -= 1; i -= 1
        if j == -1: 
            return i + 1
        k += skip[ord(texte[k])]
    return -1
    # compteur, i = 0, 0
    #     while True:
    #         occurrence = find(motif, i)  # occurrence est l'index du sous-texte à partir de l'index i
    #     if occurrence == -1:
    #         return compteur
    #     else:
    #         compteur += 1
    #         i += occurrence + 1
            
    return nbrcomparaison, compteur ,position

"""texte = open("LesTroisMousquetaires.txt", 'r')"""
texte2 = "du pain"
motif2 = "in"
# motif = "crime"
texte = "À vaincre sans péril, on triomphe sans gloire."
motif = "baril"
# texte = "Il frictionne sa jambe."
# motif = "fonction"
# texte = "Il y a deux histoires : l'histoire officielle, menteuse, qu’on enseigne, puis l'histoire secrète, où sont les véritables causes des événements."
# motif = "histoire"
# texte = "Il frictionne sa jambe."
# motif = "fonction"
# texte = "Rien de grand ne s'est accompli dans le monde sans passion."
# motif = "savant"


# -------------------------- Test identiqueDG_1
print (f'Le motif "baril" est-il dans le texte "À vaincre sans péril, on triomphe sans gloire." ?:')
print (identiqueDG_1(texte,motif,5))
print (f'Le décalage à droite à appliquer au motif "baril" est de:')
print (identiqueDG_2(texte,motif,2))

print (f'Le motif "in" est-il dans le texte "du pain" ?:')
print (identiqueDG_1(texte2,motif2,5))
print (f'Le décalage à droite à appliquer au motif "in" est de:')
print (identiqueDG_2(texte2,motif2,2))

# -------------------------- Test decalageMC
# print (decalageMC(motif))

# -------------------------- Test identiqueDG_3
# dicoMC = decalageMC(motif)
# print (identiqueDG_3(texte,motif,dicoMC,15))

# -------------------------- Test horspool
# print(horspool(texte,motif))






















