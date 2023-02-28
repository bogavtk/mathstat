import csv

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r1z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(float(row[0]))

sample_size = len(data)
minimum = min(data)
maximum = max(data)
range = maximum - minimum
mean = sum(data) / sample_size
biased_variance = sum([(x - mean) ** 2 for x in data]) / sample_size
unbiased_variance = (biased_variance * sample_size) / (sample_size - 1)
standard_deviation = biased_variance ** 0.5
skewness = sum([(x - mean) ** 3 for x in data]) / (sample_size * standard_deviation ** 3)
median = sorted(data)[((sample_size - 1) // 2)]
q1 = sorted(data)[:sample_size // 2][sample_size // 4]
q3 = sorted(data)[sample_size // 2:][sample_size // 4]
interquartile_range = q3 - q1

print('Объем выборки:', sample_size)
print('Минимум:', minimum)
print('Максимум:', maximum)
print('Размах:', range)
print('Среднее:', mean)
print('Диперсия - Смещенная оценка:', biased_variance)
print('Дисперсия - Несмещенная оценка:', unbiased_variance)
print('Стандартное отклонение:', standard_deviation)
print('Ассиметрия:', skewness)
print('Медиана:', median)
print('Интерквартильная широта:', interquartile_range)

