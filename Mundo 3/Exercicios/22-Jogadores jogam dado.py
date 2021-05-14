from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador1':randint(0,6),'jogador2':randint(0,6),'jogador3':randint(0,6),'jogador4':randint(0,6)}
ranking=[]
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('*'*10)
print('Lista de campeões')
print('*'*10)
for a,b in enumerate (ranking):
    print(f'{a+1}ª lugar {b[0]} tirou {b[1]}')
    sleep(0.3)

'''lista=[]
for a in range(1,5):
    jogadores={'jogador': a,'resultado':randint(0,6)}
    lista.append(jogadores.copy())
for a in lista:
    print(f"O jogador {a['jogador']} tirou o numero {a['resultado']}")
    sleep(1)
print("Os ganhadores foram  ")
for a in lista:
    if a['resultado'] ==6:
    print()
'''






'''from random import randint
jogadores={}
lista={}
for a in range(0,4):
    jogadores['nome']=str(input("DIgite o nome do jogador "))
    jogadores['jogada']=randint(0,6)
    lista[]

print(lista)'''
