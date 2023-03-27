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

n1 = len(x)
n2 = len(y)

x_mean = sum(x) / n1
y_mean = sum(y) / n2
