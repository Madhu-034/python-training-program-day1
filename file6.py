#day:6
'''
#1.)python program to capitalize the first and last character of each
#word in a sting
#2.)input :128
#output:yes
#128%1==0.128%2==0.and128%8==0.
#3.)l1=[1,2,3,4],l2=[5,6,7,8]
#add both l1 and l2.ans=[6,8,10,12]

#s1="mechanical"
#fst=s1[0].upper()
#lst=s1[1].upper()
#print(fst+s1[1:len(s1)-1]+lst)

n=128
while n!=0:
    rem=n%10
    print(rem)
    n=n//10
    
n=128
if  n % 1 == 0 and n % 2 == 0 and n % 8 == 0:
    print("yes")
else:
    print("no")
#n= 128
##for i in str(n):
 #   print(i)

n=128
tem=n
f1=0
while n!=0:
     rem =n%10
     check=tem%rem
     if check!=0:
         f1=1
     n =n//10    

if f1==0:
    print("yes")
else:
    print("no")

l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[]
#print(l1[0]+l2[0],l1[1]+l2[1])
for val in range(len(l1)):
    ans=l1[val]+l2[val]
    l3.append(ans)
print(l3)


#---->set

#characteristics of set
1.)set can be created using{}
2.)The elements inside set are not indexed
3.)Does not allow duplicate values
4.)It unordered
4.)Heterogenous  --->acceot only unmutable datatypes
5.)mutable or changable

#eg:1
s1={9,9,89,7.76,8+7j,(8,7,5,),"truck",'e'}
print(s1)

#eg:2
s2={3,4,45,6,[9,0]}
print(s2)---->error

#eg:3
#min(),max(),len()

#eg:4
#to add element inside set
#add()
s1={2,44,56,'fg'}
s1.add(43)
print(s1)

#update()
s1.update([9,0])
print(s1)
#to delete element inside set
s1={8,68,89,'u'}

#pop()#to delete one element randomly
s1.pop()
print(s1)

#remove()
#s1.remove(68)
#print(s1)

#discaed()
#s1.discard(8967)
#print(s1)

#clear()
#l1={}
#print(type(l1))--->datatype is dict

#s1=set()#to creat empty set
#print(type(s1))

s1={8,9,0}
#s1.clear()
#print(s1)#--->set()

del s1
print(s1)


#*join the sets
s1={9,8,7}
s2={9.90,"card",'t',65}
#union()-->to combine 2 sets
s3=s1.union(s2)
print(s3)

#*intersection()-->to get common elements inside set
s1={4,5,6}
s2={5,6,7,8}
print(s1.intersection(s2))

#*differance()
s1={4,5,6}
s2={5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))

#isdisjoint(),issubset(),issuperset()
s1={8,9,0}
s2={6,7,8,9,0}

print(s1.issubset(s2))
print(s2.issuperset(s1))
'''
#problem:1
s1={1,2,3,4,5}
s2={3,2,7,8,9}

#for val in s1:
#    if val in s2:
#        print("Its joint set")


for val in s1:
    if val in s2:
        str1="Its joint set"
print(str1)
'''


#---->dictionary

#eg:1
d1={1:100,'a':200,4.5:"hello"}

print(d1)
print(len(d1))


#char of dictionary
#1.)have to be surrounded by{}
#2.)It have to be in the form of  key, valuepair
#3.)It is mutable
#4.)Duplicate keys are not allowed, duplicate values are allowed
#5.)IT is unindexed
#6.)It is ordered
#7.)key does no allow  mutable datatypes, values allow  mutable datatyp

d1={1:100,2:200,3:300,4:400}
#to access elements in dictionary
print(d1)
#or
#to acces the values, have to use key
print(d1[1])#o/p-->100


#some common functions
#len(),min(),max()
print(max(d1))
printr(min(d1))

#To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

#dictionary  based functions
#To add element(key and value pair)in dict 
d1={1:100,2:200,3:300,4:400}     
d1[5]=500
print(d1)

#to replace a value in dictionary

d1={1:100,2:200,3:300,4:400}
d1[2]="moyo moyo"
print(d1)

#Delete elment from dictionary
d1={1:100,2:200,3:300,4:400}
#popitem()#--->to delete last key value pair in dict
d1.popitem()
print(d1)

#*join 2 dictionary
#update()
d1={1:100,2:200,3:300,4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)      

#get()
#d1={1:100,2:200,3:300,4:400}
#print(d1[3])

#d1={1:100,2:200,3:300,4:400}
#print(d1[90])
#print(d1.get(90))

#To print all the keys
#print(d1.keys())
#print(type(d1.keys()))

#to print all the values
#print(d1.values())

#*Iterating dictionary
d1={1:100,2:200,3:300,4:400}
for val in d1:# To iterate keys alon
    print(val)

for val in d1.values():#TO iterate values alone
    print(val)

#To get both key values
for key, val in d1.items():
    print(key,val)

#n=input()   

#1.)swap elements in string list
#The original list is:['Gft','is','best','for','eGGKs']
#list after performing character swap:['egf','is','bGst','for','eGGK']

#problem:1

n=int(input("enter num of times:"))
integer=[]
float_value=[]
string=[]
for val in range(n):
    value=eval(input("enter the values"))
    if type(value)==int:
        integer.append(value)
    elif type(value)==float:
        float_value.append(value)
    elif type(value)==string:
        sring.append(value)
    else:
        print("pls provide value in int, float,string")
print(integer)
print(float_value)
print(sting)

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3=set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)


# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

l1=[1,2,3,4]
l2=["a","b","c","d"]

d1={}
#d1[l1[0]]=l2[0]
#print(d1)

for val in range(len(l1)):
    d1[l1[val]]=l2[val]
print(d1)

'''












