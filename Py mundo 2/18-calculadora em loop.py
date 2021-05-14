num1= int(input("DIgite o primeiro numero  "))
num2= int(input("DIgite o segundo numero  "))

choice = int(input("Escolha uma das seguintes opções, Soma [1], Subtração[2], Divisão[3], Multiplicação[4] ,Sair[5]"))

while choice != 5:
    if choice == 1:
        print("O resultado é = ",num1+num2)
        num1= int(input("DIgite o primeiro numero  "))
        num2= int(input("DIgite o segundo numero  "))
        choice = int(input("Escolha uma das seguintes opções, Soma [1], Subtração[2], Divisão[3], Multiplicação[4] ,Sair[5]"))
    if choice == 2:
        print("O resultado é =", num1-num2)
        num1= int(input("DIgite o primeiro numero  "))
        num2= int(input("DIgite o segundo numero  "))
        choice = int(input("Escolha uma das seguintes opções, Soma [1], Subtração[2], Divisão[3], Multiplicação[4] ,Sair[5]"))
    if choice == 3:
        print("O resultado é = ",num1/num2)
        num1= int(input("DIgite o primeiro numero  "))
        num2= int(input("DIgite o segundo numero  "))
        choice = int(input("Escolha uma das seguintes opções, Soma [1], Subtração[2], Divisão[3], Multiplicação[4] ,Sair[5]"))
    if choice == 4:
        print("O resultado é =  ",  num1*num2)
        num1= int(input("DIgite o primeiro numero  "))
        num2= int(input("DIgite o segundo numero  "))
        choice = int(input("Escolha uma das seguintes opções, Soma [1], Subtração[2], Divisão[3], Multiplicação[4] ,Sair[5]"))
else:
    print("==="*10,"Saiu","==="*10)
    exit
                        