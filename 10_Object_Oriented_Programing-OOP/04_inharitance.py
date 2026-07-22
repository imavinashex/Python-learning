# Inheritance: Building Upon Existing Classes

#21/06/2026


class Animal: # Parent class (superclass)
    def __init__(self, name):
        self.name = name


        def speak(self):
            print("Speaking..")

class Dog(Animal): # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self,): # We *override* the speak method (more on this later)
    #  super().speak()
     print("Woof!")

class Cat(Animal): # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

        
# class Dog(Animal):
#     def speak(self):    
#         print("Woof!")

my_dog = Dog("Raka")
my_cat = Cat("Fluffd")

# They both have a 'name' attribute (inherited from Animal)
print(my_dog.name) #output: Raka
print(my_cat.name) #output: Fluffy


# They both have a 'speak' method, but it behaves differently:
# print(my_dog.speak()) # Output: Woof!
print(my_cat.speak()) # Output: Meow!
print(my_dog.speak(), type(my_dog.speak))