numeros = [1, 2, 3, 4, 5]

numeros.append("hola")

# [1, 2, 3, 4, 5, "hola"]

numeros.pop(5)

# [1, 2, 3, 4, 5]

"hola" + " " + "mundo"
# hola mundo


numeros = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9]

lista_final = numeros + numeros2
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros * 5
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# LAS LISTA OCUPAN MAS MEMORIA PARA GENERAR UNA LISTA

mi_tupla = (1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# una tupla no se puede modificar una vez creadas


# como las listas ocupan mas memoria ya que son dinamicas
# Las tuplas al ser estaticas son mas rapidas
# por ejemplo al iterar sobre las tuplas es mas rapid

