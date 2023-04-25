import csv
from math import sqrt

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\15\r3z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

data_square = [x ** 2 for x in data]

n = len(data)

mean = sum(data) / n
mean_square = sum(data_square) / n

sigma = sqrt(mean_square / n)

print(f"Найденое значение оценки параметра σ: {sigma}")