# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:12:21 2020

@author: axel.vaganay
"""


from compteBancaire import CompteBancaire
compteAxel=CompteBancaire(12313544845,"CompteAxel",5433.25)
compteGerard=CompteBancaire(1245454345,"CompteAxel",1233.25)

compteAxel.versement(30)
print(compteAxel.solde)

print(compteAxel)