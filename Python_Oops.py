#Object orientend programming language(Oops)

#Class         =>Blue Print of the object
#object        => instance of the class
#Inheritance   => Reusability of code
#Polymorphism  => Many forms
#Encapsulation => Hiding the data
#Abstraction   => Hiding the implementation details
#Polymarphisam => Compile time polymorphism
#Encapsulation => Public

#Inheritance
#1)single
#2)Multilevel
#3)Multiple
#4)Hierarchical
#5)Hybrid

#1)Single Inheritance

class Parent:
   def add(self):
       print("This is parent class")
class Child(Parent):
    def sub(self):
        print("This is child class")
obj=Child()
obj.add() #This is child class
obj.sub() #This is child class

#2)Multilevel Inheritance

class Parent:
    def add(self):
        print("This is parent class")
class Child(Parent):
    def sub(self):
        print("This is child class")
class GrandChild(Child):
    def mul(self):
        print("This is grand_child class")

obj=GrandChild()
obj.add()
obj.sub()
obj.mul()


#3)Multiple Inheritance
class Parent1:
    def add(self):
        print("This is parent1 class")
class Parent2:
    def sub(self):
        print("This is parent2 class")
class Child:
    def mul(self):
        print("This is child class")

obj=Child()
obj.add()
obj.sub() 
obj.mul()
        






