# Intrucción(es)
#Marcus Cubitus y Julius Humerus juegan esta vez a ver quién alcanza antes una puntuación determinada. Una vez decidido el número de puntos a alcanzar o superar, cada jugador lanza un dado hasta que haya conseguido el objetivo. El jugador que haya necesitado menos tiradas es el ganador.

# Ejemplo
# ¿Cuántos puntos hay que conseguir? 4
# Tiradas de Cubitus: 5
# Cubitus ha conseguido el objetivo en 1 tirada.
# Tiradas de Humerus: 2 3
# Humerus ha conseguido el objetivo en 2 tiradas.
# Ha ganado Cubitus.
import random


def juego_dados_v2():
    print("===========================")
    print("     Juego de Dados v2     ")
    print("===========================")
    pts_winner = int(input("\n¿Cuántos puntos hay que conseguir? "))

    tiradas_player1 = []
    num_lances_player1 = 0

    tiradas_player2 = []
    num_lances_player2 = 0

    valores_dado = [1, 2, 3, 4 ,5 ,6]
    i = 1

    player1 = input("\nNombre del Player1: ")
    player2 = input("\nNombre del Player2: ")

    suma_player1 = 0
    suma_player2 = 0

    while suma_player1 < pts_winner:
        num_dados_player1 = random.choice(valores_dado)
        tiradas_player1.append(num_dados_player1)
        suma_player1 = sum(tiradas_player1)
        num_lances_player1 += 1
        if suma_player1 > pts_winner:
            print(f"\nTiradas de {player1}: {tiradas_player1}")
            print(f"\n{player1} ha conseguido el objetivo en {num_lances_player1} tiradas")
        
    while suma_player2 < pts_winner:
        num_dados_player2 = random.choice(valores_dado)
        tiradas_player2.append(num_dados_player2)
        suma_player2 = sum(tiradas_player2)
        num_lances_player2 += 1
        if suma_player2 > pts_winner:
            print(f"\nTiradas de {player2}: {tiradas_player2}")
            print(f"\n{player2} ha conseguido el objetivo en {num_lances_player2} tiradas")

    if num_lances_player1 == num_lances_player2:
        print("\n¡Han Empatado!")
    elif num_lances_player1 > num_lances_player2:
        print(f"\n¡Ha ganado {player2}!")
    else:
        print(f"\n¡Ha ganado {player1}!")


juego_dados_v2()