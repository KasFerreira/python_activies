num = (int(input(" Digite um numero  ")),
       int(input((" Digite um numero  "))),
       int(input((" Digite um numero  "))),
       int(input(" Digite um numero  ")))
print(num)
print(f"O numero nove apareceu {num.count(9)} vezes" )
if 3 in num:
    print(f"O numero 3 aparece na  {num.index(3) +1 }ª posição")
else:
    print("O valor três não foi digitado")
    print("Os numeros pares são: ")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")
