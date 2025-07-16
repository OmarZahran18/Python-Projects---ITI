# How super Function handle Multiple Inheritance ? 

class vehicle:
    def v(self):
        print("This Vehicle!")
        

class car(vehicle):
    def c(self):
        print("This Car")
        super().v()

class tesla(car):
    def t(self):
        print("This Tesla")
        super().v()

class tesla_model_3(tesla):
    def m(Self):
        print("This Model 3")
        super().v()

model = tesla_model_3()
model.m()
model.v()
model.t()
model.c()      


# If Human and Mammal Have the same method like eat but with different Implementation
# When Child[Employee] calls eat method 
# different Implementation. When Child[Employee] calls eat method 
# how python handle this case ?

class human:
    def eat(self):
        print ("Human is Eating Fish")
        
class mammal:
    def eat(self):
        print("Mammal is Eating Chicken")

class employee(human,mammal):
    pass

emp = employee()
emp.eat()