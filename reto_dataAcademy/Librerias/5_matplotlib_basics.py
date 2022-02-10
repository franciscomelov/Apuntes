import matplotlib.pyplot as plt

x = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
y = [1, 2, 5, 10, 21, 40, 54]

plt.plot(x, y, marker="*", linestyle=':', color="g")
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.title("Revenue per year")

plt.show()

