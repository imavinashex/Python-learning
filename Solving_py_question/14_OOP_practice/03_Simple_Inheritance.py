'''
Simple Inheritance
Create a base class Animal with a method sound() that prints "Some sound" .
Create a derived class Dog that overrides sound() to print "Bark!" .
Create an object of Dog and call sound()

'''

class Animal:
    def animal_sound():
        print("Some Sound")

class Dog:
    def animal_sound():
        print("Bark")

a = Animal
a.animal_sound()

b = Dog
b.animal_sound()