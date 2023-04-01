import csv
from scipy.stats import expon
from math import sqrt

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r2z2.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

n = len(data)
def efr(data):
    n = len(data)
    ecdf = [i / n for i in range(1, n + 1)]
    data.sort()
    ecdf = []
    n = len(data)
    for i in range(n):
        ecdf.append((i + 1) / n)

    return ecdf

ecdf = efr(data)
lambda_ = 1.5
cdf_values = expon.cdf(data, scale=1/lambda_)

list_of_D_n = []

for i in range(0, len(data)):
    list_of_D_n.append(ecdf[i] - cdf_values[i])

D_n = max(list_of_D_n)

F_kolmag = sqrt(n) * D_n
print(F_kolmag)


# Создаем нормальное распределение
# mu, sigma = 0.5, sqrt(1.5)
# X = norm(mu, sigma)
#
# # Задаем диапазон значений аргумента функции
# x = np.linspace(-5, 5, num=1000)
#
# # Вычисляем значение функции плотности в заданных точках
# pdf = X.pdf(x)
#
# # Строим график функции плотности
# plt.plot(x, pdf)
# plt.title("Нормальное распределение, μ=0.5, σ=sqrt(1.5)")
# plt.xlabel("Значения")
# plt.ylabel("Плотность вероятности")
# plt.show()


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
