Sal = float(input("Qual o seu salário  "))
Vcasa = float(input("Qual é o valor da casa??  "))
Anos = float (input("Em quantos anos pretende pagar?"))


parcela = Vcasa / Anos


if parcela >= (30 / 100 * Sal):
    print("Não é possivel comprar a casa pois as parcelas são de {:.2f}".format(parcela))
else:
    print("Pode comprar a casa, as parcelas serão de {:.2f} reais".format(parcela))
