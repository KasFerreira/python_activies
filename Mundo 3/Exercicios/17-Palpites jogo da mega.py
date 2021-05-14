from random import randint
from time import  sleep

jogos=[]
sorteio=[]
print("-"*40)

print("        Jogo da mega        ")
print("-"*40)
n=int(input("Quantos jogos você quer sortear?  "))


for a in range(0,n):
    sorteio.clear()
    num=0
    while num != 6:
       sort=randint(0,60)
       if sort not in sorteio:
           sorteio.append(sort)
           num+=1
    jogos.append(sorteio[:])

print("-"*30)
for a in range(0,n):
    print(f" O jogo {a+1} é : ", end="")
    print(jogos[a])
    sleep(3)
print('-='*5, '>>Boa Sorte<< ' ,'-='*5)