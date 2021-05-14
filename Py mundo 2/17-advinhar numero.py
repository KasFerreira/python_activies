from random import randint

numero = int(input("Digite um numero "))
computador = randint(0,10)
contador= 1
print("---------------------\n O computador escolheu  ",computador)
print(" Você escolheu  ",numero)
if numero == computador:
    print("Parabéns, você acertou na primeira tentativa")
else: 
    while numero != computador:
        numero = int(input("Tente novamente  "))
        contador = contador + 1
        computador = randint(0,10)
        print("  O computador escolheu  ",computador)
        print(" Você escolheu  ",numero)
    else:
        print(" ="*10)
        print("- Parabéns, você acertou na tentativa numero ", contador) 
        print(" O computador escolheu  ",computador)
        print(" Você escolheu  ",numero)
        print(" ="*10)      
    
