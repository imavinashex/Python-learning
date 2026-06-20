# lest create a company


class Employee:
    company = "Spark" #This is class attribute


    def __init__(self, salary, name, time, company):
        self.salary = salary # crating a instance attribute of name, chatoo_points,time assin it with chatoo.
        self.name = name
        self.time = time
        self.company = company

    def get_salary(self):
        return self.salary
    
     #  this 15 line start methetod 
    def get_info(self):
       print(f"Mr. {self.name},He/She Recived salary {self.salary}, Then How much time He/She in company, {self.time} ")


e1 = Employee(30000, "Naman ash", "1 month", "Spark")

print(e1.company,e1.salary,e1.time) # will always print instance attribute whenever in present.

#my mistake i am using bracket () to print but don't use braket my mistake print(e1.company()) don't  use like that.
print(e1.company)
print(Employee.company) #  This will print class attribute.

e1.get_info() # This is for my method. 

# object introspection
print(dir(e1))