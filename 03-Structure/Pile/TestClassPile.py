# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:25:43 2020

@author: axel.vaganay
"""

from ClassPile import Pile

maPile=Pile([2,12,-4])
print(maPile)
maPile.empiler(18)
maPile.empiler(11)
print(maPile.depiler())
print(maPile)
print(maPile.hauteur())