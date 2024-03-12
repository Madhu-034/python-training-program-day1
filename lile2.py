'''
day2
---->swapping of variables

eg:1
a=7
b=5
temp=a 
a=b    
b=temp
print(a, b)

#eg:2
a=a+b   
b=a-b
a=a-b
print(a, b)

#eg:2
    
a=a*b
b=a/b
a=a/b
print(a, b)


id()-->used to find the memoryaddress of the variable

a=7
b=8
print(id(a))
print(id(b))

#---->keywords
#keywords are reserved word which provides special meaning to
#compiler or interpretor

#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist)
#print(type(keyword.kwlist)
#to check if the string is keyword or not
#print(keyword.is keyword("sid")  false


#if=8
#print(if) # error coz if is a keyword

#--->literals
#literals is the constant value assigned to a variable
#a variable is considers to be constant when it is defines
#in caps
#a=78 # ais variable
#A=78 #A is a constant

#hash()_-->it creates a hash value for constant datatypes and
#provides error for non constant datatypes

n1 =89+7j
print(hash(n1))

f1 =[7, 8, 9]

#print(hash(f1))  #error -->list is non-constant

a=9
b=90
print(id(a))
print(id(b))
#--->operations
#operators are symbols which is used to perform various operations 
#between 2 or more operands

#arithmatic
#assignment
#logical
#relational or comparison
#bitwise
#identity
#membership

#todo--->arithmatic --->+,-,*,/,%,//,**


a=8
b=6
c=9
print(a+b+c)

#input()-->used to get the runtime input
#evcal()-->used to get the runtime values of all datatype
#n1=eval(input("enter the value:"))
#print(type(n1))

a=4
b=2
print(a/b) #is used to get the quotient value
print(a%b) #is used to get the remaider value

#//-->floor devision

a=76543
b=19
print(a//b) #->the output will be inn integer & the output
# comparison --> ==, >,<, !=,<=, >=

a=9
b=7
print(a>b)# true

a = 9
b = 5
print(a==b)

# bitwise operator -->&,|,^,~,<<,>>
a = 7
b = 4
print(a&b )

a = 7
b = 6
print(a|b)
#AND
#A  B  A&B

#2^4 2^3 2^2 2^1 2^0
#8   4    2    1

#0   1    1    1   #-->7
#0   1    1    0   #-->6
#------------------
#~--->
A=9876
print
#logical --> used to compare the expression
#and , or, not
a= 6
print(a>3 and a<10)
print(a>7 or a<30)
print(not(a>8 and a<10))


#identity operator
#it is used to compare the memory location that
#are stored
#is, is not
a = 8
b = 8
print(a is b)
print(a==b)

a=(1, 2, 3)
b=(1, 2, 3)
print(a is b)

#membership operator
#in, not in
#11= [7, 8, 9, 0, 6, 5]
num = 55
print(num in 11)
print(num not in 11)

num = 678
print(8 in num) #error
#conditional statement
#if, elif, else
#eg:1
#--> C syntax
#if (condion){
#   statement;
#   statement;
#   statement;
#}
#python syntax
#if condition
#   statement
#   statement
#   statement
#statement

#eg:1
#a=6
#if a:
 #   print("hllo")
#eg:2
#a=6
#if a>3:
  #  print("hey")
#else:
   # print("no")

#eg:3
#if 7>8:
 #   print("hollo")
    
#print("no")

#eg:4
#a=0
#a= non
#a=false
#a=""
#if a:
 #   print("yes")
#else:
#    print("no")
'''
#a number is even or odd
'''
n = int(input("enter the number"))
if n %2==0:
    print(n, "is even")
else:
    print(n, "is odd")
'''
#sum:2
#name, age, nationality
# 18 above, indian

name = input("enter the name:")
age = int(input("enter the age: "))
nationality = input("enter the nation:")
if age>=18 and nationality=="indian":
    print("eligible for vote")
else:
    print("not eligible")


