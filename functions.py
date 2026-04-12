# EX:- 1
# def function_name():
#     print("Hello World")
# function_name()

# EX:-2
# def addition(a,b): # parameters
#    c= a+b
#    print(c)
# addition(1,2) # arguments
# addition(4,6)

#EX:-3
# def multiplication(num1,num2):
#     return num1*num2
# obj1=multiplication(7,3)
# obj2=multiplication(5,7)
# print(multiplication(7,9))
# print(obj1)
# print(obj2)

#EX:-4
# def my_function(fname):
#     print(fname+"Rfness")
# my_function("hllo")
# my_function("hi")

#EX:-5
# def my_function_name(a,b):
#     print(a,b)
# my_function_name(b=5,a=3)

#EX:-6
# def my_function(*a):
#     print(a)
#     print(a[1])
# my_function(1,2,3,4)

# EX:-7 
def my_function(**kwargs):
    print(kwargs.get("fname"))
my_function(fname="hello",Iname="hi")

#EX:-8
# def functionName(a="Hello"):
#     print(a)
# functionName()
# functionName("hi")
# functionName("hiii")

# def addition(a,b):
#     return a+b
# print(addition(3,5))


# Q-21 To add first n terms of the following Series:
# def sumOfSeries(a):
#     s = 0
#     fact = 1
#     i = 1

#     while i <= a:
#         fact *= i
#         s += 1 / fact
#         i += 1
#     return s
# a= int(input("Enter the value of n: "))
# print(f"Sum of the series of {a} terms: {sumOfSeries(a):.6f}")

# Q-22 Enter the numbers till the user wants and at the end it should display the sum of all the numbers entered :
# def sum_of_numbers():
#     s = 0  
#     for i in range(n):
#         num=int(input())
#         s=s+num
#         print("The total sum of the n value is: ",s)
# n=int(input("Enter the n value: "))        
# sum_of_numbers()

# Q-23 Enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers 
# def count_positive_negative():
#     positive_count = 0
#     negative_count = 0

#     while True:
#         num = int(input("Enter a number (enter 0 to stop): "))

#         if num == 0:  
#             break
#         elif num > 0:
#             positive_count += 1  
#         else:
#             negative_count += 1  

#     print("Total positive numbers entered:", positive_count)
#     print("Total negative numbers entered:", negative_count)

# count_positive_negative()


# Q24. HCF of Two Numbers
# def hcf():
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))

#     while b!=0:
#         a,b=b,a%b  
#         print("HCF of the given numbers is:",a)
# hcf()


# Q26. Binary to Decimal
# def binary_to_decimal():
#     binary = input("Enter a binary number: ")
#     decimal = int(binary, 2)  
#     print("Decimal representation:", decimal)
# binary_to_decimal()


# Q25. Decimal to Binary:
# def decimal_to_binary():
#     decimal = int(input("Enter a decimal number: "))
#     binary = bin(decimal)[2:]  
#     print("Binary representation:", binary)

# decimal_to_binary()