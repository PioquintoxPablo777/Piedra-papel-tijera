#desafio
# Se puede colocar el nombre en la segunda solicitud
# lo ingresado por el usuario sea lowercase de tal forma de comparar minuscula con minuscula
# mas de un turno con el bucle  while




nombre01 = input("Como se llamara el Jugador 01: ")
nombre02 = input("Como se llamara el Jugador 02: ")

jugador01 = input("Hola jugador01, que eliges: Piedra, Papel o Tijeras?: ")
jugador02 = input("Hola jugador02, que eliges: Piedra, Papel o Tijeras?: ")

condicion01 = jugador01 == "piedra" and jugador02 == "tijeras"
condicion02 = jugador01 == "tijeras" and jugador02 == "papel"
condicion03 = jugador01 == "papel" and jugador02 == "piedra"


if jugador01 == jugador02:
    print("Ha sido un empate")
elif condicion01 or condicion02 or condicion03:
    print("Ha ganado", nombre01)
else:
    print("Ha ganado", nombre02)