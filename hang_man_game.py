import os
import random
import ascii_magic


# Esta funcion guarda las palabras de data en una lista y ejecuta las funcionalidades del juego
def read():
    palabras = []

    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
        palabra_escogida = random.choice(palabras)

    for size in palabra_escogida:
        print("_ ", end='')
    print("")

    letra = input("")












# esta funcion se encarga de las funcionalidades basicas del menu
def main():

    while True:
        print("1. Comenzar juego")
        print("2. Ver reglas")
        print("3. Salir")

        usuario_uno = int(input("Escoge una de estas 3 opciones "))

        if usuario_uno == 1:

            # Este codigo convierte la imagen a codigo ascii
            os.system("cls")
            output = ascii_magic.from_image_file("./image/calabaza.jpg", columns=100, char="@")
            ascii_magic.to_terminal(output)

            print("Bienvenido el juego va a comenzar")
            print("La palabra es")
            read()
            break


        elif usuario_uno == 2:
            print(os.system("cls"))
            print("Reglas")
            print("Regla 1: adivinar la palabra")
            print("Regla 2: Tienes un total de 8 vidas")



        else:
            print("Gracias por jugar...")
            break


if __name__ == '__main__':
   main()



