from random import randint
vence= True
while vence == True:
    escolha=str(input("Escolha Par ou impar [P/I] "))
    num=int(input(" Escolha um numero "))
    comp=randint(1,10)
    soma=comp+num
    if escolha in 'Pp':
        if soma % 2 == 0:
            print(f"A soma deu {soma} e é par, parabéns, vc ganhou")
        else:
             print(f"A soma deu {soma}, vc perdeu, tente de novo")   
             break
    if escolha in 'Ii':   
        if soma % 2 != 0:
             print(f"A soma deu {soma}, impar, parabéns vc ganhou")
        else:
            print(f"A soma deu {soma}, vc perdeu, tente de novo")   
            break
        