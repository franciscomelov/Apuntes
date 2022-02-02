# def imprimir_mensaje():
#     print("Estoy aprendiendo a uar funcoines: ")
#     print("!Estoy aprendiendo a usar funcoines¡")

# # Invocando funcion
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()



# Usando parametros

from unittest import result


def conversacion(mensaje):
    print("hola")
    print("como estas")
    print("mensaje")


opcion = int(input("Elije una opcin (1, 2, 3): "))

if opcion == 1:
    conversacion("Elegiste la opcoin 1")
elif opcion == 2:
    conversacion("Elegiste la opcoin 2")
elif opcion == 3:
    conversacion("Elegiste la opcoin 3")
else:
    print("Elige la opcion correcta")



#________-


def suma(a, b):
    print("Se sumam dos numeros")
    resultado = a + b
    return resultado


sumatoria = suma(1, 2)
print(sumatoria)
