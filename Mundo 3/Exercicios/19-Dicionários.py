'''lista=[]
pessoas={'nome': 'Lucas', 'sexo': 'Masculino', 'idade': 25}
lista.append(pessoas)
print(f'O {pessoas["nome"]}  tem {pessoas["idade"]} anos')
del pessoas['sexo']
for k,v in pessoas.items():
    print(f'{k}: {v}')'''

'''brasil=[]
estado1={'uf':'Bahia', 'capital':'Salvador', 'população':23000000}
estado2={'uf':'Parana', 'capital':'Curitiba', 'população':33000000}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['capital'])'''

estado={}
brasil=[]
for a in range(0,3):
    estado['Uf'] = str(input("Digite o nome do estado "))
    estado['sigla']= str(input("Digita a sigla do estado  "))
    brasil.append(estado.copy())
print(brasil)
print("-="*30)
for x in brasil:
    for k,v in x.items():
        print(f'{k}: {v[0]}')