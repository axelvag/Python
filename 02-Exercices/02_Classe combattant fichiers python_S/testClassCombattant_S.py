# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:33:28 2020

@author: davidpaul.granjon
"""

from ClassCombattant_S import Combattant

guerrier = Combattant(10,2,"Guerrier ")
magicien = Combattant(5,4,"Magicien ")

print (guerrier.vie)
magicien.attaquer(guerrier)
print (guerrier.vie)

magicien.attaquer(guerrier)
print (guerrier.vie)

print (guerrier.estVivant())

magicien.attaquer(guerrier)
print (guerrier.vie)
print (guerrier.estVivant())

magicien.seBlesse(4)
print (magicien.vie)

magicien.seSoigne(2)
print (magicien.vie)

print (magicien)
print (guerrier)

magicien.combat(guerrier)