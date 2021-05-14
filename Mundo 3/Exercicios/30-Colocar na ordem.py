from time import  sleep
def greater(*num):
    print("Analisando os valores passados...")
    for i,a in enumerate(num):
        if  i == 0:
            maior = a
        else:
            if a > maior:
                maior = a
        print(a,end=' ')
        sleep(0.3)
    print(f"Foram informados {len(num)} valores ", end='')
    print(f'O maior valor informado foi {maior}.')


greater(2,3,1,4,7,8,3)
