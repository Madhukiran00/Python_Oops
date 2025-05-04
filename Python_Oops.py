#Object-Oriented Programming (OOPS)

#Class         =>Blue Print of the object
#object        => instance of the class
#Inheritance   => Reusability of code
#Polymorphism  => Many forms
#Encapsulation => Hiding the data
#Abstraction   => Hiding the implementation details
#Polymarphisam => Many forms
#Encapsulation => wrapping of variables  and methods into a single unit

#Inheritance
#1)single
#2)Multilevel
#3)Multiple
#4)Hierarchical
#5)Hybrid

#1)Single Inheritance

# class Parent:
#    def add(self):
#        print("This is parent class")
# class Child(Parent):
#     def sub(self):
#         print("This is child class")
# obj=Child()
# obj.add() #This is child class
# obj.sub() #This is child class

#2)Multilevel Inheritance




# class Parent:
#     def add(self):
#         print("This is parent class")
# class Child(Parent):
#     def sub(self):
#         print("This is child class")
# class GrandChild(Child):
#     def mul(self):
#         print("This is grand_child class")

# obj=GrandChild()
# obj.add()
# obj.sub()
# obj.mul()
#3)Multiple Inheritance
# class Parent1:
#     def add(self):
#         print("This is parent1 class")
# class Parent2:
#     def sub(self):
#         print("This is parent2 class")
# class Child:
#     def mul(self):
#         print("This is child class")
# obj=Child()
# obj.add()
# obj.sub() 
# obj.mul()
#4)Hierarchical Inheritance
# class Parent:
#     def add(self):
#         print("This is parent class")
# class Child1(Parent):
#     def sub(self):
#         print("This is child1 class")
# class Child2(Parent):
#     def mul(self):
#         print("This is child2 class")
# obj=Child1()
# obj.add()
# obj.sub()    
# obj1=Child2()
# obj1.add()
# obj1.mul()
#5)Hybrid Inheritance    
# class Parent:
#     def sum(self):
#         print("This is parent class")
# class Child1(Parent):
#     def sub(self):
#         print("This is child1 class")
# class Child2(Parent):
#     def mul(self):
#         print("This is child2 class")
# class GrandChild(Child1):
#     def div(self):
#         print("This is grand child class")
# obj=GrandChild()
# obj.sum()
# obj.sub()
# obj.div()
#Polymorphism
#1)Method Overloading
#2)Method Overriding

#1)Method Overloading
#Method Overloading => Same method name with different arguments

# class Parent():
#     def add(self,a,b):
#         return a+b
    
    
    
# obj=Parent()
# print(obj.add(10,20))
# print(obj.add("Madhu","Kiran"))
# print(obj.add(10.5,20.5))
#2)Method Overriding
#Method Overriding => Same method name with same arguments
# class Parent():
#     def add(self,a,b):
#         return a-b
# class Child(Parent):
#     def add(self,a,b,c):
#         return a+b+c
# obj=Child()
# print(obj.add(10,20,30))
# print(obj.add("Madhu","Kiran","Kumar"))
# print(obj.add(2,4,6))










