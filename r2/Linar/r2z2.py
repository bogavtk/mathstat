import csv
from scipy.stats import norm, kstwobign, kstest, expon
from math import sqrt, exp, log
import numpy as np
import matplotlib.pyplot as plt

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\15\r2z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

n = len(data)
df = n - 1
data.sort()

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

mu = 0.5
sigma = sqrt(1.5)

lambda_ = 1.5
cdf_values = norm.cdf(data, mu, sigma)
alpha = 0.05

list_of_D_n = []
for i in range(0, len(data)):
    list_of_D_n.append(abs(emperic_function[i] - cdf_values[i]))

D_n = max(list_of_D_n)

t_stats = D_n
critical_const = kstwobign.ppf(1 - alpha)

D, _ = kstest(data, norm.cdf, args=(0, 1 / 1.5))
p_value = 1 - norm.cdf(np.sqrt(n) * D)

print(f'Статистика: D = {D * sqrt(n)}, p-value = {p_value}')
print(f'Критическая константа: {critical_const}')

if t_stats > critical_const:
    print('Отвергаем H0')
elif t_stats < critical_const:
    print('Не отвергаем H0')

if p_value > alpha:
    print("Гипотеза 0 не можем отвергнуть")
else:
    print("Гипотеза 0 отвергается")




x, y = ecdf(data)

# Вычисляем функцию плотности вероятности нормального распределения
mu, sigma = np.mean(data), np.std(data)
x_pdf = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
y_pdf = norm.pdf(x_pdf, mu, sigma)

# Строим графики
fig, ax1 = plt.subplots()

# График эмпирической функции распределения
ax1.plot(x, y, 'b.', markersize=5, label='Эмпирическая ЭФР')
ax1.set_xlabel('X')
ax1.set_ylabel('Кумулятивная вероятность')
ax1.legend(loc='lower right')

# График функции плотности вероятности нормального распределения
ax2 = ax1.twinx()
ax2.plot(x_pdf, y_pdf, 'r-', label='Нормальное распределение')
ax2.set_ylabel('Плотность вероятности')
ax2.legend(loc='upper right')

plt.title('ЭФР и нормальное распределение')
plt.show()
