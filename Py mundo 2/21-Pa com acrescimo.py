num =int(input(" Primeiro termo "))
r = int(input(" A razão "))
c= 0
total=0
mais=10

while mais !=0:
    total=total+mais
    while c < total:
        print(num,end=" ->  ")
        num = num+r
        c +=1
    print("pausa")
    mais=int(input( " Deseja digitar mais qts? "))
print("FIM")    
    

        
