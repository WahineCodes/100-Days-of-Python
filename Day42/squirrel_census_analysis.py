import pandas

#Reads the CSV file with the Data
data = pandas.read_csv("Day42/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

#Extracts the specific fur color from the PrimaryFurColor column
grey_fur_count = len(data[data.PrimaryFurColor == "Gray"])
red_fur_count = len(data[data.PrimaryFurColor == "Cinnamon"])
black_fur_count = len(data[data.PrimaryFurColor == "Black"])

#Prints the amount for each squirrell fur count
print(f"Number of Grey Fur: {grey_fur_count}")
print(f"Number of Red Fur: {red_fur_count}")
print(f"Number of Black Fur: {black_fur_count}")


#Creates a Dictionary for the Fur Color and Count
data_fur_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_fur_count, red_fur_count, black_fur_count]
}

#Creates a dataframe of the data_fur_count dictionary
df = pandas.DataFrame(data_fur_count)

#Creates a new csv file of the dataframe
df.to_csv("Day42/squirell_count.csv")