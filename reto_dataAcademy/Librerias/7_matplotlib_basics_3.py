import matplotlib.pyplot as plt


prices = [1000, 2300, 3001, 3450, 4200, 4780, 5100, 5500, 6000, 7500]
bins = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

plt.hist(prices, bins)
plt.show()