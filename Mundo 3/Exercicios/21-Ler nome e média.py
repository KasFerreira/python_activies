'''alunos={}
sala=[]
while True:
    alunos['Nome']=str(input("Digite o nome do aluno:  "))
    alunos['Média']=float(input(f"Digite a média do {alunos['Nome']}: "))
  #  alunos['Aprovado']=bool(input(f"Digite o status do {alunos['Nome']} "))
    resp=str(input("Deseja cadastrar mais alunos? [S/N]  "))
    sala.append(alunos.copy())
    if resp in 'Nn':
        break
print()
print(f'{"Boletim":^50}')
for x in sala:
    print('-=-' * 15)
    for k,v in x.items():
        print(f'{k}:{v}')'''
alunos={}

while True:
    alunos['Nome']=str(input("Digite o nome do aluno:  "))
    alunos['Média']=float(input(f"Digite a média do {alunos['Nome']}: "))
    if alunos['Média'] <= 5:
        alunos['Status'] = 'Reprovado'
    else:
        alunos['Status'] = 'Aprovado'
    print("*"*10)
    print(f"O nome é igual a {alunos['Nome']}\nA média é igual a {alunos['Média']}\nO o status é {alunos['Status']}")
    print("*" * 10)
    resp = str(input("Deseja cadastrar mais alunos? [S/N]  "))
    if resp in 'Nn':
        break
