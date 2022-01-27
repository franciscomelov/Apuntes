menu = """
Bienvenido al conversor de monedas 💰
1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos
"""

opcion = input(menu)

if opcion == "1":
    pesos = input("¿Cuantos pesos colombianos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == "2":
    pesos = input("¿Cuantos pesos argentinos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == "3":
    pesos = input("¿Cuantos pesos mexicanos tiene?: ")
    pesos = float(pesos)
    valor_dolar = 20.70
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    pass

