from datetime import datetime
p = datetime.now()
cadastro={}

cadastro['nome']=str(input("Digite seu nome "))
cadastro['ano']=int(input("Digite o ano de nascimento  "))
cadastro['carteira']=int(input("Digite o numero da carteira (0 não tem carteira) "))
if cadastro['carteira']!=0:
    cadastro['contrato'] = int(input("Digite o ano de contratação   "))
    cadastro['salário']=int(input("Digite o salário: R$ "))
    ttrabalho= p.year - cadastro['contrato']
    resta= 35 - ttrabalho
    for k,v in cadastro.items():
        print(f" -{k} tem o valor de {v}")
    if resta >= 0:
        print(f"- Faltam {resta} anos para você se aposentar. ")
else:
    for k,v in cadastro.items():
        print(f"- {k} tem o valor de {v}")