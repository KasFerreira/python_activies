continuar= True
lista=[]
lista_par=[]
lista_impar=[]
while continuar == True:
    lista.append(int(input("Digite um numero:  ")))
    resp= str(input("Deseja continuar [S/N]"))
    if  resp not in 'Ss':
        continuar=False
    else:
        pass
for a in lista:
    if a%2 ==0:
        lista_par.append(a)
    else:
        lista_impar.append(a)
print("--"*40)
print(f"A lista original é {lista}")
print(f"A lista par é {lista_par}")
print(f"A lista impar é {lista_impar}")
print("-"*40)