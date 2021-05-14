from random import randint
from time import sleep
print(" \n Manga, duvido você ganhar de mim, boa sorte! \n")
print(" -----Escolha -----\n Pedra[0] \n Papel[1] \n Tesoura[2]\n------------")
itens = ['Pedra', 'Papel', 'Tesoura']
computer = randint(0,2)
choice= int(input(" "))

print("=*="*11,"\n  O computador escolheu  ",itens[computer])
print("  Você escolheu " ,itens[choice])
print("=*="*11)

if computer == 0: # Se computador escolher Pedra
    if choice == 0: # Se jogador escolher Pedra
        print("Empate")
    elif choice == 1: # Se jogador escolher Papel
        print("Você ganho")
    elif choice == 2: # Se jogador escolher Tesoura
        print("Você perdeu") 
                
elif computer == 1: # Se o computador escolher Papel
    if choice == 0: # Se jogador escolher Pedra
        print("Você perdeu")
    elif choice == 1: # Se jogador escolher Papel
         print("Empate")
    elif choice == 2:  # Se jogador escolher Tesoura
        print("Você ganhou")
elif computer == 2: # Se o computador escolher Tesoura
    if choice == 0: # Se jogador escolher Pedra
        print("Você Ganhou")
    elif choice == 1:  # Se jogador escolher Papel
        print("VOcê Perdeu") 
    elif choice == 2: # Se jogador escolher Tesoura
        print("Empate")     
print('#=#'*11,"\n----Fim ----")         

sleep(5)    
