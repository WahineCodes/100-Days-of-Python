'''
TITLE: Dictionaries and Lists
DESCRIPTION: A look at how Dictionaries and Lists are used together. 
'''

#Dictionary that contains keys and values that range from str, int, and lists. 
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#Function that adds to the dictionary above. 
def add_new_country(country_visit, visits_visit, cities_visit):
    new_dictionary = {}
    new_dictionary["country"] = country_visit
    new_dictionary["visits"] = visits_visit
    new_dictionary["cities"] = cities_visit

    travel_log.append(new_dictionary)

add_new_country("Spain", 2, ["Barcelona", "Madrid"])
print(travel_log)
