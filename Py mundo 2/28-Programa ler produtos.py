soma=quant=menor=mbarato=0
resp='S'
while resp in 'Ss':
    prod=str(input(" Digite o nome do produto : "))
    prec=float(input("Digite o preço do produto : "))
    soma=prec+soma
    quant+=1
    resp=str(input(" Deseja continuar? [S/N] "))
    if quant == 1:
        menor = prec
        mbarato= prod
    if prec < menor:
        menor = prec
        mbarato = prod
   
print(f" O total foi R$ {soma}, foram comprados {quant} itens , o produto mais barato o(a) {mbarato} ")    
