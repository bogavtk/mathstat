import matplotlib.pyplot as plt

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r1z1.csv', 'r') as f:
    data = [float(x.strip()) for x in f.readlines()]

# определяем количество интервалов гистограммы
num_bins = 12

# вычисляем минимальное и максимальное значения данных
min_val = min(data)
max_val = max(data)

# вычисляем длину интервала гистограммы
interval_length = (max_val - min_val) / num_bins

# создаем список, содержащий границы интервалов гистограммы
interval_boundaries = [min_val + i * interval_length for i in range(num_bins + 1)]

# создаем список, содержащий частоты вхождения значений в каждый интервал
frequencies = [0] * num_bins
for x in data:
    for i in range(num_bins):
        if x >= interval_boundaries[i] and x < interval_boundaries[i + 1]:
            frequencies[i] += 1
            break

# создаем список, содержащий вероятности вхождения значений в каждый интервал
total_data_points = len(data)
probabilities = [freq / (total_data_points * interval_length) for freq in frequencies]
probabilities = [p / sum(probabilities) for p in probabilities]

# рисуем гистограмму
fig, ax = plt.subplots()
ax.bar(interval_boundaries[:-1], probabilities, width=interval_length, edgecolor='black')

# задаем название графика и подписи осей
ax.set_title('Вероятностная гистограмма')
ax.set_xlabel('Значения')
ax.set_ylabel('Вероятности')

plt.show()
