pesos = input("¿Cuantos pesos mexicanos tiene?: ")
pesos = float(pesos)
valor_dolar = 20.70
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")



dolares = input("¿Cuantos dolares tiene?: ")
dolares = float(dolares)
valor_peso = 0.048
pesos = dolares / valor_peso
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos")

