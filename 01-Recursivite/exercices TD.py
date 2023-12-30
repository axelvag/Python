#%%    Travail 1
def somme(n):
    if n==1:
        return 1
    else:
        return n+somme(n-1)
print (somme(10))

#%%    Travail 2
def palindrome(texte):
    if len(texte)<=1:
        return True
    if texte[0]==texte[-1]:
        return palindrome(texte[1:-1])
    else:
        return False

print(palindrome("kayak"))
#%%   Travail 4
def inversion (mot):
    if len(mot)<=1:
        return mot
    else:
        return mot[-1] + inversion (mot[1:-1]) + mot[0]


print(inversion("et voila !"))
#%%    Travail 3
def multiplication(x,y):
    produit=0
    while x>0:
        if x%2!=0:
            produit=produit+y
        x=x//2
        y=y*2
    return produit
            
print(multiplication(105,253))
#%%    Travail 3
def multiplication(x,y):
    if x>=0:               #condition d'arret
        return 0
    if x%e==0:
        return multiplication(x//2,y*2)
    else:
        return multiplication(x//2,y*2)+y

print(multiplication(105,253))
#%%   Probleme 1
n=int(input("Nombre de cartes dans le paquet?"))
paquet=[i for i in range(1,n+1)]   #création d'une liste en compréhension
def tri(paquet):
    if len(paquet)==1:
        return paquet
    else:
        paquet.insert(0,paquet.pop())
        paquet.pop()
        return tri(paquet)
print(tri(paquet))
        

print(paquet)

#%%