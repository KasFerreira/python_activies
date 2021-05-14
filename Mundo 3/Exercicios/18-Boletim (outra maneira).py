'''lista=[]
notas=[]
aluno=[]
print("-="*20)
print("         BOLETIM ESCOLAR          ")
print("-="*20)
for a in range(0,3):
    lista.append(str(input("Digite um nome  ")))
    notas.append(float(input("Digite uma nota  ")))
    notas.append(float(input("Digite uma nota  ")))
    lista.append(notas[:])
    aluno.append(lista[:])
    notas.clear()
    lista.clear()

print('-'*20)

for a,b in enumerate(aluno):
    media = (b[1][1]+b[1][0]) / 2
    print(f'{a}   A média de {b[0]} foi:', ' '*2,f"  {media}")

print('-'*20)

while True:
    num=int(input("As notas de qual aluno(a) você deseja saber? (digite [999] para sair) "))
    if num == 999:
        print("FIM")
        break
    else:
        print(f'As notas do aluno(a)  {aluno[num][0]} são : {aluno[num][1]}')'''


ficha=[]
while True:
    nome=str(input("Digite seu nome  "))
    nota1=float(input("Digite a primeira nota  "))
    nota2=float(input("Digite a segunda nota  "))
    media= (nota1+nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    resp=str(input("Deseja continuar? [S/N]  "))
    if resp in 'Nn':
        break
print("-="*30)
print(f'{"No.":<4}{"Nome":<10}{"Media":8}')
print("-="*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-="*30)
    opc=int(input("Mostar notas de qual aluno? (999 interrompe):"))
    if opc == 999:
        print('FInalizando...')
        break
    if opc<=len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<Volte Sempre>>>>')