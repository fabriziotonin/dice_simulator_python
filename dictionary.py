import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Quisiste decir %s en vez de:" %
              get_close_matches(word, data.keys())[0])
        decide = input("presiona 'y' para si o 'n' para no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("No existe la palabra buscada")
        else:
            return("Presionaste la tecla equivocada")
    else:
        print("No existe la palabra buscada")


buscador = input("Que palabra quieres buscar: ")
output = translate(buscador)
i = 1
if type(output) == list:
    for item in output:
        print(i, "-", item)
        i += 1
else:
    print(output)
