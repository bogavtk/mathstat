import numpy as np
import csv

filename = r"C:\Users\Bogdan\Desktop\mathstat\3\r2z1.csv"
x_elem = []
y = []
with open(filename, "r") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        x_elem.append(row[0])
        y.append(float(row[1]))

x = [float(x) for x in x_elem if x != ""]


def kolmogorov_smirnov_test(x, y, alpha):
    """
    Функция для проведения КС-теста без использования библиотек
    x: выборка 1
    y: выборка 2
    alpha: уровень значимости
    """
    n1 = len(x)
    n2 = len(y)
    n = n1 + n2

    # объединяем две выборки и сортируем их
    merged_data = np.sort(np.concatenate([x, y]))

    # рассчитываем эмпирическую функцию распределения (ECDF) для каждой выборки
    ecdf_x = np.searchsorted(x, merged_data, side='right') / n1
    ecdf_y = np.searchsorted(y, merged_data, side='right') / n2

    # рассчитываем значение статистики КС
    d = np.max(np.absolute(ecdf_x - ecdf_y))

    # рассчитываем критическое значение статистики КС
    c_alpha = np.sqrt(-0.5 * np.log(alpha / 2)) / np.sqrt(n)

    # сравниваем значение статистики КС с критическим значением и принимаем решение
    if d > c_alpha:
        return False
    else:
        return True


print(kolmogorov_smirnov_test(x, y, 0.01))
