import os
import random
import os
#import ascii_magic


# Esta funcion limpia todo lo contenido en pantalla

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



# Esta funcion crea la imagen ascii mediante el modulo ascii_magic

def showAscii():
    os.system("cls")
    output = ascii_magic.from_image_file("./image/calabaza.jpg", columns=100, char="@")
    ascii_magic.to_terminal(output)


# Esta funcion accede a data y guarda texto aleatorio en una lista

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
            #showAscii()
            clearConsole()
            print("Bienvenido el juego va a comenzar")
            print("La palabra es")
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
    clearConsole()
    print("REGLAS")
    print()
    print("1- Debes adivinar la letra contenida en la palabra")
    print("2- Una vez acertadas todas las letras ganaras")
    print()
    print("3- Tienes un limite de 10 vidas")
    print()



# Esta funcion se encarga de darle funcionalidad al juego

def foundLetter(palabras, palabr_secreta):

    palabra_escogida = random.choice(palabras)
    lista_letras = list(palabra_escogida)
    print(palabra_escogida)

    palabra_secreta = ["-" for i in lista_letras]
    palabra_secreta.pop(-1)

    for i in palabra_secreta:
        print(i, "", end='')

        
    for i in range(0,10):
            letra = input("")

            try:

                if lista_letras.index(letra) >= 0:
                    palabra_secreta[lista_letras.index(letra)] = letra


                    indices_repetidos = [i for i, x in enumerate(lista_letras) if lista_letras.count(
                        x) > 1]  

                    for i in indices_repetidos:  
                        if lista_letras[i] == letra:
                            palabra_secreta[i] = lista_letras[i]
                        else:
                            pass
                        

                    for i in palabra_secreta:
                        print(i, "", end='')
                    print("correct")
        

            except ValueError:

                for i in palabra_secreta:
                    print(i, "", end='')
                print("incorrect")
    checkWin(palabra_secreta)
        


# Esta funcion se encarga de dar el mensaje final si ganaste
def youWin():
    clearConsole()
    print("Felicidades!!!")
    print("Has ganado el juego!!")




# Esta funcion se encarga de dar el mensaje final si perdiste
def youLose():
    clearConsole()
    print("Que triste eres demasiado malo!!!")
    print("Has perdido el juego")




# Esta funcion se encarga de verificar si has ganado o no
def checkWin(palabra_secreta):
    for i in palabra_secreta:
        if i == "-":
            youLose()
            break
        else:
            youWin()
    
    



if __name__ == '__main__':
    menu()
