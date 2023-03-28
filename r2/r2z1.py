import csv
from scipy.stats import t
from math import sqrt

filename = r"C:\Users\Bogdan\Desktop\mathstat\15\r2z1.csv"
x_elem = []
y = []
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        x_elem.append(row[0])
        y.append(float(row[1]))

x = [float(x) for x in x_elem if x != ""]

n1 = len(x)
n2 = len(y)

x_mean = sum(x) / n1
y_mean = sum(y) / n2
print(f"Среднее значение 1 выборки: {x_mean}")
print(f"Среднее значение 2 выборки: {y_mean}")

df = n1 + n2 - 2  # Число степеней свободы

alpha = 0.01

variance_x = sum((x - x_mean) ** 2 for x in x) / n1
variance_y = sum((y - y_mean) ** 2 for y in y) / n2

critical_const = t.ppf(1 - alpha / 2, df)
t_stats = ((x_mean - y_mean) / sqrt(n1 * variance_x + n2 * variance_y)) * (sqrt((n1 * n2 * df) / (n1 + n2)))
abs_t_stats = abs(t_stats)
p_value = 2 * (1 - t.cdf(abs(t_stats), n1 + n2 - 2))

if abs_t_stats > critical_const:
    print('Отвергаем H0')
elif abs_t_stats < critical_const:
    print('Не отвергаем H0')

if p_value > alpha:
    print("Гипотеза 0 не можем отвергнуть => различия между выборками не являются статистически значимыми")
else:
    print("Гипотеза 0 отвергается => различия между выборками статистически значимы")

print(f"Значение t-статистики: {t_stats}")
print(f"Критическая константа: {critical_const}")
print(f"p-value: {p_value}")
