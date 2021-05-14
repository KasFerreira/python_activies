matriz=[[],[],[]]
total=0
for a in range(0,3):
  for b in range(0,3):
        matriz[a].append(int(input(f"Digite um numero na posição  [{a},{b}]   ")))

for a in range(0,3):
    for b in range(0,3):
         if matriz[a][b] % 2 == 0:
            total+=matriz[a][b]

#print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]} ')

print(f"A soma de todos os valores pares é {total}")
