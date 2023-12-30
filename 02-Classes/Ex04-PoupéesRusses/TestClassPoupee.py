# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:31:48 2020

@author: axel.vaganay
"""

from ClassPoupee import Boite
from random import randint

b1 = Boite(14,12,8)  #créer boite 1 avec longueur=14 , largeur=12 et hauteur=8
b2 = Boite(13,11,6)  #créer boite 2 avec longueur=13 , largeur=11 et hauteur=6

print(b1)
print ()
print(b2)

print(b1.rentreDans(b2))
print(b2.rentreDans(b1))


listeBoites=[]       #liste vide pour 20 boite avec longueurs,.... aléatoires
for i in range(20):
    nomBoite="boite"+str(i)
    nomBoite=Boite(randint(1,50),randint(1,50),randint(1,50))
    listeBoites.append(nomBoite)
    print(listeBoites[i])
    
from operator import attrgetter

listeBoites.sort(key=attrgetter('longueur'), reverse=True) 
#Tri la liste (avec sort) en prenant la clé de chaque boites qui contient ce qu'il y a dans la partie Longueur
#Puis (reverse=True) met dans l'ordre décroissant car par défaut c'est dans l'ordre croissant
