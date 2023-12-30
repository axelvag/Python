# -*- coding: utf-8 -*-
"""
@author: david
"""

def identique(texte, motif, i):
    """
    fonction qui renvoi True si le motif est dans le texte sinon False
    """
    for lettre in motif:
        if lettre != texte[i]:
            return False
        i += 1
    return True


def recherche_naive(texte,motif):
    """
    fonction qui utilise la fonction identique pour renvoyer un entier égal à la position du premier caractère du motif dans la chaine texte si la recherche aboutit, et à -1 dans le cas contraire
    """
    for i in range(len(texte)-len(motif)+1):
        if identique(texte, motif, i):
            return i
    return -1

 
def recherche_naive_v2(texte,motif):     #version break
    """
    fonction qui renvoi un entier égal à la position du premier caractère du motif dans la chaine texte si la recherche aboutit, et à -1 dans le cas contraire
    """
    for i in range(len(texte)-len(motif)+1):    
        nbMatch = 0
        for j in range (len(motif)):
            if motif[j] != texte[i+j]:
                break
            nbMatch += 1
        if nbMatch == len(motif):
            return i
    return -1
            

def recherche_naive_v3(texte,motif):     
    """
    fonction qui renvoi le nombre de comparaisons effectuées, ainsi que le nombre d’occurrences du motif dans le texte avec leurs positions
    """         
    occurence = 0
    positions = []
    compteurComparaison = 0
    for i in range(len(texte)-len(motif)+1): 
        nbMatch = 0
        for j in range (len(motif)):
            compteurComparaison += 1
            if motif[j] != texte[i+j]:
                break
            nbMatch += 1
        if nbMatch == len(motif):
            occurence += 1
            positions.append(i)
    return compteurComparaison,occurence,positions

 
texte = "Les sanglots longs des violons de l'automne blessent mon cœur d'une langueur monotone. Tout suffocant et blême, quand sonne l'heure, je me souviens des jours anciens et je pleure."
motif = "vio"
# texte = "un papou papa à poux a des poux papas et des poux pas papas"
# motif = "papas"
# texte = "00000001"
# motif = "1"
# texte = "Réfléchir est un bon moyen de progresser"
# motif = "avis"
# texte = "Il y a deux histoires : l'histoire officielle, menteuse, qu’on enseigne, puis l'histoire secrète, où sont les véritables causes des événements."
# motif = "histoire"
# motif = "officielle"
# texte = "Rien de grand ne s'est accompli dans le monde sans passion."
# motif = "savant"  
# texte = "du pain"
# motif = "in"         


# -------------------------- Test identique
print (identique(texte,motif,2))

# -------------------------- Test recherche_naive
print (recherche_naive(texte, motif))

# -------------------------- Test recherche_naive_v2
print (recherche_naive_v2(texte, motif))

# -------------------------- Test recherche_naive_v3
print (recherche_naive_v3(texte, motif))


















