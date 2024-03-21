#day:8
'''
#eg:3
def profile(name,age,place):
    txt="my name is {}.iam {} year old.iam from{}."
    print(txt.format(name, age, place))
profile("madhu",23,"bdvl") 

#eg:4
#function with return statement
# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

def f1():
    z = 8
f1()
print(z) #error --->cannot use outside the fonction


#def f1(a,b):
#    c=a*b

#def gracemark():
#    print(output+4)
#gracemark()

def f1(a,b):
    c=a*b
    return c
#print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)

def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

#123
def palindrome(n):
    string = str(n)
    rev=str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
        print("not palindrome")
a=int(input("enter the value:"))
palindrome(a)



#based on the decleration of parameter and args
#functions are divided into 5 categories


#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args

# * Positional args

#eg:1
def profile(name, phone, mark):
    txt="my name is{}.my phone number is{}. i got {} marks."
    print(txt.format(name, phone, mark))
profile(9876543210,"madhu",88)    
#*keyword args
#eg:1`
# To overcome the disadvantage of position args, we use args
# it is process of initiating the parameter with args while calling the
# funtions
def profile(name, phone, mark):
    txt="my name is {}.my phone number is {}. i got {} marks."
    print(txt.format(name, phone, mark))

profile(name="madhu",mark=88,phone=9876543210)

# todo---> exception of keyword args function
def profile(name, phone, mark):
    txt="my name is {}.my phone number is {}. i got {} marks."
    print(txt.format(name, phone, mark))

#profile(name="madhu",9876543210, mark=88) #error-->positional args follow keyword args
#profile(9876543210,name="madhu", mark=88)#error--->namew has multiple values
profile("madhu",mark=88,phone=9876543210)

#*default args
#The method of assigning the argument to the parameter while declaring the
#function 
#eg:1
def profile(name, phone,place="KADAPA"):
    if place =="kadapa" or place=="kadapa" or place =="KADAPA":
        txt = "my name is{}.my phone number is{}.i am from{}."
      
        print(txt.format(name, phone,place))      
    else:
        print("you are not eligible to signup") 
profile("madhu",8976543210)

      

def profile(name,place="KADAPA", phone):#  error --> because default args should not follow 
                                            #positional param
    if place =="kadapa"or place=="kadapa" or place =="KADAPA":
       txt="my name is{}.my phone number is{}.i am from{}."
       print(txt.format(name, phone,place))
      
    else:
         print("you are not eligible to signup")
profile("madhu",8976543210)


#*variable length params

#eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param
#eg:1
name="madhu",'name2','name3'

def profile(*name):
    for val in name:
        print("my name is", val)
profile("madhu",'name2','name3')

#eg:2
def profile(*name, age):
    for val in name:
        print("my name is", val, "my age is",age) 
profile("madhu",'name2','name3',23)#-->age has no args

def profile( age,*name):
    for val in name:
        print("my name is", val, "my age is",age) 
profile(23,"madhu",'name2','name3')


#* keyword variable length args
#kwargs--->which is used to provide the args in the form of key value pair.
#eg:1
def price(**price_list):
    print(price_list)
   
price(shirt=1000,mobile=3000)

d1={"a":100,"b":200,"c":300}
d1=dict(a=100,b=200,c=300)
print(d1)


#n=5
#{1:1,2:4,3:9,4:16,5:25}

n=int(input("enter the number:"))

d1={}
for val in range(1,n+1):
    d1[val]=val**2
    print(d1)


def dict1(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)
dict1(5)

# ! ---> object oriented programming
# The panadigms of objects oriented progarmming are


# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

#class is a blue print of an object
#l1 = [1,2,3,4,5,6]

#eg:1
class c1:
    name1="madhu"
    print(name1)

#eg:2    
class person:
    name ="madhu"
    
c = person()
print(c.name)

#eg:3
#create of a method
#when the function is created with a class is called as method

class person:
   def display(person):# It is a method
       print("hello welecome to classes")
p=person()
p.display()

#eg:4
#method with parameter
class person:
    def display(person, name, age):
        print(name,age)

p=person()
p.display("madhu",28)

#eg:5

class person:
    fname =",madhu"# attribute or static variable
    lname="T"

    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p=person()
p.first_name()
p.full_name()

#eg:6
# constructors --->__int__()
# This is a special method which has the ability to execute itself without
# Calling it manually through the process of instantiation
class profile:
    def__d1__(self): #constructor method
    print("hey")
p= profile()# Execute of constructor through this process 
p.d1()

  Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal
'''































