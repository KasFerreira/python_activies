lista= []
count=0
continuar=True
while continuar == True:
        lista.append(int(input("DIgite um numero  ")))
        count+=1
        resp=str(input("Deseja continuar [S/N]"))
        if resp not in 'sS':
            continuar = False
        else:
            continuar= True

lista.sort(reverse=True)
print(f"Você digitou  {count} numeros")
print(f'E na ordem decrescente é {lista}')
if 5 in lista:
    print("Tem 5 na lista.")