import csv

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r2z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

# x = np.linspace(min(data), max(data), 100)
# cdf = stats.t.cdf(x, len(data) - 1)
# plt.plot(x, cdf, label='Функция распределения')
#
# # Строим график эмпирической функции распределения (ЭФР)
# x_sorted = np.sort(data)
# y = np.arange(1, len(data) + 1) / len(data)
#
# # Строим график ЭФР
# plt.step(x_sorted, y, label='ЭФР')
#
# plt.legend()
# plt.show()