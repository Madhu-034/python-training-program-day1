day:3
'''
#eg:3
#take values of length and breadth of a
#from user and check if it is square or not.

#length = int(input())
#breadth = int(input())
#if length==breadth:
#    print("its a square")
#else:
#    print("its not square")

#eg:4
#python program to check whether the
#given integer is a multiple of both 5 and 7

#n= int(input("enter the number "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")
#eg:5    
#write a program to accept the cost price of a bike and display the
#road tax to be paid
# according to the following criteria
#       cost price (in rs)
#       >100000
#       >50000 and <= 100000
#       <= 50000

price = int(input("enter the price: "))
amount = 0
if price >=100000:
    discount= price*(6/100)
    value = price-discount
    tax=value*(15/100)
    total=value+tax     
else:
    tax = price*(5/100)
    total = price+tax
print("the onroad cost of bike is:",total)

#if elif
#eg:1
a=7
b=3
c=9
if a>b and a>c:
    print(" a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")

#A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
mark =int(input("enter mark: "))
if mark>=80 and mark<=100:
    print("a")
elif mark>=60 and mark<80:
    print("b")
elif mark>=50 and mark<60:
    print("c")
elif mark >=40 and mark<50:
    print("d")
else:
    print("fail")

#eg:6
#accept the age of 4 people and display the oldest one.

#---> short hand if else
#eg:1
a=9
b=60
if a>b:
    print("a")
else:
    print("b")
    
--> using short hand if else
#rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

#print("a") if a>b else print("b")

#code to check the given char is vowel or consonent

char = input("enter the char: ")
if char=="a" or char =='e' or char =='i' or char =='u':
    print("is a vowel")
else:
    print("its consonent")

    
# or

str1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonent")

# sorthand if else

char = input("enter the char: ")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")

#---> elif ladder using short hand if else
#eg:1
#find greatest among 3 variable using short if else

a=8
b=5
c=9
print("a is greater")if a>b and a>c else print("b is greater")if b>a and b>c else print("c is greater")

# ----------> looping

#looping can be implimented using
#for loop
#while loop

#----> for loop

# --->for loop
#for loop is used for iteartion, if we know the number of times the loop have to run
#it is used to iterate the iterables eg(sting, tuple, list, etc....)

#todo --> syntax for loop
for(i=0;i<10;i++){
    printf("hello");
}

#for syntax in python
#for userdefined_variable in range(start, end, step):default step is 1
#    statement
#    statement
#    statement

#eg:1
#to print the value from 1 to 10 using for loop

for i in range(0, 10): #(n, n-1)
    print(i)
    print("hello")

#eg:2
for val in range(1, 15, 2):
    print(val)

for val in range(1, 15, 3):
    print(val)

#eg:3
#to decrement the value

for val in range(10, 0, -1):
    print (val)


for val in range(10, 0, -2):
    print (val)

for val in range(10, 0, 1):
    print (val) #no output

#eg:4
#print the output of 7th multiplication table from 21 to 43


#for val in range(1, 10+1):
    
  #  print('7','x',val,'=',val*7)#--->method:1
 #method:2   
    # ans="7x{}={}"
    # print(ans.format(val, val*7))
#--->method:3
   # print(f"7 x {val}={val*7}")
#eg:5

#break --->used to teerminate the loop
#for val in range(1, 10):
#    if val ==6:
#        break
 #   print(val)
 #eg:6
#for val in range(1, 10):
#    print(val)
#    if val ==6:
#    break

#eg:7
#for val in range(1, 10):
#    if val ==6:
#        print(val)
#        break

#-->continue
#eg:1
for val in range(1, 10):
    if val ==6:
        continue
    print(val)


# practise problems
# print the even number between 20 to 40
for val in range(20, 40):
    if val %2==0:
       print(val)

#--->while  loop
#while loop is used when we do not know the number of times the loop have to
#to iterate the non iterable elments while loop is used

#todo syntax
#initialisation
#while condition:
#    statement
#    incre or decre

#3,1}#to iterate number from 1 to 10

#i = 0
#while i<11:
#   print(i)
#   i=i+1 # or i+=1

#eg:2
#to decrement using while loop
i=10
while i>0:
    print(i)
    i-=1
    

#for loop practise

# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432

#1.)----->1-4+9-26+25
'''
a={3,4,{7,5}}
print(a[2][0])
