# And
x=10
y=2
print(x<y and x>y)
print(x>y and x>y)
print(x<y and x<y)
#True and True= TRUE
#False and False= FALSE
#True and Flase= FALSE
#False and True = FALSE

#OR
c=200
r=300
print(c<r or c<r)
print(c>r or c>r)
print(c<r or c>r)
print(c>r or c<r)

#not
x=200
y=200
print(not(x<y and x>y))
print(not (x>y or x<y))

#Examples
x="Navya"
y="Kavya"
z=x
print(id(x))
print(id(y))
x=100
y=200
print(x<y and x>y)
print(x<y or x>y)
print(not(x<y and x>y))

