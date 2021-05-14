jogador={}
colection=[]
gols=[]

while True:
    jogador['nome']=str(input("Digite o nome do jogador "))
    jogador['partidas']=int(input("Digite o numero de partidas jogadas "))
    for a in range(0,jogador['partidas']):
        gols.append(int(input(f"Digite os gols da partida {a}  ")))

    jogador['stats']=gols.copy()
    jogador['gols']=sum(gols[:])
    gols.clear()
    del jogador['partidas']
    colection.append(jogador.copy())

    while True:
        resp=str(input("Deseja continuar? "))
        if resp in 'SsNn':
            break
        else:
            print("ERRO")
    if resp in 'Nn':
        break
print('=-'*30)
print(f"{'cod':<3} {'nome':<20} {'gols':>0}{'total':>20}")
print('-'*60)

for k,v in enumerate(colection):
    print(f"{k:>1} ", end='')
    for d in v.values():
        print(f"{str(d):<22}",end='')
    print()
print('=-' * 30)
while True:
    print("Mostrar dados de qual jogador?   ")
    num=int(input(""))
    print('=-'*30)
    if num > len(colection):
        print("Não temos esse jogador no banco, digite outro numero.")
    else:
        print('=-' * 30)
        print(f"LEVANTAMENTO DO JOGADOR : {colection[num]['nome']}")
        for k,v in enumerate(colection):
         print(f"No jogo {k+1} fez {v['gols']} gols")
         break
    print('=-'*30)
    while True:
        rep=str(input("Deseja continuar?[S/N]  "))
        if resp in 'SsnN':
            break
        else:
            print("Erro, escolha [S/N] ")
    if resp in "nN":
        print(">>>>>>>FIM<<<<<<<")
        break