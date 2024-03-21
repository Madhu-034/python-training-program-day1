#day:9

'''
#Find the uncommon words from 2 strings

s1 ="hello how are you"
s2 = "hello how is"
s1=s1.split(" ")
s2=s2.split(" ")

for val in s1:
    if val not in s2:
        print(val)
for val in s2:
    if val not in s1:
        print(val)

#write a code print the 8th fibanochi number
#0,1,1,2,3,5,8

n1= 0
n2=1
ans=1+1==>2

n1=1
n2=2
ans=1+2==>3

n1=2
n2=3
ans=2+3==>5

#find the 8th fibanochi number
num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    n1 =n2
    n2 = ans
print(ans)


#constuctors
#eg:2
#

class profile:
     def __init__(self):
         print("hello world")
obj = profile()
obj.__init__()

#eg:3
#parameterised constructor
class profile:
    def __init__(self,id,name,age):
        print(id,name,age)
        
obj=profile(1, "madhu",23)

#eg:4
class c1:
    name="madhu"
    place="cbe"

    def m1(self):
        print(self.name,self.place)
object =c1()
object.m1()

#or
class c1:
    email="madhu@gmail.com"
    
    def m1(self):
        name="madhu"
        place="cbe"
        print(name, place)
        print(self.email)
object =c1()
object.m1()

#eg:5
class c1:
    def m1(elf):
        name="madhu"
        age=23
        return name,age
    def display(self):    
           print(self.m1())
 
object =c1()
object.display()


#eg:6
#To use the variable inside the constructor in another method
class class1:
  # email="madhu@gmail.com"    #--->static variable
    def __init__(self):
        self.name="madhu"       #instance variable
        self.email="madhu@gmail.com"
        #return name,email # error-->cannot use return with constructor
        
    def display(self): #instance method
        print(self.name,self.email)

c1=class1()
c1.display()


#----->Inheritunce
#The process of utilising the method and attributes of parent class
#through the object of child class it is called as inheritance


#5 types inheritance 
#Single inheritance
#multilevel inheritance
#multiple inheritance
#Hybrid inheritance
#Heirarichal inheritance

#single inheritance
# It has only one parent class and only one child class

#eg:1
class parent:
    def m1(self):
        print("Iam parent class")

class child(parent):
    def m2(self):
        print("Iam child class")
            
obj=child()
obj.m1()

#eg:2

class c1:
    def __init__(self):
        print("iam constructor from parent class")
        
class child1(c1):
    pass
obj=child1()


#eg:3

class parent:
    name = 'madhu'
    
class child(parent):
    name='madhu'

    def display(self):
        print(self.name)

d = child()
d.display()



# Multilevel inheritance
#? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")
        
class dog(voice):
    def dog_voice(self):
        print("bark")
        
class cat(dog):
    def cat_voice(self):
         print("Meow")
         
class parrot (cat):
    def parrot_voice(self):
         print("speak")

all=parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


#eg:2

class honda_city: 
     def honda_city_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
         print(cc, Hp, torque, fuel_type, num_of_piston)
         
     def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
         print(color, weight, height, length, vehicle_type)
         
class amaze(honda_city):
     def amaze_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
         print(cc, Hp, torque, fuel_type, num_of_piston)
         
     def amaze_body_specs (self, color, weight, height, length, vehicle_type):
         print(color, weight, height, length, vehicle_type)
class civic(amaze):
     def civic_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):

         print(color, weight, height, length, vehicle_type)
class honda(civic):
     pass

honda = honda()
honda.honda_city_engine_specs (1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")


#multiple inheritance
#It has multiple parent and 1 child

class while_pertol:
    def function_w(self):
        print("used to Airplans")
class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")
class premium_petrol:
    def function_p(self):
        print("spots cars, bikes")
class petrol (while_pertol, Organic_petrol, premium_petrol):
    def defanition(self):
         print("Petrols types")


p= petrol()
p.defanition()
p.function_o()


# Eg:2
# MRO---> Method resolution Order
class addition:
    def add(self, a, b):
        print(a+b)
    def mul(self,a,b):
        print(a%b)
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)


# Heirarical inheritance
class catagory:
    def weight(self, weight):
        print(weight)
    def display(self, color, taste):
        print(color, taste)
class Tomato(catagory):
    def tomato_specs(self):
        color="black"
        taste= "neutral taste"
        self.display(color, taste)
class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste ="sweet"
        self.display(color, taste)
c=carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20gms")

##hibrid inharitance
#? The combination of above 4 inheritance is called Hybrid inheritance
class c1:
   def ml(self):
        print("Class1")
class c2(c1):
   def m2(self):
       print("class2")

class c3(c2):
    def m3(self):
        print("Class 3")

class c4(c3):
    def m4(self):
        print("Class 4")
        
    def m3(self):
        print("iam m3 from c4")   
        
class c5(c4):
    def m5(self):
        print("Class 5")


class c6(c5,c4,c2,c1):
    def m6(self):
        print("Class 6")

obj=c6()
obj.m3()

'''

#...........>polymorphism

#? poly many, morph--> form
# A function which has the ability to perform more than 1 functionality
#then it is considered to be as plioymorphism


#Ploymorphism in builtin functions
#len()-> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()


#* Ploymorphism in operators
#+
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])

print(6*7) 
l1 = [1,2,3,4]
print(*l1)
#def f1(*args):
l1 = [1,2,3,4]
print(l1*10)






































