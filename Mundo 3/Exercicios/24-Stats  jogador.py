jogador={}
gols=[]


jogador['Nome']=str(input("Digite o nome do jogador "))
jogador['partidas']=int(input("Digite o numero de partidas jogadas "))
for a in range(0,jogador['partidas']):
    gols.append(int(input(f"Digite os gols da partida {a}  ")))

jogador['stats']=gols.copy()
jogador['gols']=sum(gols[:])
print('=-'*30)
print(jogador)
print('=-'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f"O jogador {jogador['Nome']} jogou {jogador['partidas']} partidas.")
for a,b in enumerate(gols):
    print(f'Na partida {a}, fez {b} gols ')
print(f'Foi um total de {jogador["gols"]}')
