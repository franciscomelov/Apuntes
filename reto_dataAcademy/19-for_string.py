# for itera sobre cada elemento de un iterable
# un string es un iterable

def run():
    # nombre = input("Escribe tu nombre: ")

    # for letter in nombre:
    #     print(letter)

    # # nombre = hola
    # # h
    # # o
    # # l
    # # a

    frase = input("Escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())
    # frase = abc
    # A
    # B
    # C


if __name__ == "__main__":
    run()
