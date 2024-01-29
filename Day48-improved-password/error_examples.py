#Example of Catching Exceptions

#EXAMPLE 1
try:
    file = open("Day48-improved-password/a_file.txt")
    a_dictionary  = {"key": "value"}
    print(a_dictionary["key"])

#Note: except block will ignore all errors after the first error it finds in try block.
#to fix that you can specify what type of error except will look for
except FileNotFoundError:
    file = open("Day48-improved-password/a_file.txt", "w")
    file.write("Something")

#gets a hold of the error message that was generated from the except error (except KeyError)
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

#executes when the try block succeeds and there were no exceptions
else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")

    #allows us to raise/make our own exceptions
    raise TypeError("This is an error that I made up.")
# - - - - - - - - - - -- - - - -- - - - - 

#EXAMPLE 2
# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     #raising this error b/c 3m is not a valid height
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)



# - - - - - - - - - - -- - - - -- - - - - 
#TYPES OF ERRORS

#FileNotFound Error, unable to find/read the file b/c mistake in name or path
# with open("a_file.txt") as file:
#     file.read()


#KeyError: Looks for a key that doesnt exist
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

#Index Error: Looking for something not in list. remember it starts at 0
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

#Catching Exceptions
# try: trying to execute code that might cause an exeption
# except: you want to execute if there WAS an exception
# else: Do this if there were NO exceptions
# finally: Do this no matter what happenes