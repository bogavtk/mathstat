import math
import matplotlib.pyplot as plt
import csv

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r1z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(float(row[0]))

k = math.floor(len(data) / 10)

# строим вероятностную гистограмму
plt.hist(data, bins=k, density=True)
plt.show()