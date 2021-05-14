lista= []
maior=menor=posiçãom=posiçãoM=0
for a in range(0,5):
   num=int(input("Digite um numero   "))
   lista.append(num)

for p,n in enumerate(lista):
    if p==0:
       maior = menor = n
    if n > maior:
        maior = n
        posiçãoM = p

    if n < menor:
        menor =n
        posiçãom = p

print(f"O maior numero é {maior} e esta na posição {posiçãoM} o menor é: {menor} que esta na posição {posiçãom}")
print(lista)