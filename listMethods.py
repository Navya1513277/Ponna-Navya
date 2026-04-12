# append();
a=[1,2,3,4,5,6]
a.append(7)
print(a)

# insert ();
a=[1,2,3,4,5]
a.insert(-2,6)
print(a)

a=[1,2,3,4,5]
a.insert(0,"H")
print(a)

# extend();
a=[1,2,3,4,5]
a.extend([1,2,3])
print(a)

a=[1,2,3,4,5]
a.sort()
print(a)

a=[5,4,3,2,1]
a.sort()
print(a)

a=[300,850,200]
a.sort(reverse=True)
print(a)

#pop();
a=[300,850,200]
print(a.pop())

a=[300,850,200]
print(a.pop(0))

a=[300,850,200]
del a[1]
print(a)

a=[300,850,200]
a.remove(200)
print(a)

q=[300,850,200] 
k=q.index(200)
print(k)

w=[300,850,200]
b=a.clear()
print(b)

a=[300,850,900]
d=a.copy()
print(d)

a=[430,900,500]
a.reverse()
print(a)

a=[430,900,500]
a.sort(reverse=True)
print(a)

# a=("orange","mango","kiwi","pinapple","banan")
# b=a.sort()
# print(b)