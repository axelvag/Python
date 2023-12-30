# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 11:14:19 2020

@author: axel.vaganay
"""
from TD_Class_Pile import Pile

class File():
    
    def __init__(self):
        self.pileG=Pile()
        self.pileD=Pile()
    
    def estVide(self):
        return self.pileG.estVide() and self.pileD.estVide()
    
    def enfiler(self,elem):
        '''Méthode qui enfile(ajoute) un élément à la file en fin de file(liste)'''
        self.pileG.empiler(elem)
        
        
    def defiler(self):
        if self.pileD.estVide():
            while not self.pileG.estVide():
                element=self.pileG.depiler()
                self.pileD.empiler(element)
        return self.pileD.depiler
    
file1=File()
print (file1.estVide())
file1.enfiler(3)
file1.enfiler(5)
print(file1.defiler())