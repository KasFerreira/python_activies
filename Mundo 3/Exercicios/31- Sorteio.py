from time import  sleep
from random import  randrange, randint
lista=[]

def sorteio():
    for a in range(0,5):
        lista.append(randint(0,10))
    print(lista,'ok')

def soma():
    cont=0
    for a in lista:
        if a % 2 == 0:
           cont= a+cont
    print(f" A soma dos pares em {lista} é {cont}")

sorteio()
soma()