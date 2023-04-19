import csv

data = []

with open('/home/bogdan/Рабочий стол/study/mathstat/15/r3z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

