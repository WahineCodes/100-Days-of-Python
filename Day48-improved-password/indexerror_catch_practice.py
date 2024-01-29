#Practice using except so that the program when encountering an error prints Fruit Pie without it crashing.

##Original Code to Fix
# fruits = eval(input())

# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")

# make_pie(4)

#---Solution---
fruits = eval(input())

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
       print("Fruit pie")
    else:
        print(fruit + " pie")

##Raises IndexError on list with less than 5 items
make_pie(4)