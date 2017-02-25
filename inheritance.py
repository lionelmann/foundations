class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        #instance variables
        self.last_name = last_name
        self.eye_color = eye_color

    #instance method
    def show_info(self):
        print("Last Name  = " +self.last_name)
        print("Eye Color = " +self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self): #Method Overriding
        print("Last Name  = " +self.last_name)
        print("Eye Color = " +self.eye_color)
        print("Number of Toys = " +str(self.number_of_toys))
    
        
#create an instance of Parent
billy_cyrus = Parent("Cyrus", "blue")
#billy_cyrus.show_info()
#print(billy_cyrus.last_name)

#create an instance of Child
miley_cyrus = Child("Cyrus", "green", 5)
miley_cyrus.show_info()
#print(miley_cyrus.number_of_toys)



