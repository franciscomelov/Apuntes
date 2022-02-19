# Nos permite guardar varios valores en una sola variable

numero = 3

otro_numero = 4

numeros = [1, 2, 3, 4, 5, 5, 6, 1]
print(numeros)
# [1, 2, 3, 4, 5, 5, 6, 1]

objetos = ["hola", 2, True, "a", 2.5]

# Accediendo a los elementos

lista = ["a", "b", "c"]
lista[0]
# a

lista[1]
# b

lista[3]
# IndexError

# AÑADIENDO A UNA LISTA
lista = ["a", "b", "c"]
objetos.append(1)

lista
["a", "b", "c", 1]

lista[3]
# 1

# BORRANDO DE LA LISTA
objetos = ["a", "b", "c", 1]

objetos.pop(1)

lista
# ["a", "c", 1]


