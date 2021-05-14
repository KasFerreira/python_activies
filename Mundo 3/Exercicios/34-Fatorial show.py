
def fatorial(n,show=False):
   f=1
   for x in range(n,0,-1):

       if show == True:
            print(f" {x} ",end="")
            if x>1:
                print("x",end="")
            else:
                print(" = ",end="")

       f*=x

   return f


print(fatorial(4,True))
