#DAY:10-->last day
'''
#Ploymorphism in classes
#We can achieve polymorphism in 2 ways
#1.) Method overloading it is not possible in python
#2.) Method overriding


#method over- riding
#* Ploymorphism in classes using inheritance
#eg:1
class bank:
    def ratio(self):
        print("All banks has repo rate")
class SBI(bank):
    def ratio(self):
        print("SHI rate is 9%")
class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")
i = IOB()
i.ratio()


s= SBI()
s.ratio()



 #EG:2

class USA:
    def langauge(self):
        print("English")
        
    def capital(self):
        print("Washington DC")
        
class India (USA):
    def langauge(self):
        print("None")
        
    def capital(self):
        print("New delhi")
I = India()
I.langauge()
I.capital()

#eg:3
#polymarphism using objects

#c1, c2,-->c1=print(c1),print(c2)
#f1, f2

class c1:
    def f1(self):
        print('class 1')
        
    
class c2(c1):
    def f1(self):
        super().f1()
        print('class 2')
        
obj1 = c2()
obj1.f1()

#eg:4

class c1:

    def f1(self):
        print("class 1")
class c2(c1):

    def f1(self):
        print("class 2")
obj1 =c2()
obj2 = c1()


def display(a):
    a.f1()
display(obj1)
display(obj2)


#eg:5       
a= 9 
b= 6
print(a+b)
print(a.__add__(b)) #Dunder method or mafic method


int()
print(a.__add__(b))
#len()

#* Changing the functionality  of builtin functions

class shooping:
    def __init__(self, l1):
        self.items = l1

    def __len__(self):
        length = len(self.items)
        return length
s = shooping([1,2,3,4])
print(len(s))


#-->method overloading
#eg:1
class summing:
    def add(self, a,b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)
        
s = summing()
#s.add(4, 3)#--->error
s.add(4,5,1)

#eg:2
class summing:
    def add(self, a=None, b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:    
            print(a)
obj=summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)



#!-----> Abstraction
#The process of hiding the implimentation details is abstraction


#eg:1
from abc import ABC, abstractmethod
class shapes (ABC):
    @abstractmethod
    def sides(self):
        print('All shapes have sides except circle')
class triangle(shapes):
    def traingle_sides(self):
        print("3 sides")

    def name(self):
        print("Iam traingle")

    def sides (self):
       pass

class square(shapes):
    def square(self):
        print("4 sides")
        
tr= triangle()
tr.traingle_sides()
tr.name()


# Rules to define abstract class1
#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method.
#5.) all the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the #child classes

#eg:2


#super()-> used to access the parent class method from childclass method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
class2 = c2()
class2.m2()


#Eg:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd ="madhu2000$"
        return pswd
class login(password):
    def validate(self, name, password):
        if super().pwd()== password:
            print("Welcome", name, '!!')
            print("Login Successfull")
        else:
            print("Please check the password")
    def pwd(self):
        pass
login = login()
name=input("enter the name:")
pwd = input("enter the password:")
login.validate(name,pwd)

#encapsulation
#*-->eg:1
class car:
    __name ="BMW"# private variable
 #   print(__name)
    
c1= car()
print(c1.name)#error
c1.name="audi"
print(c1.name)#error


#eg:2
#accessing private  data outside the class
class c1:
    __phone='9876543210'
    
    def display(self):
        print(self.__phone)
c = c1()
c.display()

#eg:3
# declare private method
class class1:
    def __m1(self):
        print(" iam private method")
    def __init__(self):
        self.__m1()
c=class1()
#c.__m1()  #error



# nested class 
class class1:
    class class2:
        name = "madhu"

        def display(self):
             print(self.name)

    obj1 = class2()
    
obj = class1()
obj.obj1.display()

#Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "908", "handkey": 30}
d1={"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:

        if d1 [val]== min(d1.values()):
           print(val)
    for va in d1:    
        if d1[val] = max(d1.values()):
            print(val) for val in d1:
if val.startswith('s') or val.startswith('S'): print(val)

'''
d1 ={"shirt" : 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
for val in d1:
    if d1 [val] == min(d1.values()):
       print(val)
for val in d1:
    if d1 [val] ==max(d1.values()):
       print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
       print(val)

'''
d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)
'''







 
