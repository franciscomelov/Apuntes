# str()
# int()
# input()

numero = input("Escribe un numero: ")
# Python imprimira en pantalla
# >Escribe un numero:
# Dndo la opcion de ingresar un numero desde el teclado

# Pero este numero
# enluh¿gar de ser reconocido como un numero
# sera reconocido como texto

# por lo cual es necesario convertir
# de texto a un numero entero

numero = int(numero)

numero_decimal = 4.5
# int() tambien funciona
# pasando de float a entero

print(int(numero_decimal))
# > 4

# Tambien es posible convertir de
# numero a texto
numero_decimal = str(numero_decimal)
# Ahora numero_decimal sera tratado
# como texto por lo cual no se podran hacer
# operaciones y tratarlo como un decimal


