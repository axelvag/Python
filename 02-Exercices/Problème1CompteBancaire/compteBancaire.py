# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:05:28 2020

@author: axel.vaganay
"""


class CompteBancaire:
    
    def __init__(self, numeroCompte, nom, solde):
        self.numCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def __str__(self):
        texte = f'Le numéro de compte est {self.numCompte} \nLe nom est {self.nom}\nLa solde est de {self.solde}'
        return texte
    
    def versement(self, gainArgent):
        self.solde = self.solde + gainArgent
        
    def retrait(self, perteArgent):
        self.solde = self.solde - perteArgent
        
    def interets(self, pourcentageArgent):
        self.solde = self.solde + (self.solde*1,5)/100