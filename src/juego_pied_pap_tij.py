''' Name
    juego_pied_pap_tij.py
VERSION
        2.0
AUTHOR
        Victor Ulises Plascencia Perez
DESCRIPTION
    Jugar el juego "piedra o papel o tijera" contra la computadora.
USAGE
    py juego_pied_pap_tij.py
ARGUMENTS
    none
SEE ALSO
    none
GitHub link
    https://github.com/ulisesplaper/python_class/blob/master/src/juego_pied_pap_tij.py     
'''
import random
from timeit import repeat

# Definir las opciones validas
valid_options = ["piedra", "papel", "tijera"]

# Determinar condiciones iniciales del juego y si el usuario quiere repetir
play_again = "si"
while play_again == "si":
    # Solicitar al usuario una eleccion valida
    user_choice = input(
        "Tu turno de elegir: ¿piedra, papel o tijera?\n").lower()
    if (user_choice in valid_options):

        # Calcular la eleccion de la computadora
        computer_choice = random.choice(valid_options)

        # Imprimir las elecciones del usuario y computadora
        print(f"\nTu elegiste: {user_choice}")
        print(f"La computadora eligio: {computer_choice}")

        # Comparar la eleccion de la computadora con la eleccion del usuario
        # Si ambas elecciones son iguales
        # imprimir "empate"
        if(computer_choice == user_choice):
            print("Nada para nadie: empate!!")

        # Si la eleccion del usuario es "piedra"
        # Si la eleccion de la computadora es "tijera"
        # Imprimir "usuario gana"
        # Si la eleccion de la computadora no es "tijera"
        # Imprimir "computadora gana"
        elif(user_choice == "piedra"):
            if(computer_choice == "tijera"):
                print("Felicidades!!! Le ganaste a la computadora!")
            else:
                print(
                    "Suerte para la proxima, parece que la \
computadora es mas habil que tu!")

        # Si la eleccion del usuario es "tijera"
        # Si la eleccion de la computadora es "papel"
        # Imprimir "usuario gana"
        # Si la eleccion de la computadora no es "papel"
        # Imprimir "computadora gana"
        elif(user_choice == "tijera"):
            if(computer_choice == "papel"):
                print("Felicidades!!! Le ganaste a la computadora!")
            else:
                print(
                    "Suerte para la proxima, parece que la \
computadora es mas habil que tu!")

        # Si la eleccion del usuario es "papel"
        # Si la eleccion de la computadora es "piedra"
        # Imprimir "usuario gana"
        # Si la eleccion de la computadora no es "piedra"
        # Imprimir "computadora gana"
        elif(user_choice == "papel"):
            if(computer_choice == "piedra"):
                print("Felicidades!!! Le ganaste a la computadora!")
            else:
                print(
                    "Suerte para la proxima, parece que la \
computadora es mas habil que tu")
    else:
        print("Vamos, se que conoces el juego, solo elige piedra, papel o tijera")

    # Preguntar al usuario si quiere jugar de nuevo
    # Mientras no seleccione una opcion valida, preguntar de nuevo
    play_again = input("\nQuieres seguir jugando?(si/no)\n").lower()
    while play_again not in ["si", "no"]:
        print("\nVamos chico, solo responde si o no sin rodeos. ")
        play_again = input("Quieres seguir jugando?(si/no)\n").lower()
    if play_again == "no":
        print("\nGracias por jugar, vuelve pronto\n")

# Los unicos manejos de errores podrian ser para la eleccion
# del usuario y para determinar si quiere o no seguir jugando
# Al ser muy comun que se cometan errores en este aspecto
# Es mas conveniente usar if/else
