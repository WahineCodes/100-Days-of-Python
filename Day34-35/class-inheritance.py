

class Animal:
    def __init__(self):
        self.num_eyes = 2

    #method of the class
    def breath(self):
        print("Inhale, exhale.")

#Inheritance class is in the () after Animal
#Fish class has all access to all the attributes and methods in the Animal class.
class Fish(Animal):
    
    #Allows anything in the fish class to inherit,
    #whats in the Animal class with super()
    def __init__(self):
        super().__init__()

    #Takes the method of breath from Animal class, but adds stuff unique to Fish class
    def breath(self):
        super().breath()
        print("doing this underwater")


    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.breath()