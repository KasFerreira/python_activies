lista=[]
temp=[]
while True:
    temp.clear()
    temp.append(str(input("DIgite o nome  ")))
    for a in range(0,2):
        temp.append(int(input(" Digite a Primeira nota  ")))
    resp=str(input("Deseja continuar [S/N]   "))
    lista.append(temp[:])
    if resp in 'Nn':
        break

for a in lista:
    media = a[1]+a[2]/2
    print(f'O aluno {a[0]}:{a[1],a[2]} e a média foi {media}')
