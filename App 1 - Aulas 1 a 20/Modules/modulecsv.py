import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

# csv.reader(file) is not readable, temos de converter em lista
# data será uma list of lists

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])
