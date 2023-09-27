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
# print(data["temp"])

#Checks the data type: Series or DataFrame
#Data Frame: the whole spreadsheet 
# print(type(data)) 

#Series Object: single column in your data
# print(data["temp"])


#Dictionaries: taken each column in table to create dictionaries
data_dict = data.to_dict()
# print(data_dict)


#Series conversion: Turns series into a python list
#Enables me to manipulate the data as if it were a list. Ex. len()
temp_list = data["temp"].to_list()
# average = sum(temp_list)/len(temp_list)
# print(average)

average = data["temp"].mean()

max = data["temp"].max()

'''Get Data in Columns
'''#data["column name"].pandas function()

#Ex1: selection of column
data["condition"]

#Ex2: selection of column
data.condition

'''How to get Data in Rows'''

#data[column name == row name]
data[data.day == "Monday"]

#Pulls out the row with the highest temperature 
max_temp_row = data[data.temp == data["temp"].max()]

monday = data[data.day == "Monday"]

#Gets the specific condtion for the day
monday.condition

#Monday temperature - celsius to fahrenheit
monday_temp = (monday.temp) * (9/5) + 32
# print(monday_temp)


'''Create a dataframe from scratch'''
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# data.to_csv("path you want to save teh file ")
data.to_csv("Day41/new_data.csv")