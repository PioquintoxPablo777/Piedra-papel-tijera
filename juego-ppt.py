nombre01 = input("Como se llamara el Jugador 01: ")
nombre02 = input("Como se llamara el Jugador 02: ")

jugador01 = input("Hola jugador01, que eliges: Piedra, Papel o Tijeras?: ")
jugador02 = input("Hola jugador02, que eliges: Piedra, Papel o Tijeras?: ")

if jugador01 == jugador02:
    print("Ha sido un empate")
elif (jugador01 == "piedra" and jugador02 == "tijeras") or (jugador01 == "tijeras" and jugador02 == "papel") or  (jugador01 == "papel" and jugador02 == "piedra"):
    print("Ha ganado", nombre01)
else:
    print("Ha ganado", nombre02)

#otra forma de ordenarlo

x = "--------------------"
print(x)