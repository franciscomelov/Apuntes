# imprimir numeros del uno al mil
# range()
# range(inicio, final -1, saltos)

contador = 1
print(contador)
while contador < 1000:
    contador += 1
    print(contador)

# Los codigos hacel lo mismo

for i in range(1, 1001):
    print(i)

a = range(1000)
print(a)
# range(0, 1000)
a = list(range(1000))
# list() convierte range() auna lista
# [0, 1, 2, 3..., 999]

for i in range(10):
    print(i * 10)
