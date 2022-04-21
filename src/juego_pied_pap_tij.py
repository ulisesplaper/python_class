''' Name
    piedra_papel_tijera.py
VERSION
        1.0
AUTHOR
        Victor Ulises Plascencia Perez
DESCRIPTION
    Jugar el juego "piedra o papel o tijera" contra la computadora.
USAGE
    py piedra_papel_tijera.py
ARGUMENTS
    none
SEE ALSO
    none
GitHub link
    https://github.com/ulisesplaper/python_class/blob/master/src/juego_pied_pap_tij.py     
'''
import random

# Definir las opciones validas
valid_options = ["piedra", "papel", "tijera"]

# Solicitar al usuario una eleccion valida
user_choice = input("Tu turno de elegir: ¿piedra, papel o tijera?\n").lower()
if (user_choice in valid_options):

    # Calcular la eleccion de la computadora
    computer_choice = random.choice(valid_options)

    # Imprimir las elecciones del usuario y computadora
    print(f"Tu elegiste: {user_choice}")
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
                "Suerte para la proxima, parece que la computadora es mas habil que tu!")

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
                "Suerte para la proxima, parece que la computadora es mas habil que tu!")

    # Si la eleccion del usuario es "papel"
    # Si la eleccion de la computadora es "piedra"
    # Imprimir "usuario gana"
    # Si la eleccion de la computadora no es "piedra"
    # Imprimir "computadora gana"
    elif(user_choice == "papel"):
        if(computer_choice == "piedra"):
            print("Felicidades!!! Le ganaste a la computadora!")
        else:
            print("Suerte para la proxima, parece que la computadora es mas habil que tu")

else:
    print("Vamos, se que conoces el juego, solo elige piedra, papel o tijera")
