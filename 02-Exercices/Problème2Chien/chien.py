# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:30:14 2020

@author: axel.vaganay
"""

class Chien:
    
    def __init__(self, nom, pointsSante=10, aboiement="waafff"):
        self.nom = nom
        self.pointsSante  = pointsSante
        self.aboiement = aboiement
        
    def __str__(self):
        texte = f'{self.nom} \n'
        texte+= f'Santé: {self.pointsSante}    Aboiement:{self.aboiement}'
        return texte

    def mordre(self, autreChien):
        autreChien.pointsSante -=2
        
    def manger(self):
        self.pointsSante +=5
    
    def grogner(self):
        return f'Grrr...{♣self.aboiement}'
    
    def machouiller(self, chaine):
        chaineEnLite = list(chaine)
        shuffle(chaineEnListe)
        resultat = ''.joinn(chaineEnListe)
        return resultat