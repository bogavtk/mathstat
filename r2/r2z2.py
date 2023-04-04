import csv
from scipy.stats import expon, kstwobign, kstest, ksone
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r2z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

n = len(data)
data.sort()


def exp_cdf(x):
    return expon.cdf(x, scale=1 / lambda_)


def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1) / len(data)
    return x, y


def emperical_func(X):
    cdf_vals = []
    counts = {}
    cumulative_count = 0

    for x in X:
        counts[x] = counts.get(x, 0) + 1

    for x in sorted(counts):
        cumulative_count += counts[x]
        cdf_vals.append(cumulative_count / len(X))

    return cdf_vals


emperic_function = emperical_func(data)


lambda_ = 1.5
expon_func = expon.cdf(data, scale=1 / lambda_)
alpha = 0.01

list_of_D_n = []

for i in range(0, len(data)):
    list_of_D_n.append(abs(emperic_function[i] - expon_func[i]))

D_n = max(list_of_D_n)

t_stats = D_n
critical_const = kstwobign.ppf(1 - alpha)

D, _ = kstest(data, expon.cdf, args=(0, 1 / 1.5))
p_value = 1 - expon.cdf(np.sqrt(n) * D)

print(f'Статистика: D = {D_n}, p-value = {p_value}')
print(f'Критическая константа: {critical_const}')

if t_stats > critical_const:
    print('Отвергаем H0')
elif t_stats < critical_const:
    print('Не отвергаем H0')

if p_value > alpha:
    print("Гипотеза 0 не можем отвергнуть")
else:
    print("Гипотеза 0 отвергается")

# Вычисление эмпирической функции распределения


# Построение графиков ЭФР и функции распределения
x, y = ecdf(data)
f = np.linspace(0, 5, 100)
plt.plot(f, exp_cdf(f), 'r-', label='Экспоненциальное распределение')
plt.plot(x, y, 'b.', markersize=5, label='Эмпирическая ЭФР')
plt.xlabel('X')
plt.ylabel('Кумулятивная вероятность')
plt.legend(loc='lower right')
plt.show()
