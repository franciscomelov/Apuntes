import pandas as pd


anime_df = pd.read_csv("./data/dataanime.csv")


anime_df.head()  # .head() primeras cinco lineas default


anime_df.head(10)  # Especificndo cuantas lineas mostar "10"

anime_df.tail()  # .tail() muestra las ultimas cinco lineas

anime_df.sample(7)  # .sample(n) muestra n lineas al azar

anime_df.shape  # .shape muestra cuantas filas y columnas hay (1563, 20)

anime_df.size  # multiplica filas * columnas para sacar datos totales

anime_df.info()
# da la cuenta de valores no nulos, el tipo de dato de cada columna
#  (recuerda que solo puede haber un único tipo de dato por columna)
#  y el uso de memoria.

anime_df.describe()  # calcula algunas estadísticas descriptivas para cada columna.



#_-_-_-_-_-_-_-_-_-

anime_df["Title"]  # [nombre columna] retorna datos de la columna especificada

anime_df.columns  # Retorna las columnas

#Se pueden ver estadisticas de cada columna
anime_df["Scored by"].mean()
anime_df["Scored by"].median()
anime_df["Scored by"].std()


