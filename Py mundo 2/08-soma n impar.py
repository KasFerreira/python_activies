soma = 0
for c in range(1,500,2):
    if c % 3 == 0:
       soma = soma  + c
       print(c, end=" ")
       
print("\n",soma," É a soma de todos os multiplos de 3 entre 0 e 500")