lista= ("Python", "carroça", "Trem", "computador","Macarronada", " Requeijão", "Acerola")
vogais=("a","e","i","o","u")

for a in lista:
    print( f"\n A palavra {a} tem", end=" ")
    for l in a:
        if l.lower() in "aeiou":
            print(l, end=" ")