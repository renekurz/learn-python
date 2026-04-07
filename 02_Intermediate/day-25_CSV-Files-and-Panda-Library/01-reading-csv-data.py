# Without CSV Reader
with open("weather_data.csv", mode="r") as data_file:
    data = data_file.readlines()
    print(data) # ['day,temp,condition\n', 'Monday,12,Sunny\n', ...]

# With CSV Reader
import csv

with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file) # CSV Reader Object
    temperatures = []

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(f"\n{temperatures}")

# With Pandas
import pandas

csv_data = pandas.read_csv("weather_data.csv")
print(f"\n{csv_data}")
print(f"\n{csv_data["temp"]}")