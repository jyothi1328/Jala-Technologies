#Create a class with PRIVATE fields
class A:
             def __init__(self):
                          self.__privatea=20
                          self.publica=20
             def m1(self):
                   print("HELLO ",self.__privatea)

                   def subm1(self):

                                     print("HELLO ",self.__privatea)
class Person():
             def __init__(self,p_name,p_age):
                          self.name=p_name
                          self.age=p_age
             def display1(self):
                          print("super",self.name,self.age)
class Employee(Person):
             def display2(self):
                          print("sub");
e=Employee("Jyothi",23)
e.display1()
e.display2()
p=Person("Spandu",22)
p.display1()
'''
p=Person()
p.display1()
p.display2()
'''          
'''                                     
obj = A()
obj.m1()
#print(obj.__privatea)
print(obj.publica)
'''
