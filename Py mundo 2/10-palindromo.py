palavra=str(input("Digite uma palavra sem espaços "))
palavra = ''.join(palavra.split())
t = len(palavra)
lista=[]
l=[]
print(palavra)
for c in range(0,t,1):
   lista += palavra[c]

for c in range(t-1,-1,-1):
  l += palavra[c]    
print(lista, l)