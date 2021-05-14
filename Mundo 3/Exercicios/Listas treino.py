'''continua = True
lista = []
while continua == True:

    nomes=str(input(" Digite um nome  "))
    if nomes != "fechar":

        lista.append(nomes)
        print(lista)
    else:
        continua= False
lista.pop()
print(lista)
'''

'''lista=[]
lista.append(2)
lista.append(3)
lista.append(5)

for c,v in enumerate(lista):
    print(f" Na posição {c} temos  {v}")
'''
lista=[2,3,4,1,6,4]
lista_2= lista
lista_2[3]=9
print(lista)
print(lista_2)