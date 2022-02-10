import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./studentsperformance.csv")
df.head()
df.columns

bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(df["math score"], bins)
# plt.xlabel("Math score")
# plt.ylabel("Nomber of students")

y = df["math score"]
x = df["reading score"]

plt.scatter(x, y)
plt.xlabel("math score")
plt.ylabel("Reading score")
plt.show()
