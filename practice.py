# number = input("Enter the number: ")
# length_of_number = len(number)
# armstrong_number=int(number[0])**length_of_number+int(number[1])**length_of_number+int(number[2])**length_of_number
# print(armstrong_number==int(number)) 


# a=23
# b=11
# c=9.5
# s1="Hello"
# s2="There"
# print(a+b)
# print(type(a==b))
# print(b+c)
# print(type(b+c))
# print(s1+s2)
# print(type(s1+s2))

# str='Hi There!'
# tup=('Mon','Tue','Wed','Thu','Fri')
# lst=['Jan','Feb','Mar','Apr']
# dict={'1D:Line','2D:Triangle','3D:Sphere'}
# print(len(str))
# print(len(tup))
# print(len(lst))
# print(len(dict))

# import datetime
# x=datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))


# import datetime
# x=datetime.datetime.now()
# print(x)


# a=("a","b","c","d","e","f","g","h")
# x=slice(2)
# print(a[x])

# a=("b","g","a","d","f","c","h","e")
# x=sorted(a)
# print(x)

# x=chr(97)
# print(x)

# x=abs(-7.25)
# print(x)

# def my_function(x):
#     return 5*x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function():
#     print("Hello from a function")
# my_function()

# def my_function(fname,lname):
#     print(fname+" "+lname)
# my_function("suma","sir") 
   


# User input 
# 1  To find smallest number of given 2 numbers:
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# if a<b:
#     print(a ,"is a smallest number")
# elif a>b:
#     print(b ,"is a smalest number")


# 2  To find smallest number of given 3 numbers:
# x=int(input("Enter the x value: "))
# y=int(input("Enter the y value: "))
# z=int(input("Enter the z value: "))
# if x<=y and y<=z:
#     print("x is a smallest number")
# elif y<=x and y<=z:
#     print("y is a smallest number")
# elif z<=x and z<=y:
#     print("z is a smallest number")    

# 99
# 3 to check whether the given number is odd and even :
# a=int(input("Enter a=")101

# # 4  To check whether the given numbers is in between 1 and 100 :
# ab=int(input("Enter the value:"))
# if 1<=ab<=100:
#     print(ab,"is a correct value")
# else:
#     print(ab,"is worng, Please enter the numbers between 1 to 100")    
        


# n=int(input("Enter the a value: "))
# sum=0
# n=0
# while n>=0:
#     a=int(input())
#     print("n value:",n)
#     sum=sum+n
#     n=n+1
#     print(sum)
# print("The total sum of the numbers is: ",sum)    

# x="That's"
# y="Hello world"
# c="Let's go"
# print(x,y)
# print(c)

# # LOVE calculator
# name_1=input('what is your name:  ' )
# name_2=input('Enter his/her name:  ')
# combine_string=name_1+name_2
# lower_case=combine_string.lower()
# t=lower_case.count('t')
# r=lower_case.count('r')
# u=lower_case.count('u')
# e=lower_case.count('e')
# true=t+r+u+e
# l=lower_case.count('l')
# o=lower_case.count('o')
# v=lower_case.count('v')
# e=lower_case.count('e')
# love=l+o+v+e
# love_score=(true)+(love)
# love_score=int(love_score)
# if love_score<10 or love_score>90:
#     print(f'Your love score is {love_score} and you go together like coke and mentos')
# elif love_score>=40 and love_score<=50:
#     print('Your score is',love_score,'and you are alright together ')
# else:
#      print(f'Your love score is {love_score}')

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# class Solution:
#     def romanToInt(self, s):
#         roman_to_int = {
#             'I': 1, 'V': 5, 'X': 10, 'L': 50,
#             'C': 100, 'D': 500, 'M': 1000
#         }
#         result = 0
#         for i in range(len(s)):
#             if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
#                 result -= roman_to_int[s[i]]
#             else:
#                 result += roman_to_int[s[i]]
#         return result


name=str(input("Enter your name: "))
num=input("Enter your mobile number:")
address=str(input("Enter your address:"))
mail=input("Enter your mail: ")