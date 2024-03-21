#day:7
'''
d1={'ten':10,'twenty':20,'thirty':30}
d2={'thirty':30,'fourty':40,'fifty':50}
d1.update(d2)
print(d1)


set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language','Python' }
set3 = {'Data Analytics', 'Robotics', 'Deep learning'}
c=0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break
    if c==3:
        for val in set3:
            if val in set1 or val in set2:
               flag=1
               break    
if flag==0:
    print("disjoint")
else:
    print("joint")
    

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

l3=[]
for val in range(len(list1)):
    ans = list1[val]+list2[val]
    l3.append(ans)
print(l3)   
#or
l3=[]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=+1
print(l3)    

# functions
# DEF
#function is a block of code which is used to perform a specific functionality
#functions can be created using def keyword

#generally functions are 3 parts
#function decleration
#function fefanition
#function call

#eg:1
def greet(): # function defanation 
    print("welcome user!!")
greet()
greet()
greet()
greet()
greet()
greet()    #--->funtion calling  


#eg:2
def greeting(name):
    print("Welcome", name)

for val in range(3):
    username=input("enter the name:")
    greeting(username) #--->user name is argument

'''
def profile(name,age,place):
     print(name,age,place)
str1=int(input("enter the name, age,place"))

        print(str1)















