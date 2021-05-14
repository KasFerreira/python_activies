from operator import itemgetter
pessoa={}
grupo=[]
total=0
print("=-"*20)
print("Esse é um programa em que você salva os dados de pessoas e ao final\nele mostra algumas informações"
      " sobre o conjunto dos dados inseridos\n"
      "OBS:\n 1-A medida que preencher os campos pressione ENTER\n 2-Cadastre várias pessoas ")
print("=-"*20)

while True:
    pessoa['nome']=str(input("Nome  "))
    pessoa['idade']=int(input("Idade:  "))

    while True:
         pessoa['sexo'] = str(input("Sexo [M/F]  "))
         if pessoa['sexo']  in 'mMfF':
            break
         else:
            print("ERRO, digite [M/F]")
    grupo.append(pessoa.copy())
    resp=str(input("Deseja continuar [S/N]  "))
    if resp in 'Nn':
        break
print('=-'*15)
print(f'O grupo tem {len(grupo)} pessoas ')
print("=-"*20)
for a in grupo:
  if a['sexo'] in 'Ff':
      print(f"As mulheres são: ", end='')
      break
for a in grupo:
    total=a['idade']+total
    media= total / len(grupo)
    if a['sexo']in 'fF':
         print(f"{a['nome']} ",end='')
print()
print("=-"*20)
print("As pessoas com idade acima da média são: ")
for a in grupo:
       if a['idade'] > media:
            print(f' nome = {a["nome"]}, idade = {a["idade"]}, sexo = {a["sexo"]} ')
print("=-"*20)
print(f"A média de idade do grupo é de {media} anos")
