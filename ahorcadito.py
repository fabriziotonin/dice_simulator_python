import random


def hangman():
    words = random.choice(["elefante", "camion", "pelota",
                           "persona", "hipopotamo", "superman"])
    validLetters = "qwertyuiopasdfghjklzxcvbnm"
    turnos = 10
    guess = ""
    while len(words) > 0:
        main = ""
        for letras in words:
            if letras in guess:
                main = main + letras
            else:
                main = main+"_"+" "
        if main == words:
            print(main)
            print("Adivinaste")
            break
        print("Adivina la palabra:", main)
        letra = input()
        if(letra in validLetters):
            guess = guess + letra
        else:
            print("Enter a valid character")
            letra = input()
        if letra not in words:
            turnos -= 1
            if turnos == 9:
                print("quedan 9 turnos")
                print("  --------   ")
            if turnos == 8:
                print("quedan 8 turnos")
                print("  --------   ")
                print("  |          ")
                print("  |          ")
                print("  |          ")
            if turnos == 7:
                print("quedan 7 turnos")
                print("  --------   ")
                print("  |   O      ")
                print("  |          ")
                print("  |          ")
            if turnos == 6:
                print("quedan 6 turnos")
                print("  --------   ")
                print("  |   O      ")
                print("  |   |      ")
                print("  |          ")
            if turnos == 5:
                print("quedan 5 turnos")
                print("  --------   ")
                print("  |   O      ")
                print("  |   |      ")
                print("  |  / \     ")
            if turnos == 4:
                print("quedan 4 turnos")
                print("  --------   ")
                print("  |   O      ")
                print("  |  /|      ")
                print("  |  / \     ")
            if turnos == 3:
                print("quedan 3 turnos")
                print("  --------   ")
                print("  |   O      ")
                print("  |  /|\     ")
                print("  |  / \     ")
            if turnos == 2:
                print("quedan 2 turnos")
                print("  ---|----   ")
                print("  |  |O      ")
                print("  |  /|\     ")
                print("  |  / \     ")
            if turnos == 1:
                print("quedan 1 turnos")
                print("  --|-----   ")
                print("  | |_O_     ")
                print("  |  /|\     ")
                print("  |  / \     ")
            if turnos == 0:
                print("Perdiste :(")
                print("  |\         ")
                print("  | \o       ")
                print("  | /|       ")
                print("  | / \      ")
                break


name = input("Ingresa tu nombre: ")
print(f"Bienvenido {name}")
print("=========================")
print("Tienes 10 intentos para adivinar la palabra")
hangman()
print()
