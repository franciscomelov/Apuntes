from random import randint
import os
clear = lambda: os.system('cls')



def run():
    print("Adivina el número")
    print("""Escoje la dificultad
    [1] - facil
    [2] - dificil""")
    level = int(input("dificultad: "))
    
    print("Adivina el numero escondido, del 1 al 100")
    print("Si quieres rendirte ingresa el numero 0")

    counter = 0
    hidden_number = randint(0, 100)

    while True:

        print(hidden_number)
        
        player_guess = int(input("Mi numero es: "))
        

        if player_guess > hidden_number:
            clear()
            print("Tu numero es muy alto")
        elif player_guess < hidden_number:
            clear()
            print("Tu numero es muy bajo")
        else:
            print(f"Felicidades adivinanste es {counter} intentos")
            break

        
        counter += 1
        if player_guess == 0:
            break

    print("Adios")


if __name__ == "__main__":
    run()