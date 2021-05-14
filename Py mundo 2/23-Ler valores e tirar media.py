resp = 'S'
soma = media = quant = maior = 0
menor = 0
while resp in 'Ss':
    num = int(input(" DIgite um numero   "))
    soma +=num
    quant+=1

    if quant == 1:
        maior = menor = num
    else:
        if num < menor:
             menor = num
        if  num > maior:
              maior = num
        
             
    resp=str(input(" Quer continuar [S/N]")).upper().strip()[0]
media = soma/quant
print(" A média é ", media," o maior numero é ", maior, " e o menor é ",menor, "ok")    

