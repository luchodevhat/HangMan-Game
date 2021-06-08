import os
import ascii_magic


def read():
    palabra = ""
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        pass



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

            print("Bienvenido....")


        elif usuario_uno == 2:
           # os.system("cls")
            print("Reglas")
            print("Regla 1: adivinar la palabra")
            print("Regla 2: Tienes un total de 8 vidas")



        else:
            print("Gracias por jugar...")
            break


if __name__ == '__main__':
    main()


