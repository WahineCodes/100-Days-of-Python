''''
Note: How to make a Class
    - attributes - what the object HAS
    - methods - what the object DOES
'''

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    #Methods always needs a self parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "WahineCodes")
user_2 = User("002", "Leilow")

'''object.method(object #2)'''
user_1.follow(user_2)

print(user_1.followers)
#0
print(user_1.following)
#1
print(user_2.followers)
#1
print(user_2.following)
#0



''' examples of what would be printed when calling specific aspects of class'''
#print(user_1.id)
#Prints 001

#print(user_1.followers)
#Will be 0 to begin with until you add follower in code

