from datetime import date
date = date.today().year
ano = int(input(" DIgite o seu ano de nascimento   "))


idade = date - ano
if idade <= 9:
    print(" Esta na categoria Mirim")
elif idade <=14:
    print("esta na categoria infantil")
elif idade <= 19:
    print("Esta na categoria Junior")
elif idade <= 25:
    print("Senior")
else:
    print("Classificação master")