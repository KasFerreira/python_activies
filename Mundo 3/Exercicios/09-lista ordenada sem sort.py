lista= []
maior=menor=0
for p in range(0,5):
        num=int(input("Digite um numero "))
        if p == 0 or num > lista[-1]:
            lista.append(num)
            print("Adicionado no inicio da listaa")

        else:
            pos=0
            while pos < len(lista):
                if num <= lista[pos]:
                    lista.insert(pos,num)
                    print(f"Adicionado na posição {pos} da lista")
                    break
                pos+=1
print(lista)
