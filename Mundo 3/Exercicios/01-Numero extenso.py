numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',' onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num=int(input("Digite um numero "))
    if 0 <= num <= 20:
        break
print(f"O numero é {numeros[num]}")        



# num=int(input("Digite um numero "))
# while num > 20 or num < 0 :
    
#    num=int(input("Digite um numero "))
# print(f"Você digitou o numero {numeros[num]}")


