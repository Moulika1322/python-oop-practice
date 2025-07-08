

"""
class Mobile:
    def __init__ (self,brand,battery,ram,price):
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.price=price
    def display(self):
        print("brand:", self.brand)
        print("battery:",self.battery)
        print("ram:", self.ram)
        print("price:", self.price)
        print("-------------------")
for i in range(5):     # this line to use more number of time to ittrate or print
    object = Mobile("apple",'400mbh','8gb','15000') 
    object.display()       
        
        
 """""
class animals:
    def speaks(self):
        print("animals sounds")
class dog(animals):
    def speaks(self):        
        print("dog is barking")
class cat(animals):
    def speaks(self):
        print("cat is meowing")
object = dog()
object.speaks()
object = cat() 
object.speaks() 



class Animals:
    def __init__(self,name):
        self.name = name
    def speaks(self):
        print(f"{self.name} animals sounds")     #The f in front of the string is used for f-string formatting
class Dog(Animals):
    def speaks(self):        
        print(f"{self.name} is barking")
class Cat(Animals):
    def speaks(self):
        print(f"{self.name} is meowing")
dog = Dog("julli")        
cat = Cat("chuchu")

dog.speaks()
cat.speaks()
