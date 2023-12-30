# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 11:29:31 2020

@author: axel.vaganay
"""

class Boite:
    
    def __init__(self,longueur,largeur,hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur

    def __repr__(self):     #Pratiquement comme surcharger (__str__)
        return f'Longueur: {self.longueur} \nLargeur: {self.largeur} \nhauteur: {self.hauteur} \nVolume: {self.volume()}'
    
    def volume(self):
        return self.longueur * self.largeur * self.hauteur
    
    def rentreDans(self, autreBoite):
        return autreBoite.longueur>self.longueur and autreBoite.largeur>self.largeur and autreBoite.hauteur>self.hauteur
