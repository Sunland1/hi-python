def check(c):
    t = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "w", "x", "y",
         "z" , "n"]
    i = len(t)
    while i == len(t):
        k = 0
        while k < len(t):
            if c == t[k]:
                return c
            k = k + 1
        print("saisie de nouveau un caractère de l'alphabet ")
        c=input()
        i=len(t)
from random import *
#Crée une fonction qui verifie un caractère de l'alphabet saisie par l'utilisateur
#et on demandera de saisir a nouveau et retourne a la lettre saisie
#On supposera que les caractère vérifier son majuscule et commence par a et finis par z
def randmot():
    t=[]
    x=randint(0,3)
    f=open("../asset/dico.txt","r")
    li=f.readline()
    while ''!=li:
        t+= [li]
        li=f.readline()
    mot=t[x]
    mot = mot.replace('\n', '')
    mot = mot.replace('\t', '')
    return mot
#Crée une fonction qui prend au hasard un mot dans le fichier texte dico
#On utilisera la bibliothèque random et on stockera provisoirement les mot dans une liste
#Pour des soucis quelconque on apliquera mot=mot.replace('\n','') et mot=mot.replace('\n','')
def affichage1(mot):
    a1=""
    i=0
    while i<len(mot):
        a1+="_"
        i+=1
    return a1
#Crée une fonction affichage pour le pendu qui prend parametre le mot a trouver et qui retourne
# a des _ _ _ _ _ _ qui correspond a longueur du mot !
def replace(c,a):
    a1=[]
    replace=''
    i=0
    k=0
    j=0
    isGood = False
    while k <len(a):
        a1.append(a[k])
        k+=1
    while i<len(mot):
        if c==mot[i]:
            a1[i]=c
            isGood = True
        i+=1
    while j<len(a1):
        replace+=a1[j]
        j+=1
    return replace,isGood


def test(a,b):
    if a==b:
        return True

def difficul(mot) :
    return int((len(mot)-3))

mot=randmot()
a1=affichage1(mot)
i=difficul(mot)
game = True
isGood = False
while i>0 and game:
    print("Il te reste nb chance " , i)
    print(a1)
    print("une nouvelle lettre")
    c=input()
    check(c)
    a1,isGood=replace(c,a1)
    isSame=test(a1,mot)
    if isSame :
        print("GG")
        print(mot)
        game = False
    if not isGood : 
        i-=1

if i==0:
    print(" Perdu le mot etait :" ,mot)
