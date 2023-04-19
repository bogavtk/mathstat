import csv
from scipy.stats import t
from math import sqrt

data = []

with open('/home/bogdan/Рабочий стол/study/mathstat/15/r3z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

n = len(data)
df = n - 1

alpha = 0.01
mean = sum(data) / n

variance = sum((x - mean) ** 2 for x in data) / n
sigma = sqrt(variance)

standard_mean_error = sigma / sqrt(df)

t_alpha = t.ppf(1 - alpha / 2, df)

mu_lower = mean - standard_mean_error * t_alpha

mu_higher = mean + standard_mean_error * t_alpha

print(f"Объем выборки: {n}")
print(f"Выборочное среднее: {mean}")
print(f"Стандартная ошибка среднего: {standard_mean_error}")


print(f"нижняя граница = {mu_lower}, верхняя граница = {mu_higher}, ")
print(f"Доверительный интервал при двусторонней доверительной границе: ({mu_lower}, {mu_higher})")