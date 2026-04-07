import pandas

data = pandas.read_csv("weather_data.csv")

print(f"type(data): {type(data)}")
print(f"type(data[\"temp\"]): {type(data["temp"])}\n")

data_dict = data.to_dict()
print(f"data_dict: {data_dict}\n")

temp_list = data["temp"].to_list()
print(f"temp_list: {temp_list}\n")

temp_average = data["temp"].mean()
print(f"temp_average: {temp_average}")

temp_max = data["temp"].max()
print(f"temp_max: {temp_max}\n")

# Get data in columns
print(f"data[\"condition\"]: {data["condition"]}\n")
print(f"data.condition: {data.condition}\n")

# Get data in row
print(f"data[data.day == \"Monday\"]: {data[data.day == "Monday"]}\n")
print(f"data.temp == data.temp.max(): {data[data.temp == data.temp.max()]}\n")

monday = data[data.day == "Monday"]
print(f"monday.condition: {monday.condition}\n")

monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(f"monday_temp_F: {monday_temp_F}\n")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(data_dict)
print(f"student_data: {student_data}\n")

# This will create the student_data.csv file in the current folder
student_data.to_csv("student_data.csv")