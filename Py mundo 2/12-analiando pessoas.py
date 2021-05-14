soma = 0
maior = 0
for p in range(0,4):
   nome = str(input("Digite o nome "))
   idade = int(input("Digite a idade da pessoa "))
   sexo = str(input(" QUal o sexo [M/F]? "))
   print("-----------------------------")
   soma = soma + idade
   if (sexo == 'M' and p == 0):
       maior = idade
       hmaisvelho = nome
   else:
          if (sexo == 'M' and idade > maior):
              maior = idade
              hmaisvelho=nome

media = soma/4
print("A média das idades é ", media)  
print(" O homem mais velho tem ",maior, " e é o ", hmaisvelho) 
