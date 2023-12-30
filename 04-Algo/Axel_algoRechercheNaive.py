# -*- coding: utf-8 -*-
"""
@author: axel
"""

def identique(texte, motif, i):
    """
    fonction qui renvoi True si le motif est dans le texte sinon False
    """
    k = len(motif)
    for _ in texte:
        if texte[i:i+k] == motif:    #si le motif de longueur k est présent dans le texte à la position i
            return True
    return False


def recherche_naive(texte,motif):
    """
    fonction qui utilise la fonction identique pour renvoyer un entier égal à la position du premier caractère du motif dans la chaine texte si la recherche aboutit, et à -1 dans le cas contraire
    """
    if identique(texte, motif) == True:    #utilisation de la fonction "identique" ci-dessus si il y a une occurence du motif dans le texte
        n = len(texte)
        i = 0
        while i < n and motif[0] != texte[i]:
            i += 1
            if i < n:
                return i
    else:
        return -1

def recherche_naive_v2(texte,motif): 
    """
    fonction qui renvoi un entier égal à la position du premier caractère du motif dans la chaine texte si la recherche aboutit, et à -1 dans le cas contraire
    """
    m = len(motif)
    position = []
    for i in (int(len(texte))-m+1):  #boucle pour analyser de façon optimisé chaque rang du texte
    	if texte[i:i+m] == motif:    #si le motif de longueur k est présent dans le texte à la position i
    		position = i
    if position == []:
        position = -1
    return position  #renvoi de la position de l'occurence
        

def recherche_naive_v3(texte,motif):  
    """
    fonction qui renvoi le nombre de comparaisons effectuées, ainsi que le nombre d’occurrences du motif dans le texte avec leurs positions
    """
    m = len(motif)         
    indice = 0
    nbrDeComparaison = 0
    while indice < len(texte):   #prise des positions de chaque occurences
        indice = texte.find(motif, indice)    
        if indice == -1:
            break
        indice += len(motif)
    for i in (int(len(texte))-m+1):  #calcul du nombre de comparaison
        nbrDeComparaison += 1
        if texte[i:i+m] == motif:
            nbrDeComparaison +=1
    return nbrDeComparaison,indice

 
# texte = "Les sanglots longs des violons de l'automne blessent mon cœur d'une langueur monotone. Tout suffocant et blême, quand sonne l'heure, je me souviens des jours anciens et je pleure."
# motif = "vio"
# texte = "un papou papa à poux a des poux papas et des poux pas papas"
# motif = "papas"
# texte = "00010001"
# motif = "1"
# texte = "Réfléchir est un bon moyen de progresser"
# motif = "avis"
# texte = "Il y a deux histoires : l'histoire officielle, menteuse, qu’on enseigne, puis l'histoire secrète, où sont les véritables causes des événements."
# motif = "histoire"
# motif = "officielle"
texte = "Rien de grand ne s'est accompli dans le monde sans passion."
motif = "savant"  
# texte = "du pain"
# motif = "in"         


# -------------------------- Test identique
print (identique(texte,motif,2))

# -------------------------- Test recherche_naive
# print (recherche_naive(texte, motif))

# -------------------------- Test recherche_naive_v2
# print (recherche_naive_v2(texte, motif))

# -------------------------- Test recherche_naive_v3
# print (recherche_naive_v3(texte, motif))




















