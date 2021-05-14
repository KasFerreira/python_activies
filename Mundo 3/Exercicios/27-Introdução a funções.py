import codecs

''''def escrever(x):
    with open('texto.txt', 'a') as file:
        file.write(x + '\n')
        print(x)

escrever(codecs.decode(input('Digite alguma coisa: '), "unicode-escape"))'''




def dobra(li):
    posicao=0
    while len(li) > posicao:
        li[posicao]*=2
        posicao+=1
    print(li)


x=[3,4,5,2,1]
dobra(x)


def duplica(*valores):
    s= 0
    for num in valores:
        s=num+s
    print(s)


duplica(2,3,5,1)