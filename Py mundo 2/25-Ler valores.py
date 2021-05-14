soma=media=menor=maior=quant = 0
continuar=True
while continuar == True:
    num=int(input("Digite um numero: "))
    soma= soma +num
    quant+=1
    cont=str(input("Deseja continuar [S/N] ..."))
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num        
    if cont in 'Ss':
         continue
    else:
            continuar = False
media=soma/quant            
print(media,"O menor numero é", menor, "E o maior é ", maior)            