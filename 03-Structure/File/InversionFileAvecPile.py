# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 10:57:50 2020

@author: axel.vaganay
"""

from ClassFile.py import File
from ClassPile.py import Pile

def inverseFile(uneFile):
    
    maPileTampon=Pile()
    
    while not uneFile.estVide():
        maPileTampon.empiler(uneFile.defiler())
    
    while not maPileTampon.estVide():
        uneFile.enfiler(maPileTampon.depiler())
        
maFile=File([1,2,3,4])
print("Contenu de la File avant inversion:")
print (maFile)
inverseFile(maFile)
print ("Contenu de la File après inversion:")
print (maFile)