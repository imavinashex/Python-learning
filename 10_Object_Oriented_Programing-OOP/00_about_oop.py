'''

What  is OOP?

Ansewr- Object-Oriented Programming (OOP) in Python is a programming style that organizes code into classes and objects to represent real-world entities. Instead of just focusing on functions and logic, OOP groups data (attributes) and behaviors (methods) together into self-contained units.

Core Concepts 

Classes: Think of a class as a blueprint or template. 
For example, a Car class defines what a car is (color, model) and what it can do (drive, brake).

Objects: An object is an instance of a class. While the class is the blueprint, the object is the actual house built from that blueprint.

Attributes: Data associated with an object, like car.color = "Red".Methods: Functions defined inside a class that describe the behaviors of an object, like car.drive()



Principles of OOPs Concepts.

1. Class

2. Object

3. Encapsulation

4. Inheritance

5. Polymorphism

6. abstraction


                /\
               //\\
              ///\\\
             ///  \\\
            ///====\\\   
           ///      \\\


'''  


#                 /\
#                //\\
#               ///\\\
#              ///  \\\
#             ///====\\\   
#            ///      \\\

           
# defining class
class Smartphone:
   # constructor    
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand
   
   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description())

#defining class
class Avi:
    #defi
    def __init__(self,Today, DOb):
        self.Today = Today
        self.DOb = DOb

    def discrp(self):
        return f"{self.Today} To {self.DOb} Avi"


rem = Avi("Happy Birthday", "You Dear")

print(rem.discrp())


