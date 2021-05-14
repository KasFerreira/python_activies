from time import time, sleep
from tqdm import tqdm

    
uSexo = str(input(" DIgite seu sexo  "))
sexo = ["m","f"]
while uSexo not in sexo:
    uSexo = str(input("Digite novamente, valor inválido. \n  "))
else:
    print("Parabéns!! \n carregaremos os dados... ")
    for p in range(1,10,1):
     print(".", end =" ")
    for i in tqdm(range(10),unit=' Peta',bar_format="Secret: {l_bar}{bar}{r_bar}"):
     sleep(0.5)   