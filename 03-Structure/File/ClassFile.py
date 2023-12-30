# -*- coding: utf-8 -*-
"""
@author: david
"""

# *****************************************************************
# CREATION D'UNE STRUCTURE DE TYPE FILE en POO avec une List Python
# *****************************************************************

class File:
    '''Classe définissant une structure de données de type File (FIFO: First In First Out) avec méthodes'''

    # Méthode qui construit la File
    def __init__(self,L=None):
        '''Méthode qui construit une structure de type File à partie d'une liste vide ou pas'''
        if L==None:
            L=[]
        self.liste=L

    # Surcharge de la méthode d'affichage
    def __repr__(self):
        '''Méthode qui redéfinie l'affichage de la File de façon personnalisée'''
        if self.estVide():
            return "File vide !!"
        else:
            chaine="File:  "
            nbElem=self.longueur()
            for i in range (0,nbElem-1):
                chaine += eval("f'{self.liste[i]}  '")
            chaine += eval("f'{self.liste[nbElem-1]}'")
            return chaine

    # Méthode longueur pour obtenir le nombre d'éléments dans la File
    def longueur(self):
        '''Méthode qui renvoie la longueur de la file, ou False si elle est vide'''
        return len(self.liste)

    # Méthode estVide
    def estVide(self):
        '''Méthode qui renvoie True si la File est vide ou sinon False'''
        return (len(self.liste)==0)

    # Méthode enfile
    def enfiler(self,elem):
        '''Méthode qui enfile(ajoute) un élément à la file en fin de file(liste)'''
        self.liste.append(elem)

    # Méthode défile
    def defiler(self):
        '''Méthode qui renvoie le premier de la file et le supprime de la file, renvoie False si la file est vide'''
        if not self.estVide():
            return self.liste.pop(0)
        else:
            return False

    # Méthode Vider
    '''Méthode qui vide le contenu de la file, et renvoi False si elle est vide'''
    def vider(self):
        if not self.estVide():
            self.liste.clear()




# f1=File()
# print (f1.estVide())
# print (f1.longueur())
# f1.enfiler(5)
# f1.enfiler(-2.568)
# f1.enfiler(('a',18))
# f1.enfiler([1,5,90])
# print (f1)
# print (f1.defiler())
# print (f1)