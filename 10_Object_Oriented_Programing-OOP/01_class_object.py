# class: class is just a blueprint or template. Eg. Form for  a exam that contains name, age, electives, father's name etc.

# object: Spacific instance created from the template (class.) Eg. from  which contains the data for Damodar Godi.

#lets make a program

class party_member:
    party = "CJP"

    def chatu_points(self): # self is inportant here because self referace of the object of the class which being created.
        # print(self)
        return 1000
    

m1 = party_member()  # an object of class Employee is created here
print(m1.chatu_points())

m2 = party_member()
print("abhit Dipksuck Got Points", m2.chatu_points(), "Party Name", m2.party,"(Reward for Chatu karta)")

