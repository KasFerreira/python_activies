lista=[[],[]]  # Duas listas dentro de uma para segregar em par e impar.

for a in range(0,6):                                    #laço para leitura
    num=int(input(" Digite um numero  "))

    if num % 2 == 0:
        lista[0].append(num)               #Detalhe para o local onde ocorrerá o append lista[0], deve ser especificado
    else:
        lista[1].append(num)               #idem
print(lista)
print(f'A lista de pares é {lista[0]} e de impares {lista[1]}')