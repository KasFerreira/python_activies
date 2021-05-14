from datetime import datetime

agora= datetime.now()
def vota(ano):
    r=agora.year-ano
    if 18<r and r< 65:
        print(f"Com {r} anos: voto é OBRIGATÓRIO")
    elif r>65:
        print(f" com {r} anos: Voto  é OPCIONAL")
    else:
        print(f"O voto com {r} anos: Não é OBRIGATÓRIO")


n=int(input("Digite o ano em que nasceu  "))
vota(n)
