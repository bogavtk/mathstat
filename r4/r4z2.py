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

# Вычисление коэффициентов регрессии
numerator = sum([(x - mean_x) * (y - mean_y) for x, y in data])
denominator = sum([(x - mean_x) ** 2 for x, y in data])
beta1 = numerator / denominator
beta0 = mean_y - beta1 * mean_x

# Вычисление значения регрессии в заданной точке (например, x = 106)
x = 105
y_pred = beta0 + beta1 * x
x_2 = 127
y_2_pred = beta0 + beta1 * x_2

list_x = [x, x_2]
list_y = [y_pred, y_2_pred]


# Построение графика рассеяния данных и линии регрессии
plt.scatter([x for x, y in data], [y for x, y in data], color='blue', label='Данные')
plt.plot(list_x, list_y, color='red', label='Регрессия')
plt.plot(x, y_pred, 'o', color='green', label=f'Значение регрессии в x={x}: {y_pred:.2f}')
plt.plot(x_2, y_2_pred, 'o', color='green')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()