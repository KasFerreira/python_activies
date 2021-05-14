
num=int(input(" Quer ver a tabuada de qual numero? "))

while num > 0:
    print("="*10)
    for x in range(0,10):
     print(f"{num} x {x} = {num*x}")
    print("="*10)     
    num=int(input(" Quer ver a tabuada de qual numero? "))


