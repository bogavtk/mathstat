import csv
from scipy.stats import t
from math import sqrt

data = []

with open('/home/bogdan/Рабочий стол/study/mathstat/1/r3z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

n = len(data)
df = n - 1

alpha = 0.025

mean = sum(data) / n

variance = sum((x - mean) ** 2 for x in data) / n
sigma = sqrt(variance)

standard_mean_error = sigma / sqrt(df)

t_alpha = t.ppf(1 - alpha, df)

mu_lower = mean - standard_mean_error * t_alpha

print(f"Объем выборки: {n}")
print(f"Выборочное среднее: {mean}")
print(f"Стандартная ошибка среднего: {standard_mean_error}")

print(f"Нижняя доверительная граница: μ = {mu_lower}, ")
print(f"Доверительный интервал при нижней доверительной границе: ({mu_lower}, ∞)")