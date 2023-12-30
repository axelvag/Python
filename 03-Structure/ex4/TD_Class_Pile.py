# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:45:34 2020

@author: david
"""

# ********************************************************************************
# CLASSE FILE - CREATION D'UNE STRUCTURE DE TYPE PILE en POO avec une List Python 
# ********************************************************************************

class Pile:
    '''Classe définissant une structure de données de type Pile (LIFO: Last In First Out) avec méthodes'''
    
    # Méthode: Constructeur de la pile
    def __init__(self,L=None):
        '''Méthode qui construit la Pile à partir d'une liste existante qui peut être vide ou non''' 
        if L==None:
            L=[]
        self.liste=L
            
    # Méthode empiler
    def empiler(self, elem):
        '''Méthode qui ajoute au Sommet de Pile (fin de liste). l'élément transmis en paramètre'''
        self.liste.append(elem)

    # Méthode dépiler
    def depiler(self):
        '''Méthode qui renvoie l'élément du dessus de la pile, ou False si la Pile est vide. Puis qui supprimme le sommet de la Pile'''
        if self.estVide():
            return False
        else:
            return self.liste.pop()
    
    # SURCHARGE de la Méthode d'AFFICHAGE
    def __repr__(self):
        '''Méthode qui redéfinie l'affichage de la Pile de façon personnalisée, et renvoie False si la Pile est vide'''
        if not self.estVide():
            chaine="Pile:  "
            nbElem=self.hauteur()
            for i in range (0,nbElem-1):
                chaine += eval("f'{self.liste[i]}   '")
            chaine += eval("f'{self.liste[nbElem-1]}'")
            return chaine
        else:
            return "Pile vide !"

    # Méthode estVide
    def estVide(self):
        '''Méthode qui renvoie True si la Pile est vide et False sinon'''
        return self.hauteur()==0
    
    # Méthode Sommet
    def sommet(self):
        '''Méthode qui renvoie l'élément du dessus de la pile, est False si la Pile est vide'''
        if not self.estVide():
            return (self.liste[-1])
        else:
            return False
       
    # Méthode Vider
    '''Méthode qui vide le contenu de la pile, et renvoi False si elle est vide'''
    def vider(self):
        if not self.estVide():
            self.liste.clear()
        else:
            return False

    # Méthode hauteur
    def hauteur(self):    
        '''Méthode qui renvoie le nombre d'éléments dans la Pile et False si la Pile est vide'''
        return len(self.liste)




# p1=Pile([4,8,68])
# p1.empiler(6)
# p1.empiler(-56)
# p1.empiler(9)
# print (p1.hauteur())
# p1.depiler()
# print(p1.sommet())
# print(p1)


# p2=Pile()
# print (p2.hauteur())
# p2.vider()
# print (p2)
# print (p2.estVide())
# p2.empiler((102,"a","abc"))
# print(p2)
# print (p2.estVide())
# del p2


# p3=Pile()
























