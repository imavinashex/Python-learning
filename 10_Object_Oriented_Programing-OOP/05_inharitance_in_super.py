# Inheritance: Building Upon Existing Classes
# In this part two of inharitance i am learing "Super "

"""Disscription About super for me.

Super() : Inside a child class, super() lets you call methods from the parent
class. This is useful when you want to extend the parent’s behavior instead of
completely replacing it. It’s especially important when initializing the parent
class’s part of a child object.


"""

# class Animal: # Parent class (superclass)
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Speaking..")

# class Dog(Animal):# Parent class (superclass)
#     def speak(self):
#         super().speak()
#         print("Woof")

# d = Dog("Raka")
# d.speak()


class Human:
    def __init__(self, name):
      self.name = name
    def speak(self):
       print("Ajay Speaking...")
class man(Human):
   def speak(self):
      super().speak()
      print("Hello")

Name = man("Ajay")
Name.speak()