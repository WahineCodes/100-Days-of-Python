

'''Example of unlimited arguments with *'''
def add(*args):
    sum = 0

    #args would be tuples so need to loop to get them separateds
    for n in args:
        sum += n
    return sum
    

# print(add(3, 4, 5, 6, 7, 8))


'''Many Keyword Arguments with **kwargs'''

#Creates a dictionary presents the key and value
def calculate(n, **kwargs):
    print(kwargs)

    #Tap into individual items
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    #alternative way to specify what kwargs you want
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:

    #**kw all the optional arguments
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

        #Get makes sure that it works but doesn't get an error
        #It means that if there is no specify in calling it then it'll just say None
        self.color = kw.get("color")
    

my_car = Car(make="Nissan", model="GT-R")

#You need to specify or else it will crash
print(my_car.model)
