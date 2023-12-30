def creerListeVide(n):
    L=[None]*(n+1)
    L[0] = 0
    return L

def inserer(L,element,i):
    if(L[0]==len(L)-1 or (i>L[0]+1) or (i<1)):
        print("La liste est pleine,ou le rang n'est pas correct")
        return False
    else:
        for k in range(L[0]+1,i,-1):
            L[k] = L[k-1]
        L[i]=element
        L[0] = L[0]+1
        return True
    
def retirer (L,i):
    if ((L[0] != 0) and (i<=L[0])) and (i>0)):
        for k in range(i,L[0],1):
            L[k] = L[k+1]
        L[0] = L[0]-1
        return True
    else:
        print ("la liste est vide ou le rang n'est pas correct")
        return False
    
def longueur(L):
    return L[0]
    
def lire(L,i):
    if L[0] != 0 and i<=L[0] and i>0:
        return L[i]
    else:
        print ("la liste est vide, rang inaproprié")
        
def vider(L):
    if L[0] != 0:
        L[0] = 0
        
def modifier(L,i,nvlElem):
    if L[0] != 0 and i<=L[0] and i>0:
        L[i] = nvlElem
    else:
        print("la liste est vide, rang inapproprié")
    
def rechercher(L,elem):
    """
    Renvoi le premier elem trouvé en partant du début de la liste
    """
    if L[0] != 0:
        for i in range(1,L[0]+1):  #va du rang un jusqu'au dernier(L[0] n'est pas pris en compte)
            if L[i]==elem:
                return i
        return False
    else:
        print ("")
        
L1=creerListeVide(5)
inserer(L1,3,1)
retirer(L1,2)
print(L1)

         
    
        
            
        
    
