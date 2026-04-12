"""
#reverse print
x="My world"
print(x[::-1])

X="JAGADEESH"
print(X[::-1])
"""

# #remove comas:
# a="hello, world!"
# b=a.replace(",","")
# print(b)


# x="to remove ,the string, values,"
# y=x.replace(",","")
# print()

"""
# to print even letters
a="This is python language"
print(a[0::2])

#to print odd letters
b="This language is simple and easy to learn"
print(b[1::2])


#string convert into list EX-1
a="hello world python"
print(a.split())
b="".join(a)
print(b)

#EX-2
text="This is an example string convert into list formate"
x=text.split(" ")
print(x)
print(type(x))
y=" ".join(x)
print(y)


#to print middle element EX-1 :
b=[1,2,3,4,5,6,7,8,9,10]
length =len(b)//2
c=b.index(length)
print(c)

# EX_2
c=[1,2,3,4,5,6,7,8,9]
le=len(c)//2
a=c.index(le)
print(a)
x=200
y=240
print(x in y)


# # QU--1 to find area of rectangle :
# n=int(input("Enter height valu: "))
# a=int(input("Enter width value: "))
# ar=n*a
# print(ar)
"""

#QU--5 convert string into int formate
age="20"
num=int(age)
print(age)
print(type(age))
print(num)
print(type(num))
"""
#QU--4 concatenate two string :
val="my favorate place is "
la="MY HOME"
con=val+" "+la
print(con)
6
#QU-3 simple interest
price=int(input("Enter a value: "))
rate=int(input("Enter rate: "))
time=int(input("Enter time: "))
s_i=(price*rate*time)/100
amo=price+s_i
print("Simple Interest: ",s_i)
print("amount",amo)

#QU-2 compound interest
p=int(input("Enter price"))
a=int(input("Enter amount"))
r=int(input("Enter rate"))
t=int(input("Enter time"))
co_i=p*(1+r/100)**t
amount=a-p
print("Amount",amount)
print("Compound interest: ",co_i)


# AREA of circle
pi=8
r=3
tl=pi*r**2
print(tl)


# USER input
p=int(input("Enter pie valu: "))
r=int(input("Enter r value: "))
total=p*r**2
print(total)

#Armstrong number
val=153
print(1**3+5**3+3**3)

#not amstrong
v=225
print(2**3+2**3+5**3)

c=9474
d=(9**4+4**4+7**4+4**4)
print(c==d)

#user input
n=int(input("Enter n value: "))
sum=0
te=a
while(te>0):
d=te%10
sum+=d**n
print(n+"is an amstrong")
print(n+"is not amstrong")
"""
#to print(min)
# a=8
# b=9
# w=min(a,b)
# print(w)

# #max
# a=12,3,5,7,90
# b=max(a)
# print(b)
# print(type(a))

# #int
# m=68
# n=99
# c=78
# d=67
# N=max(m,n,c,d)
# print(N)

        
#calculating avg heights without using len() and sum() functions:
# Heights=input('Enter all the heights seperated by  a space: ') #int() function not able to use becoz values seperated by space.
# height_list=Heights.split()
# count=0
# print(height_list)
# for i in height_list:
#     count+=1
# print(count) #Without using len function
# for i in range(count): #or range(0,count) #index_0 1 2 3 4
#     height_list[i]=int(height_list[i])
# print(height_list)
# total=0
# for person in height_list:
#     total=total+person
# avg=total/count
# print(round(avg))


# data = "hai hello"  
# a=data.split(" ")

# reverse_string= " ".join(word[::-1] for word in a)
# print(reverse_string)
      