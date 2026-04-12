# list comprehension :
# n=['tom','bob','wow','cat']
# l=[i[0]for i in n]
# print(l)

# set comprehension :
# ex-1
n=[1,1,2,2,3,4,5,5,6,7,8]
uniqueEven={i for i in n if i%2==0}
print(uniqueEven)

# ex-2
num=[1,1,2,2,3,4,5,5,6,7,8]
squ={x**2 for x in range(1,10)}
print(squ)


# dictionary comprehension :
x=['the','last','coder']
d={i:len(i) for i in x} 
print(d)
