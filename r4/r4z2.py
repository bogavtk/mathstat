import csv

from matplotlib import pyplot as plt

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r4z2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = [(float(row[0]), float(row[1])) for row in reader]

n = len(data)

# Вычисление среднего значения
mean_x = sum([x for x, y in data]) / n
mean_y = sum([y for x, y in data]) / n

# Вычисление дисперсии и среднего отклонения
biased_variance_x = sum([(x - mean_x) ** 2 for x, y in data]) / n
standard_deviation_x = biased_variance_x ** 0.5

biased_variance_y = sum([(y - mean_y) ** 2 for x, y in data]) / n
standard_deviation_y = biased_variance_y ** 0.5

# Выборочный коэф кореляции
r = sum([(x - mean_x) * (y - mean_y) for x, y in data]) / (n * standard_deviation_x * standard_deviation_y)

# Коэф регрессии

b_xy = (r * standard_deviation_x) / standard_deviation_y

y_1 = 78
x_1 = mean_x + b_xy * (y_1 - mean_y)

y_2 = 90
x_2 = mean_x + b_xy * (y_2 - mean_y)     

k = b_xy
b = mean_x - b_xy * mean_y

# Поиск X по Y
Y = 82
X = k * Y + b
print(X)

list_x = [x_1, x_2]
list_y = [y_1, y_2]

# Построение графика рассеяния данных и линии регрессии
plt.scatter([x for x, y in data], [y for x, y in data], color='blue', label='Данные')
plt.plot(list_x, list_y, color='red', label='Регрессия')
plt.plot(x_1, y_1, 'o', color='green')
plt.plot(x_2, y_2, 'o', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
