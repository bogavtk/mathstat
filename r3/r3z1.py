import csv
from math import sqrt

data = []

with open('/home/bogdan/Рабочий стол/study/mathstat/3/r3z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

data_square = [x ** 2 for x in data]

n = len(data)
mean = sum(data) / n

mean_square = sum(data_square) / n

a = mean_square * mean ** 2
b = -2 * a
c = -mean ** 2

tetta = 2

diskr = b ** 2 - 4 * a * c
tetta_1 = (-b + sqrt(diskr)) / (2 * a)
tetta_2 = (-b - sqrt(diskr)) / (2 * a)

if tetta_1 > tetta:
    tetta = tetta_1
    print(f"Нужный параметр θ: {tetta}")
elif tetta_2 > tetta:
    tetta = tetta_2
    print(f"Нужный параметр θ: {tetta}")
else:
    print("Ни один из параметров θ не подходит")


x_0 = (mean * (tetta - 1)) / tetta

print(f"Нужный параметр x_0: {x_0}")
