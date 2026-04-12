# for loop
# for i in range(6):
#     print(i)

# for i in range(2,6): 
#     print(i)   
# for x in range(2,11,2):
#     print(x)    

# for x in range(10):
#     print(x)


# numbers=(34,54,67,21,78,97,45,44,80,19)
# total=0
# for num in numbers:
#     total+=num
#     print("Total= ",total)    

# for i in ['T','p']:
#     print(i)
#     break
# else:
#     print("Loop else statement successfully executed")
# print("hai")


# for i in range(11):
    # print("Hello")

# for i in "Hello world":
    # print(i)
# l=[1,2,3,4,"hello",True,9,0]
# for i in l:
#     if i==9:
#         continue# break
#     print(i)

# for i in range(11):
    # pass

# for i in range(11,1,-1):
    # print(i)

# nested for loop:
# for i in range(5):
    # print("Helllo")
    # for j in range(6):
        # print("World")
"""
#EX:1
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'aeiou':
      print (char,end="")
Syntax:-
The range() function has the following syntax −

range(start, stop, step)
Where,

Start − Starting value of the range. Optional. Default is 0

Stop − The range goes upto stop-1

Step − Integers in the range increment by the step value. Option, default is 1.
"""
#EX:
# for num in range(5):
#    print (num, end=' ')
# for num in range(10, 20):
#    print (num, end=' ')
# print()
# for num in range(1, 10, 2):
#    print (num, end=' ')

#EX:
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for x in numbers:
#    print (x)


# #EX:
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for x in numbers:
#    print (x,":",numbers[x]) # number.get(x)

#EX:
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for x in numbers.items():
#    print (x)

# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for x,y in numbers.items():
#    print(x,':',y)


#EX:For Else Loop
# for count in range(6):
#    print ("Iteration no. {}".format(count))
# else:
#    print ("for loop over. Now in else block")
# print ("End of for loop")


# number = int(input("Enter the table: "))
# for i in range(1,number+1):
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)
#     if i ==2:
#         break

# number = int(input("Enter the table: "))
# for i in range(1,11):
#     print(number,'*',i,'=',number*i)

# calculator
# num=int(input("Enter the num value: "))
# sign=input("Enter the input sign: ")
# num1=int(input("Enter the num1 value: "))
# if sign == "+":
#     print("Addition with num+num1=",num+num1)
# elif sign=="-":
#     print("subtraction with num-num1=",num-num1)
# elif sign=="*":
#     print("Multiplication with num*num1=",num * num1) 
# elif sign=="/":    
#     print("D02ivision with num/num1= ",num/num1) 


# Assingment :
# QU-(1) Write a program to print numbers from 1 to 10 :
# for x in range(1,11):
    # print(x)
    
# # QU-(2) write a program that takes an integer n as input and calculates the sum of the first natural numbers :
# n=int(input("Enter the n numbers : "))
# sum=0
# for x in range(1,n+1):
#     sum=sum+x
    
# print("Sum of the natural numbers are: ",sum)


# QU-(3) write a program to print the following right- angle triangle pattern using a nested loop :

# ex 1 :
# normal
# for i in range(1,6):
    # print('* '*i)

#ex -2 :
# Nested loop :
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()         

# Ex-3
#Reverse triangle :
# for i in range(1,6):
#    for j in range(6-i):
#        print('*',end=" ")
#    print()

# Ex-4 :
# for i in range(7):
#     for j in range(7-i):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=' ')
    # print()        
# Qu-(4) write a program to print a pyramid :
# for i in range(7):
#     for j in range(7-i):
#         print(end=" ")
#     for k in range(i):
#         print("*",end=' ')
#     print()        

# QU-(5): Write a program to print a square pattern of * symbols, where the size of the square is determined by user input:
# n=int(input("Enter value :"))
# for i in range(n):
#       if(i==0)or(i==n-1):
#         print("* "*(n))
#       else:
#         print("*"+" "*(2*n-3)+"*")       


# WHILE LOOP :

# while True:
#     print('Hello')
# while True:
#     print('Hello')
#     break

# while False:
#     print('Hello')
#     break
# #EX:-1

# count=0 #5
# while count<5:
#    count+=1
#    print ("Iteration no. {}".format(count))

# print ("End of while loop")

#Ex:-2

# var = 1
# while var == 1 : # This constructs an infinite loop
#    num = int(input("Enter a number :"))
#    print ("You entered: ", num)
# print ("Good bye!")

#EX:-3

# while-else:-Till the count is less than 5, the iteration count is printed. 
# As it becomes 5, the print statement in else block is executed"""

# count=0
# while count<5:
#    count+=1
#    print ("Iteration no. {}".format(count))
# else:
#    print ("While loop over. Now in else block")
# print ("End of while loop")

# count=0
# while count<5:
#    count+=1
#    print ("Iteration no. {}".format(count))
#    if count==3:
#     break
# else:
#    print ("While loop over. Now in else block")
# print ("End of while loop")

# Python break statement is used to terminate the current loop


#EX:-4

# var = 10                   
# while var > 0:              
#    print ('Current variable value :', var)
#    var = var -1
#    if var == 5:
#       break

# print ("Good bye!")


# Python continue statement is used to skip current loop to start the next iteration.


#EX:-5
# text = "hello world"
# i = 0

# while i < len(text): #11
#     if text[i] == "o":  # Skip printing 'o'
#         i += 1
#         continue
#     print(text[i])
#     i += 1

# Python pass statement is used when a statement is required syntactically
#  but you do not want any command or code to execute."""

#EX:-6

# while True:
#     pass


# programs:-

"""1.Print numbers from 1 to 5.
    2. Sum of first 5 natural numbers.
    3.Reverse a number
    4.Print even numbers from 2 to 10
    5.Keep asking for input until correct password 
"""


# QU-1 print numbers 1 to 5 :
# a=0
# while a<5:
#     a+=1
#     print("Repetative no. :",a)
#     # print("Iteration no. {}".format(a))
      
# # QU-2 sum of first 5 natural numbers :
# print("Natural numbers: ")
# i=1 
# sum=0
# while i<=5:
#     print(i)
#     sum+=i
#     i+=1
# print(sum)

# QU-3 Reverse a number :
# x=123
# rev=0
# while x!=0:
#     digit=x % 10               # to print remainder vale
#     rev=rev * 10 + digit       # 0*10=0+3=3 
#     x=x // 10                  #123//10=12.3   
# print("Reverse numbers: ",rev)    

# # QU-4 print even numbers from 2 to 10 :
# a=0
# while a<10:
#     a=a+2
#     print("Even numbers",a)

# # odd 
# a=1
# while a<10:
#     a=a+2
#     print("Odd numbers: ",a)

# # 5 keep asking input until correct password :
# password="secure"
# while True:
#     password=input("Enter the pasword: ")
#     if password=="Secure" :
#         print("Password is correct!:")
#         break
#     else:
#         print("Password is incorrect :") 



# Qu-1 first 10 even numbers :
# a=0
# print("Even numbers")
# while a<10:
#     a=a+2
#     print(a)

# Q-2 first 10 Odd numbers :
# a=1
# print("Odd numbers")
# while a<10:
#     a=a+2
#     print(a)


# Q-3 first 10 natural numbers :
# a=0
# print("Natural numbers")
# while a<10:
#     a=a+1
#     print(a)

# Q-4 first 10 whole numbers :
# a=0
# print("Whole numbers")
# while a<=10:
#     print(a) 
#     a=a+1   

# Q-5 first 10 integers and their squares :
# x=0
# print("Integers")    
# while x>-5:
#     x=x-1
#     print(x)
# print("Squares")
# y=0
# while y<=10:
#     y+=1
#     print(y*y) 

# Q-6 series 10,20,30 ......300 :
# a=10
# print("Number series")
# print(a)
# while a<300:
#     a=a+10
#     print(a)

# Q-7 sreies 105,98,91......7
# a=105
# print("Number series")
# print(a)
# while a>7:
#     a=a-7
#     print(a)

# Q-8 first 10 natural numbers reverse order :
# a=11
# print("natural numbers reverse order")
# while a>0:
#     a=a-1
#     print(a)    

# Q-9 sum of first 10 Natural numbers :
# x=1
# y=0
# while x<=10:
#     y=y+x
#     x+=1
#     print(y) 
# print("Sum of 10 natural numbers: ",y) 
# USER INPUT:
# n=int(input("Enter n numbers: "))
# i=1
# s=0
# while(i<=n):
#     s=s+i
#     i=i+1
# print("Sum of natural numbers: ",s)    


# Q-10 sum of first 10 even numbers :
# i=2
# total=0
# while i<=20:
#        total=total+i
#        i=i+2
#        print(total)
# print("Sum of 10 even numbers: ",total)    



# Q-11 print table of a number entered from the user :
# num=int(input("Enter number:" ))
# i=0
# while i<10:
#     i=i+1
#     print(num,"*",i,"=",i*num)

# Q-12 to print all even numbers that falls between two numbers (exclusive both numbers) entered fro the user input :
# n=int(input("Enter the n number: "))
# i=0
# while i<=n:
#     if i%2==0:
      
#       print(i,end=" ") 
#     i=i+6 

#Q-13 To check wherther a number is prime or not using while loop :
# n=int(input("Enter number: "))
# total=0                                      
# for i in range(1,n+1):
#    if n%i==0:
#     total=total+1
# if total==2:
#         print(n,"is a prime number!")      
# else:
#     print(n,"is not prime number!")


# n=int(input("Enter number: "))        # using for loop
# i=1
# t=0
# while t<=n:
#     if n%1==0:
#         t=t+1
# if t==2:
#     print(n,"prime")
# else:
#     print(n,"not prime")          

# Q-14 to find the sum of the digits a accepted from the user:  
# n=int(input("Enter the number: "))
# total=0
# while n!=0:
#     a=n%10
#     total=total+a
#     n=n//10
# print("sum of digits is",total) 

# Q-15 To find the product of the digits of a number accepted from the user :
# a=int(input("Enter value of a: "))
# product=1
# while(a>0):
#     product=product*(a%10)
#     a=a//10
# print("Product of numbers: ",product)    

# Q-16 to reverse the number accepted from user :
# n=int(input("Enter n numbers: "))
# rev=0
# while n!=0:
#     digit=n % 10               
#     rev=rev * 10 + digit        
#     n=n // 10                     
# print("Reverse numbers: ",rev)

# Q-17 To dispay the number of names of the digits of a number entered by user
# For EX if the number is 123 then output is One Two Three:

# a={0:'zero',1:'One',2:'Two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# num=input("Enter n value: ")
# for i in num:
#     print(a[int(i)],end=" ")


# while:
# print("\n While loop")
# n=input("Enter value: ")
# d={    '0': 'zero',
#        '1': 'one',
#        '2': 'two',
#        '3': 'three',
#        '4': 'four',
#        '5': 'five',
#        '6': 'six',
#        '7': 'seven',
#        '8': 'eight',
#        '9': 'nine'    }

# i=0
# while i<len(n):
#     print(d[n[i]], end=" ")
#     i+=1



# Q-18 to print the fibonacci series till n terms (Accept n from user)
# n=int(input("Enter the number: "))
# x=0
# y=1
# while n>0:
#     z=x+y
#     x=y
#     y=z
#     n=n-1
#     print(z)

# Q-19 To print the factorial of a number accepted from user 
# n=int(input("Enter the number: "))
# f=1
# i=1
# while i<=n:
#     f=f*i
#     i=i+1
#     print("FActorial=",f)    

# # using for loop:
# n=int(input("Enter n value: "))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print("Factorial=",f)    

# Q-20 To check whether a number ARMSTRONG or not
# n=int(input("Enter n value: "))
# num=n
# s=0
# while n>0:
#     r=n%10
#     s=s+r*r*r
#     n=n//10
# if s==num:
#     print(num,"is an Armstrong")
# else:
#     print(num,"is not Armstrong")    


# Q-21 To add first n terms of the following Series using While Loop
# n=int(input("Enter n value:  "))
# s=0
# f=1      
# m=2
# i=1
# while i<=n:
#     s=s+(1/f)
#     f=f*m
#     m=m+1
#     i=i+1
# print("Sum of n terms: ",s)   

# Q-22 Enter the numbers till the user wants and at the end it should display the sum of all the numbers entered :
# Using for
# n=int(input("Enter n value: "))
# sum=0
# for i in range(n):
#     num=int(input())
#     sum=sum+num
# print("The total sum of the n value is: ",sum)

# Using while
# a=int(input("Enter the number: "))
# t=0
# i=0
# while True:
#     d=a%10
#     t+=d
#     a=a//10     
#     print("The total sum of all numbers is: ",t)



# Q-23 Enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers 
# entered:

# s=0
# p=0
# n=0
# while True:
#      a=int(input("Enter no. : "))
#      if a==0:
#           break
#      elif a>0:
#           p=p+1
#      else:
#           n=n+1                  
# print("Sum of positive numbers is: ",p)
# print("Sum of negative numbers is: ",n)  

# Q24. HCF of Two Numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# while num2 != 0:
#     num1,num2 =num2,num1 % num2
#     print("The given two numbers of HCF  is: ",num1)


# Q25. Decimal to Binary

# A = int(input("Enter a decimal number: "))
# b = bin(A)[2:]
# print("Binary formate of ",A,"is", b)


# Q26. Binary to Decimal

# x= input("Enter a binary number: ")
# y= int(x, 2)
# print("Decimal representation of", x, "is:", y)


# Q27. Palindrome Check

# n= input("Enter a number: ")
# if n==n[::-1]:
#     print(n, "is a palindrome.")
# else:
#     print(n, "is not a palindrome.")


# Q28. Sum of Sequence
n=int(input("Enter n value:  "))
s=1
f=1      
m=2
i=1
while i<=n:
    s=s+(1/f)
    f=f*m
    m=m+1
    i=i+1
print("Sum of n terms: ",s) 


# Q-29 Average of 10 Numbers
# total=0
# for a in range(10):
#     n=float(input("Enter number {}: ".format(a+1)))
#     total+=n
# average=total/10
# print(f"Average of the numbers:", average)


# Q-30 To accept 10 numbers from the user and display the largest & smallest number
# larg=0
# small=0
# for i in range(10):
#     n=int(input("Enter the value: "))
#     if n==0 or n==0:
#         break
#     else:
#         if n>larg:
#             larg=n
#         elif n>small:
#             small=n
# print("Largest number of the given numbers",larg)
# print("Smallest number of the given numbers",small)
