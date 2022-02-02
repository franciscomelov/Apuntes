nombre = input("¿Cual es tu nombre?: ")
nombre.upper()
# paco -> PACO

# Los meotodos retornan algo pero no transforman 
# la cadena inicial


nombre.capitaliza()
# paco -> Paco

nombre = nombre.capitalize()

nombre = nombre.strip()
# "paco  " -> "paco"

nombre = nombre.lower()
# PACO -> paco

nombre = nombre.replace("o", "a")
# paco -> paca

nombre = "paco"
nombre[0]
# p
nombre[1]
# a

letra = nombre[2]
letra
# c

len(nombre)
# 4

len(letra)
# 1

len("Hola! este es el curso de python")
# 32






