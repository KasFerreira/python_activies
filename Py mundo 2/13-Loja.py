print("[1] A vista, 10% de desconto ")
print("[2] A vista no cartão, 5% de desconto")
print("[3] Até 2 x no catão")
print("[4] 3x ou mais no cartão")
vfinal = 0
tabela = 3
p = float(input(" Digite o valor do item.  "))
print("=======================================")
opcao = float(input("Escolha uma opção de pagamento "))

if opcao == 1:
   vfinal = p*0.9
   print(vfinal)
elif opcao == 2:
        vfinal = p*0.95
        print(vfinal)
elif opcao == 3:
        vfinal = p / 3
        print(vfinal)
elif opcao == 4:
        parcelas = int(input("Digite o numero de parcelas  "))
        vfinal = p*1.20
        pfinal = (vfinal / parcelas)
        print("São {} parcelas de {:.2f} reais e cada parcela custará {:.2f} ".format(parcelas,pfinal,vfinal))

