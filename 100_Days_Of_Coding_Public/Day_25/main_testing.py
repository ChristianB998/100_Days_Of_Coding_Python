# with open("weather_data.csv", "r") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     #data.__next__() # skip first row
#     for row in data:
#         if row[1] != "temp":
#             print(row[1])
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data)) # <class 'pandas.core.frame.DataFrame'> is the whole set/data
print(type(data["temp"])) # <class 'pandas.core.series.Series'> colum is more or less a series, much like a list

data_dict = data.to_dict() # turns columns into a dict.
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# get data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0]
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
