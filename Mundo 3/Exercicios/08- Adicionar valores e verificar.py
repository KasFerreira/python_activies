lista= []
continuar = True
while continuar == True:
    num=int(input("Digite um valor.  "))
    if num not in lista:
        lista.append(num)
    else:
        print("Valor já esta na lista, não vou adicionar  ")
    l = False
    while l == False:
        resp=str(input("Deseja continuar? "))
        if resp in 'sS':
            break
            l = True
        if resp in 'nN':
            print(" -----Saindo----- ")
            continuar = False
            l=True
        else:
            print(" ERRO, escolha S ou N para continuar")
lista.sort()
print(f"Os valores adiciondos são: {lista}")

