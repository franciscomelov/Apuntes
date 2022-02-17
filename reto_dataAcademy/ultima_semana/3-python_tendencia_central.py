import pandas as pd


df = pd.read_csv("cars.csv")

print(df["price_usd"].mean())  # promedio

print(df["price_usd"].median())  # mediana

df["price_usd"].plot.hist(bins=20)

df.show()