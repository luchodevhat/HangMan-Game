import os
import random
import ascii_magic


# Esta funcion guarda las palabras de data en una lista y ejecuta las funcionalidades del juego
def read():

    palabra_secreta = []
    palabras = []

    with open("./files/data.txt", "r", encoding="utf-8") as f:  # aqui guardamos el archivo data en un una lista
        for line in f:
            palabras.append(line)

        palabra_escogida = random.choice(palabras)
        lista_letras = list(palabra_escogida)

        print(palabra_escogida)
        for size in lista_letras:
            palabra_secreta.append("-")
        palabra_secreta.pop(-1)

        for i in palabra_secreta:
            print(i, "", end='')


    while True:

        letra = input("")

        try:

            if lista_letras.index(letra) >= 0:
                palabra_secreta[lista_letras.index(letra)] = letra   # verificar no reconoce palabaras repetidas
                indices_repetidos = [i for i, x in enumerate(lista_letras) if lista_letras.count(x) > 1] # encuentra indices repetidos

                for i in palabra_secreta:
                    print(i, "", end='')
                print("correct")

        except ValueError:
            print("incorrect")



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
            os.system("cls")
            print("Reglas")
            print("Regla 1: adivinar la palabra")
            print("Regla 2: Tienes un total de 8 vidas")



        elif usuario_uno == 3:
            print("Gracias por jugar...")
            break


        else:
            print("Opcion invalida")


if __name__ == '__main__':
   main()



