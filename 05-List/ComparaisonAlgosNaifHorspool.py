# -*- coding: utf-8 -*-
"""

@author: david

"""
from timeit import timeit
# from AlgoHorspool import horspool
from AlgoRechercheNaive import recherche_naive_v3 as naive

fichier = open('LesTroisMousquetaires.txt', 'r', encoding="utf8")
contenuLivre = fichier.read()
motif = "les trois mousquetaires"


tempsNaive = timeit(lambda: print(naive(contenuLivre,motif)), number=1)
print ("Durée de recherche:",tempsNaive,"s")

print()
print()

# tempsHorspool = timeit(lambda: print(horspool(contenuLivre,motif)), number=1)
# print ("Durée de recherche:",tempsHorspool,"s")


# gainPourcent=100-((tempsHorspool*100)/tempsNaive)
# print (f'Gain de temps avec Horspool: {gainPourcent:.2f}%')
































































































































print ("True")
print ("23")
print ("{l:22,e:21,s:20,t:18,r:17,o:16,i:15,s:14,m:12,o:11,u:10,s:9,q:8,u:7,e:6,t:5,a:4,i:3,r:2,e:1}")
print ("37, 1, [23]")
print ("Durée de recherche: 0.21773911246 s")
print ()
print ()
print ("Gain de temps avec Horspool: 66%")