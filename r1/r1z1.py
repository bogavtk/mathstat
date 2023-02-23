import csv

data = []

with open(r'C:\Users\Bogdan\Desktop\mathstat\3\r1z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(float(row[0]))

# вычисляем статистические показатели
sample_size = len(data)
minimum = min(data)
maximum = max(data)
range = maximum - minimum
mean = sum(data) / sample_size
biased_variance = sum([(x - mean) ** 2 for x in data]) / sample_size  # смещенная дисперсия
unbiased_variance = sum([(x - mean) ** 2 for x in data]) / (sample_size - 1)  # несмещенная дисперсия
standard_deviation = biased_variance ** 0.5  # стандартное отклонение
skewness = sum([(x - mean) ** 3 for x in data]) / (sample_size * standard_deviation ** 3)  # асимметрию
median = sorted(data)[sample_size // 2]
q1 = sorted(data)[:sample_size // 2][sample_size // 4]
q3 = sorted(data)[sample_size // 2:][sample_size // 4]

interquartile_range = q3 - q1  # интерквартильную широту


print('Sample size:', sample_size)
print('Minimum:', minimum)
print('Maximum:', maximum)
print('Range:', range)
print('Mean:', mean)
print('Biased variance:', biased_variance)
print('Unbiased variance:', unbiased_variance)
print('Standard deviation:', standard_deviation)
print('Skewness:', skewness)
print('Median:', median)
print('Interquartile range:', interquartile_range)
