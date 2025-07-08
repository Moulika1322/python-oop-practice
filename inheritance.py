
#single inheritance

class parent:
    def function1 (self):
        print("this is parent class")
class child(parent):
    def function2 (self):
        print("this is child class")
        print("__________________")

object=child()
object.function1()
object.function2()  

#multilevel inheritance
class parent:
    def function1 (self):
        print("this is parent class")
class child(parent):
    def function2 (self):
        print("this is child class")
class grandchild(child):
    def function3(self):
        print("this grandchild class")

object=grandchild()
object.function1()
object.function2()
object.function3() 



#Hierarchical Inheritance:

class parent:
    def function1(self):
        print("this is parent class")
class child1(parent):
    def function2 (self):
        print("this is chaild1 class")
class child2(parent):
    def function3 (self):
        print("this is child2 class")
obj=child1()
obj.function1()
obj.function2()
obj=child2()   # to create the two objects because there has a two child classes and one parent class  their two child classes have a parent propertie
obj.function3()




#multiple inheritance

class father:
    def fun1 (self):
        print("this is father class")
class mother:
    def fun2 (self): 
        print("this is mother class") 
class child(father,mother):
    def fun3(self):
        print("this is child class")
obj=child()
obj.fun1()
obj.fun2()
obj.fun3()




                     
                