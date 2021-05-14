cont=soma =menor=0
while True:
    nome=str(input("Qual é o produto ?  "))
    prec = float(input(" Qual o valor ?  "))
    cont+=1
    soma+=prec
    
    if cont == 1 or prec < menor:
        menor=prec
        mbarato=nome
    
    resp = ' '
    while resp not in 'SsNn':
        resp=str(input(" Deseja continuar ? [S/N]  "))
    if resp  in 'Nn':
        break
print('{:-^40}'.format('fim do programa')) 
print(f" O total fo {soma} e a quantidade foi {cont}") 
print(f"O menor preço foi do  {mbarato}")    
  