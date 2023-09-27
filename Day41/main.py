#Option-1
#Turns the weather_data into a list
# with open("Day41/weather_data.csv") as data_file:
#     weather_data = data_file.readlines()
#     print(weather_data)



#Option-2
#Built-in library
# import csv

# with open("Day41/weather_data.csv") as data_file:
#     #reader() can read it and output data
#     data = csv.reader(data_file)
#     temperatures = []
#     #Turns the data into a list by row
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))



import pandas

data = pandas.read_csv("Day41/weather_data.csv")
#Pandas gives a nice row of the data
# print(data)

#It takes the first row and then applies it to the rest
#It also just needs that one name to find the equivalent data
print(data["temp"])