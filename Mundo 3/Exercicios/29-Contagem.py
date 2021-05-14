from time import sleep
def contador(a,b,c):
    '''
    fd


    :param a: Inicio da contagem
    :param b: Fim da contagems
    :param c: Passo
    :return: retorna a contagem
    '''
    print('-='*10)
    print("Contagem de 1 a 10, passo 1.")
    for y in range (a,b,c):
        print(y,end=' ')
        sleep(0.5)

    print("fim",end=" ")
    print()
    print('-='*10)
    print("Contagem de 10 a 1, passo 2")
    for x in range (b,a,-2):
        print(x, end=' ')
        sleep(0.5)
    print("fim", end=" ")
    print()
    print('-=' * 10)
    print("Agora é sua vez de iniciar a contagem: ")
    for a in range(int(input("Inicio: ")),int(input("Fim: ")), int(input("Passo "))):
        print(a,end=" ")
        sleep(0.5)




contador(1,10,1)
help(contador)
