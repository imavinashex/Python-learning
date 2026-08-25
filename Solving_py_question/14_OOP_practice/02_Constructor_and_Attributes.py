"""
Constructor and Attributes.


Create a class Person with a constructor ( __init__ ) that accepts name and age
as arguments and stores them as instance attributes.
Create an object and print the person’s name and age.



"""

# Creating class person with a constructor (__init__) that accepts name and age
class person:
    def __init__(self, name ,age ):
        self.name = name  # as arguments and stores thema as instance attribute.
        self.age = age

    def get_info_person(self): #method
        print(f"This Person name is {self.name}, and Person age {self.age}")

p = person("AviXyz",69) #values 

p.get_info_person() #call 