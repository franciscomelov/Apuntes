import numpy as np


vector = np.array([1, 2, 4, 8, 16])
# [ 1  2  4  8 16]

matrix = np.matrix([[5, 10], [15, 30]])
# [[ 5 10]
#  [15 30]]

#_-_-_-_-_-_-_-_-_-_-
lista_1 = [100, 200, 300, 400]
lista_2 = [3, 4, 5, 6]

vector_2 = np.array(lista_1)
# [100 200 300 400]

matrix_2 = np.array([lista_1, lista_2])
# [[100 200 300 400]
#  [  3   4   5   6]]


# -_-_-_-_-_

# Size of arrays 

vector.shape
# [ 1  2  4  8 16]
# (5, 0)

matrix_2.shape
# [[100 200 300 400]
#  [  3   4   5   6]]
# (2, 4)

matrix.shape
# [[ 5 10]
#  [15 30]]
# 2, 2

# Para vectores el único valor es la cantidad de elementos en él.
# Para matrices el primer valor son las filas y el segundo las columnas.
# Para un tensor el primer valor es la “profundidad”, el segundo las filas y el tercero las columnas.

#-__--_-_-_-______
# Tipo de dato que esta en el array

vector.dtype
# [ 1  2  4  8 16]
# int32

matrix_2
# [[100 200 300 400]
#  [  3   4   5   6]]
# int32

vector_4 = np.array([1.4, 5.6, 6.8])
vector_4.dtype
# float64

print(matrix_2.dtype)