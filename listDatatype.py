"""
#list is a data structhure which holds multiple data types items with the square brakets is called LIST.
a=[1,9.8,True,'string',1,9,8,'type',0,9,'hai']  #1,9,8,type are duplicate data types 
print(a)
#it is mutable in nature
#insertion order perserver
#duplicates item are allowed
#heterogeneous items are allowed

#Slicing
print(a[::-1])
print(type(a))
b=[1,2,3,4,7]
print(type(b))
print(list(range(1,10)))
ab='srting Hello haii'
list=list(ab)
print(list)
print(ab.split())


a[1]=20
a[-1]=30
a[3]='hai'
print(a)
print(a[2:7:2])
print(a[2:12:2])
print(a[4::2])
print(a[3:7])
print(a[8:2:-2])
print(a[4:100])
print(a[:5+2])
b=["apple","banana","cherry"]
b[1:2]=["blackcurrent","watermelon"]
print(b)
a[-1]=["hello",9,4]
print(a)

v=["hello",["python",0.5,4,False,[1,2,3,4]],'-1','true',1+8j]
print(len(v))
print(v[1])
print(v[1][-1][-3])

fr=["apple","banana","cherry"]
fr[1:2]=["navy","kkjk"]
print(fr[2])



# HW 24-2-25

# 1 list create and printing
ab=[10,20,30,40,50]
print(ab)
#2 list length
ac=[5,15,25,35,45]
print(len(ac))

# 3 accessing element
bi=[100,200,300,400,500]
print(bi[2])

#
a=["apple","banana","cherry","date"]
print(a[-1])

# part-2 list slicing & modification
#basic slicing
a=[1,2,3,4,5,6,7,8,9]
print(a[:3])

b=[10,20,30,40,50,60,70]
print(b[2:])

c=[5,10,15,20,25,30]
print(c[::2])

# 5 slicing with index range
j=[4,5,7,8,10,12]
print(j[1:4])

k=["aa","bb","cc","dd","ee"]
print(k[1:2])

g=[11,22,33,44,55,66,77]
print(g[2:5])

# 6 modifying a list
r=[2,4,6,8,10]
r[2]=100
print(r)

# part-3 nested list operators
# 7 nested list accessing
c=[1,2,[3,4,5],6,7]
print(c[2][1])

g=['a',['b','c','d'],'e']
print(g[1][1])

# 8 nested list slicing
b=[[10,20],[30,40,50],[60,70,80]]
print(b[1][:2])

u=[["aa","bb"],["cc","dd","ee"],["ff","gg"]]
print(u[1][:2])

h=[1,[2,[3,4,5],6],7]
print(h[1][1][:2])

#part-4 Changing Elements using slicing
# 9 replacing elements using slicing
n=[1,2,3,4,5,6]
n[2:4]=['A','B']
print(n) 

m=[10,20,30,40,50]
m[:2]=[100,200,300]
print(m)

# 10 inserting element using slicing
e=['apple','banana','cherry','date']
e.insert(2,'grape')
print(e)

w=[1,3,5,7,9]
w.insert(1,2)
w.insert(3,4)
w.insert(5,6)
w.insert(7,8)
print(w)

# 11 deleting element using slicing
d=['a','b','c','d','e','f']
print(d[::3]) 

t=[10,20,30,40,50,60,70]
print(t[:4])

# 12 moving elements using slicing
s=[1,2,3,4,5]
s[:]=s[-2:]+s[:-2]
print(s)


u=['X','Y','Z','a','b']
u[:]=u[3:]+u[:3]
print(u)

# part-5 list operations and membership
# 13 list concatenation
a=[1,2,3]
b=[4,5,6]
print(a+b)

# 14 list duplicate
v=['a','b','c']
print(v*3)

# 15 list indexing
r=['red','blue','green','yellow','purple']
print(b[-4:1])

# 16 check membership
e=[1,3,5,7,9]
print(5 in e)

q=['dog','cat','rabbit']
print('lion' in q)

# 17 list reverse
s=[11,22,33,44,55]
print(s[::-1])
"""
# 25/2/25
a=[1,2,3,4,5]
a[1:2:-2]
print(a)
a[1:1:-1]
print(a)
a[2::-2]
print(a)


# list methods
# append()
a.append([1,2,3,4,5])
print(a)
# sort()
#pop()
#del a[]
#index()
#remove()
#count()
#clear()
#copy()
#reverse()

#list concatination
l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
print(l1+l2)
print(l1*3)

# l=l1
# l[0]="hello"
# print(l)
# print(l1) # to print previous and copy element change

# r=l2.copy()
# r[0]="hai"
# print(r)
# print(l2)
#           # to print only the copy element

#zip()
list1=[1,2,3,4,5]
list2=[6,7,8,9,0]
z=zip(list1,list2)
print(list(z))

#unpacking list
a=[1,2,3,4]
b=[2,4,5,6]
a,b,*c=list1
print(a,b,c)

# a=[300,200,150,550]
# b=a.count()
# print(b)