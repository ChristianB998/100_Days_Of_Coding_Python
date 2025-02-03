import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_counts = data["Primary Fur Color"].value_counts()
print(color_counts)
color_counts.to_csv("squirrel_count.csv")