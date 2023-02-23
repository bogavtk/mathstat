import matplotlib.pyplot as plt
import csv

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r1z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(float(row[0]))

data_sorted = sorted(data)
n = len(data)
ecdf = [i / n for i in range(1, n+1)]

data.sort()

ecdf = []
n = len(data)

for i in range(n):
    ecdf.append((i+1)/n)

plt.step(data, ecdf)
plt.xlabel('Значение')
plt.ylabel('ЭФР')
plt.title('Эмпирическая функция распределения')
plt.show()
