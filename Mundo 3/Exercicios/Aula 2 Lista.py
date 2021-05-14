'''teste= list()

teste.append("Lucas")
teste.append(25)
New_lista=list()
New_lista.append(teste[:])
teste[0]="Maria"
teste[1]=55
New_lista.append(teste)

print(New_lista)'''

'''lista= [["Lucas", 25],["Maria",55],["Lara", 22],["Joseh", 22]]
for p in lista:
 print(f' {p[0]} tem  {p[1]} anos de idade.')'''''

galera=[]
dado=[]
maior=menor=0
for c in range(0,5):
    dado.append(str(input("Digite seu nome ")))
    dado.append(int(input(" Digite sua idade  ")))
    galera.append(dado[:])
    dado.clear()


for p in galera:
    if p[1] >= 18:
        print(f' {p[0]} é maior de idade ')
        maior+=1
    else:
        print(f' {p[0]} é menor de idade' )
        menor+=1
print(f'o numero de maiores é {maior} e o de menores é {menor}')
