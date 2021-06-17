import os
import random
import ascii_magic


# Esta funcion crea la imagen ascii mediante el modulo ascii_magic

def showAscii():
    # Este codigo convierte la imagen a codigo ascii
    os.system("cls")
    output = ascii_magic.from_image_file("./image/calabaza.jpg", columns=100, char="@")
    ascii_magic.to_terminal(output)


# Esta funcion guarda las palabras de data en una lista

def read():
    palabra_secreta = []
    palabras = []

    with open("./files/data.txt", "r", encoding="utf-8") as f:  # aqui guardamos el archivo data en un una lista
        for line in f:
            palabras.append(line)
        foundLetter(palabras, palabra_secreta)



# esta funcion se encarga de las funcionalidades basicas del menu

def menu():
    while True:
        print("1. Comenzar juego")
        print("2. Ver reglas")
        print("3. Salir")

        usuario_uno = int(input("Escoge una de estas 3 opciones "))

        if usuario_uno == 1:
            showAscii()
            read()
            break

        elif usuario_uno == 2:
            showRules()

        elif usuario_uno == 3:
            print("Gracias por jugar...")
            break

        else:
            print("Opcion invalida")


# Esta funcion muestra las reglas del juego

def showRules():
    pass



# Esta funcion se encarga de darle funcionalidad al juego

def foundLetter(palabras, palabr_secreta):
    palabra_escogida = random.choice(palabras)
    lista_letras = list(palabra_escogida)

    print("Bienvenido el juego va a comenzar")
    print("La palabra es")
    print(palabra_escogida)

    palabra_secreta = ["-" for i in lista_letras]
    palabra_secreta.pop(-1)

    for i in palabra_secreta:
        print(i, "", end='')

    while True:

        letra = input("")

        try:

            if lista_letras.index(letra) >= 0:
                palabra_secreta[lista_letras.index(letra)] = letra

                indices_repetidos = [i for i, x in enumerate(lista_letras) if lista_letras.count(
                    x) > 1]  # encuentra palabras repetidas, (arreglar el error) y crear la funcion de ganar
                for i in indices_repetidos:
                    palabra_secreta[i] = letra

                for i in palabra_secreta:
                    print(i, "", end='')
                print("correct")


        except ValueError:

            for i in palabra_secreta:
                print(i, "", end='')
            print("incorrect")


def main():
    menu()


if __name__ == '__main__':
    main()
