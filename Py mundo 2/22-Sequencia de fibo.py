num=int(input("Quantos  "  ))

t1=0
t2=1
cont=3
print("A sequencia é {} -> {}".format(t1,t2),end=" -> ")
while cont <= num:
    t3=t1+t2
    print(t3, end=" -> ")
    cont +=1
    t1=t2
    t2=t3