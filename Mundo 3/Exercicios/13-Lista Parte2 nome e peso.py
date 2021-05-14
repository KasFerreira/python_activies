pessoas=[]
galera=[]
Pesadas=[]
Leves=[]
medio=[]

maior=menor=0
while True:
    pessoas.append(str(input("Digite um nome ")))
    pessoas.append(int(input("Digite o peso  ")))
    if len(galera) == 0:
        maior =menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]

    galera.append(pessoas[:])
    pessoas.clear()
    resp=str(input("Deseja continuar?[S/N]"))

    if resp in 'Nn':
        break


'''for p in galera:
    if p[1]>= 90:
        Pesadas.append(p)
    elif p[1] <= 60:
        Leves.append(p)
    else:
        medio.append(p)'''


'''print("="*50, f"\n O numero de pessoas cadastradas foi  {len(galera)} ." )
if Pesadas != 0:
    print('\nA lista de pessoas Pesadas:',end=" ")
    for a in Pesadas:
      print(f' {a[0]},',end=", ")
if Leves != 0:
    print('\nA lista de pessoas Leves:',end=" ")
    for a in Leves:
        print(f' {a[0]}', end=", ")
if medio !=0:
    print('\nA lista de pessoas Medias:',end=" ")
    for a in medio:
      print(f' {a[0]}',end=", " )'''

print(f"O numero total de caastrados foi {len(galera)}")
print(f'\nE o maior peso foi de : {maior}kg  ',end='')
for a in galera:
    if a[1] == maior:
      print(f'Peso de [{a[0]} ]',end='')
print()
print(f"E o menor peso foi de: {menor} kg ",end="")
for a in galera:
    if a[1] == menor:
      print(f" Peso de [{a[0]}] ", end='')
