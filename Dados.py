# rand int = random & int includes 1 and 6
import random

salir = "y"
print("Simulador de dados")
while salir != "s":
    player = random.randint(1, 6)
    pc = random.randint(1, 6)

    if player == 1:
        print(" ---------- ")
        print("|          |")
        print("|     O    |")
        print("|          |")
        print(" ---------- ")
    if player == 2:
        print(" ---------- ")
        print("| O        |")
        print("|          |")
        print("|        O |")
        print(" ---------- ")
    if player == 3:
        print(" ---------- ")
        print("| O        |")
        print("|    O     |")
        print("|        O |")
        print(" ---------- ")
    if player == 4:
        print(" ---------- ")
        print("| O      O |")
        print("|          |")
        print("| O      O |")
        print(" ---------- ")
    if player == 5:
        print(" ---------- ")
        print("| O      O |")
        print("|     O    |")
        print("| O      O |")
        print(" ---------- ")
    if player == 6:
        print(" ---------- ")
        print("| O      O |")
        print("| O      O |")
        print("| O      O |")
        print(" ---------- ")
    if (pc > player):
        print(f"La pc gano {pc}  vs  {player}")
    elif pc == player:
        print(f"Empate {player} vs pc {pc}")
    else:
        print(f"Ganaste {player} vs pc {pc}")
    salir = input(
        "Si quiere salir presione 's', para tirar otra vez presione cualquier tecla")
