print('-='*20)
print("controle de terrenos")
print('-='*20)


def area(wid, len):
    a= wid*len
    print(f'A area do terreno é: {a}m²')



wid=float(input("Largura em [m]  "))
len=float(input("Comprimento"))
area(wid,len)