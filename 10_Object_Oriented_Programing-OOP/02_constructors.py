


class party_member:

    def __init__(self, name, chatoo_points, time):
        self.name = name  # crating a instance attribute of name, chatoo_points,time assin it with chatoo.
        self.chatoo_points = chatoo_points
        self.time = time


    def chatoo(self): 
     return self.chatoo_lord # in code line 4 to 13  called constructors 
    
    #  this 15 line start methetod 
    def get_info(self):
       print(f"The name of party cjp member chatoo {self.name}, \n And He/She Recived Chatoo Point {self.chatoo_points}, Then How much time He/She in chatoo karta, {self.time} "
              )

c1 = party_member("Abhijit Dipk chatoo", 90,  "5 year")

c1.get_info()