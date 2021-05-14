
lista = ("Lapís", 2.50, "Caderno", 15.50, "Tesoura", 9.90, "Lapiseira", 3.00, "Classificador", 2.20, "Borracha", 2.00,
        "Grafite", 3.30)
print("-"*40)
print(f'{"Listagem de Preços":^40}')
print("-"*40)
for a in range(0,len(lista)):
      if a % 2 == 0:
        print(f'{lista[a]:.<30} R$ {lista[a+1]:>7.2f}')
print("-"*40)

