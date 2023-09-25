#Found the file with the relative path
#file = open("Day40/my_file.txt")
# contents = file.read()
# print(contents)
# Needs to close the file so it doesn't use your resources
# file.close()


'''Alternative way to open a file using with keyword
With the "with" you don't have to manually write file.close()
It will close itself 

open() is automatically mode to "r" read 

'''
# with open("Day40/my_file.txt") as file:
#     contents = file.read()
#     print(contents)



'''How to write to the file

mode = "w" is write
mode = "a" is append (wont delete what is in the file)


'''
# with open("Day40/my_file.txt", mode="a") as file:
#     file.write("New text.")

'''To create a new file with the open()

But it goes to the main folder, not the folder I'm in


'''
with open("new_file.txt", mode = "w") as file:
    file.write("New Text Dog")