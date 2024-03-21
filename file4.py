#day:4
'''
#--->while loop
#--->break using while loop

#eg:1
#1.)iterate from 20 to 30 and break the loop in 27

i=20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1 
#2.)
i=20
while i<31:
     print(i)
     i+=1
     if i ==27:
        break

#3.)
#i=20
#while i<31:
#     print(i)
#     if i ==27:
#        break
#     i+=1

i = 27
while i ==27:
    print(i)
    if i ==27:
        break
    i+=1

#----> continue
#eg:1
i=20
while i<31:
    if i ==27:
        continue
    print(i)
    i=i+1 

i=20
while i<31:
     i=i+1
     if i ==27:
        continue
     print(i)

#eg:5
#while to iterate from 12 to 22
#find the sum of all numbers

i=12
while i<23:
       print(i)
       i+=1

i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)

#eg:6
#find the average of value from 20 to 25

# i=20
# sum=0
# count = 0
# while i<=26:
#    sum = sum+1
#    count+=1
#    i+=1
# print(sum/count)
    
# ! --------> Nested for loop
# Eg:1

for i in range(1, 3):
    for j in range(1, 4+2):
        print(i, j)

# Eg:2
for row in range(3):
    for col in range(7):
        print("*", end=" ")
    print()
        
print(1, end=" ")
print(2)


sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum, end=" ")
    print()
#--->to print stars in rigt angleed triangle
#eg:1
for row in range(0, 6):
    for col in range(0, row+1):
        print("*",end=" ")
    print()    

for row in range(0, 6):
    for col in range(row, 6):
        print("*",end=" ")
    print()    
#or
for row in range(0, 6, -1):
    for col in range(0, row):
        print("*",end=" ")
    print()    
#eg:2
for row in range(5):
    for col in range(5):
        if col==0 or col==4 or row==0 or row ==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#eg:3
for row in range(0, 5):
    for col in range(0, 6):
        if ((row==0 and col==3)or(row==1 and (col>=2 and col<=4))or (row==2 and (col>=1 and col<=5))):
           print("*", end=" ")
        else:
            print(" ", end=" ")
    print()     

#----->list



#--->data types

primary
#number--->int, float complex
#string
#boolean
#none

collection
#list
#tuple
#set
#dictionary

#---->list
#1.)if the  collection of elments are elements are sorounded by square brackets , is cosidered
#to be list
#eg:1
    #11 = [4, 7, 9, 9.89, "hello",7+9j,[8, 9, 0]]

#*charactristics of list
#1.)list have to be sorrounded by []
#2.)it is mutable (the elments in the list are changable)
every element inside list is indexed
the elements insid list will be ordered format
it can hold duplicate values
its heterogenous

#to access the element in list

lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1)

#--->indexing
#in the collection datatypes like list,tuple,string,the elements will be alloted
#with pre-defined unique value called index value

#we have 2 types of indexing
#possitive indexing -->starts with 0 from left hand side
#neggative indexing-->starts -1 from right hand side

#--->possitive indexing
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[0])
print(lst1[4])
print(lst1[20])--->error

#--->negative indexing
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-1])
print(lst1[-5])

# ---->slicing
#eg:1
c
#list[start_index:end_index:step]
print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

print(lst1[0:7:1]) #lst1[0:7]--->both are same
print(lst1[0:7:2])
'''
lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
#print(lst1[-4:-1])
#print(lst1[-1:-4])--->[]
#print(lst1[-7:-1])
#print(lst1[-7:-1:2])

# to insert or add element list


#append()--used to add element atlast position of list
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)
