# input=s2m4u8r1b2
# output=ssmmmmuuuuuuuurbb
# inp = "s2m4u8r1b2"
# out= "".join([char * int(inp[i + 1]) for i in range(0,len(inp), 2) for char in [inp[i]]])
# print(out)

# Q41. Write a program to print only odd numbers from the given list using while loop. L = [23, 45, 32, 25, 46, 33, 71, 90] 
# L=[23,45,32,25,46,33,71,90]
# i=0
# while i<len(L):
#     if L[i]%2!=0:     
#        print("odd numbers in the given list is",L[i])
#     i=i+1   

# Q42. Write a program to print all the factors of a number using while loop. 

# n= int(input("Enter a number: "))
# print(f"{n}")
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i=i+1 



# Q43. Write a python program to get the following output 
# 1—–49 => 2—–48 => 3—–47 and so on => 48—–2 => 49—–1 
# i=1
# j=49
# while i<=49 and j>=1:
#     print(f"{i}__{j}")
#     i=i+1
#     j=j-1


# Q44.Write a program to extract all the upper case character from the given string s=input(‘enter the string:’) 
# s=input("Enter the string: ")
# print(s.upper())

# Q45.Write a Program to separate positive and negative number from a list. x = eval(input('enter the list:')) 
# x=eval(input("Enter the list: "))
# pos=[] 
# nev=[]
# for i in x:
#     if i>=0:
#         pos.append(i)
#     else:
#         nev.append(i)
# print("Positive numbers:", pos)
# print("Negative numbers:", nev)

# using while :
# a=eval(input("Enter the list: "))
# s=0
# p=[]
# n=[]
# while s<=len(a):
#     if s >= 0:
#         p.append(s)   
#     else:
#         n.append(s)   
    
#     print('Positive numbers:', p)
#     print('Negative numbers:', n)        


# Q46.Write a program that appends the type of elements from a list. n = [23, 'Python',23.98] 
# n=[23,"python",23.98]
# tem=[]
# for i in n:
#     tem.append(type(i))
# print("type of element from a list:",tem)   


# Q47. Write a program to fetch only even values from a dictionary. dic = {'val1':10, 'val2':20, 'val3':23, 'val4':22 } 
# dic={"val1": 10, "val2": 20, "val3": 23, "val4": 22}
# x=list(dic.values())
# print(type(x))
# i=0
# while i<len(x):
#     if x[i]%2==0: 
#         print(f"even values from given dictionary is {x[i]}")
#     i=i+1  

# Q48.Write a program to extract all the string data items from the given list only if string is palindrome 
# def palindrome(s):
#     return s== s[::-1]  
# def palin(lst):
#     return [item for item in lst if isinstance(item, str) and palindrome(item)]
# n=['madam',24,'amma','anna','my','car','dog',90,'noon','moon',100]
# pal =palin(n)
# print("Palindrome strings:", pal)        


# n= input("Enter a number: ")
# if n==n[::-1]:
#     print(n, "is a palindrome.")
# else:
#     print(n, "is not a palindrome.")

 
 
# Q49.Write a program to extract all the special characters from the given string 
# def extract_special_characters(input_string):
#     special_characters = []
    
#     # Loop through each character in the string
#     for char in input_string:
#         # Check if the character is not alphanumeric and not a space
#         if not char.isalnum() and char != ' ':
#             special_characters.append(char)
    
#     return special_characters

# # Example usage
# input_string = "Hello, World! How's it going? #Python@123"
# special_chars = extract_special_characters(input_string)
# print("Special characters:",special_chars)

# Q50.Write a program to extract all the upper case character ,lower case character ,numbers and special characters into four 
# different output variables from the given string
# x = input("Enter the string: ")
# upper=''
# lower=''
# num=''
# spl=''
# for i in x:
#     if i.isupper():
#         upper+=i
#     elif i.islower():
#         lower+=i
#     elif i.isdigit():
#         num+= i
#     elif not i.isspace() :
#         spl+=i
# print("Uppercase characters:", upper)
# print("Lowercase characters:", lower)
# print("Digits:",num)
# print("Special characters:",spl)



# input="aaacczzzzkk"
# output=a3c2z4k2

# def sample(n):
#     res=""
#     count=1
#     for i in range(1,len(n)):
#         if n[i]==n[i-1]:
#             count+=1
#         else:
#             res=res+n[i-1] + str(count)
#             count=1
#     res+=n[i-1]+str(count)    
#     return res   
# inp="aaacczzzzkk" 
# out=sample(inp)
# print(out)

# Q51.Write a program to get the following output -   
# s=input("Enter the content: ")
# print(s)

# Q52.Write a program to convert all the lower case charater to upper case characters present in a given string 
# string =input("enter the characters :- ").upper()
# print(string)

#53.Write a program to convert all the lower case character to upper case character and upper case character to lower  case
#  character by keeping number and special character as it is 
# text = input("Enter a string :- ").swapcase()
# print(text)

# #54Write a program to extract all the lower case character from the given string only if its ascii value is even 
# text = input("enter the string:-")
# result=""
# for char in text :
#     if 'a' <= char <= 'z' :
#         if ord(char)%2 == 0:
#            result += char
# print(result)


#55 Write a program to get the following output input=’abcd’ output={‘a’:97,’b’:98,’c’:99,’d’:100} 
# text= input("enter the string:- ")
# out_put ={char:ord(char) for char in text }
# print(out_put)

#56 Write a program to get the following output input=’hello’  output={0:’h’ , 1:’e’ , 2:’l’ , 3:’l’ , 4:’o’} 


#57 Write a program to get the following output  input=[‘hai’ , 89 ,3.4 , ‘hello’ , 90 , ‘py’] 
#  output={‘hai’:’hi’ , ‘hello’:’hlo’ , ‘py’:’py’}
# x=['hai', 89, 3.4, 'hello', 90, 'py']
# result={}
# for i in x :
#     if type(i) == str :
#      s= i[::2]
#      if s!= i:
#          result[i] = s
# print(result)



# Q58.Write a program to get the following output input=‘hai hello’  output=’olleh iah’
# def reverse_each_word(input_string):
#     # Split the input string into words
#     words = input_string.split()
    
#     # Reverse each word and join them back with a space
#     reversed_words = ' '.join(word[::-1] for word in words)
    
#     return reversed_words

# # Example usage
# input_string = 'hai hello'
# output = reverse_each_word(input_string)
# print(output)

# 2nd ans.
# a='hai hello'
# print(a[::-1])

# 59. write a program to count the number of vowels present in a given string 
# s=input("Enter string content: ")
# vowels='aeiou'
# count=0
# for i in s:
#     if i in vowels:
#         count+=1
#         print("no. of vowels:",count)     


# Q60.Write a program to get the following output   input=‘hai hello good morning’ 
#  output={‘hai’:’a’ , ‘hello’: ‘l’ , ‘good’:’gd’ , ‘morning’:’n’}
#  
# def Navi(word):
#     if word=='hai':
#         return 'a'
#     elif word=='hello':
#         return 'l'
#     elif word=='good':
#         return 'gd'
#     elif word=='morning':
#         return 'n'
#     else:
#         return ''
# i={'hai':'a','hello':'l','good':'gd','morning':'n'}
# word=i.split()
# o={word:(word) for words in range(word)}
# print(o)    

# Q61- write a program get the following output input=['jiocinema.com','file.py','web.html']
# output=['com','py','html'] 

# def sample(n):
#     res=''
#     count+=1
#     for i in range(-1,range(n)):
#         if n[i]==n[i+1]:
#             count+=1
#         else:
#             res=res+n[i+1]
#             count=-1
#             res-=[+1]
#             return res
# input=['jiocinema.com','file.py','web.html']
# output=['com','py','html']
# print(output)

# Q62- write a program get the following output input=['jiocinema.com','file.py','web.html','amazon.com','text.py']
# output={'com':['jiocinema','amazon'],'py':['file','text'],'html':['web']}

# def simple (n):
#     res =''
#     count+=1
#     for i in range(-1,range(n)):
#         for i in range([0,3],[1,4],[2]):
#             count+=1
#         else:
#             res=res+n[i+1]
#             count=-1
#             res-=[+1]
#             res=res+n[i-1]
#             count=1
#             res+=[-1]
#             return res
# input=['jiocinema.com','file.py','web.html','amazon.com','text.py']
# output={'com':['jiocinema','amazon'],'py':['file','text'],'html':['web']}
# print(output) 

# Q63- write a program get the following output(count no of vowels) input={'hai hello'}
# output={'hai':2,'hello':2}
# def sample(n):
#     res =''
#     count+=2
#     for i in range(1,range(n)):
#         if n[i]==n[i+2]:
#             count+=2
#         else:
#             res=res+n[i-2]
# input='hai hello'
# output={'hai':2,'hello':2}
# print(output)

# Q64.Write a program to extract all the string values present in the list collection 
# only if the last character is upper case. Concatenate the extracted output using'*'
# def extract_and_concatenate(strings):
#     # Extract strings where the last character is uppercase
#     result = [s for s in strings if s[-1].isupper()]
    
#     # Concatenate the result with '*' between each string
#     concatenated_result = '*'.join(result)
    
#     return concatenated_result

# # Example usage
# strings = ["hello", "world", "Python", "java", "CodeX", "exampleZ"]
# output = extract_and_concatenate(strings)
# print("Concatenated Output:",output)

# Q65.write a program to extract all the list data items present in list collection 
# only if it is having middle value , that value is integer and having even number 
# at start

# def sam(lis):
#     result = []
#     for lst in lis:
#         # Check if the list has an odd length (so there's a middle value)
#         if len(lst) % 2 != 0:
#             index = len(lst) // 2  # Find the middle index
#             value = lst[index]
#             if isinstance(value, int) and value % 2 == 0:
#                 result.append(lst)
    
#     return result
# list_collection = [
#     [1, 2, 4, 6, 8],    # middle value is 4, even
#     ['a', 'b', 3, 'd'],  # no integer in the middle
#     [5, 7, 2, 6, 10],    # middle value is 2, even
#     [1, 3, 5, 7, 9],     # middle value is 5, odd
#     [11, 22, 33, 44]  ]   # even number at the start but no middle integer
# output =sam(list_collection)
# print("Extracted Lists:", output)

# Q66- write a program get the following output
# input='just looking like wow'
# output='jusT LOOKING Like wow'
# def simple(n):
#     res=''
#     for i in range(1,range(n)):
#             return res
# input='just looking like wow'
# output='jusT LOOKING Like wow'
# print(output)

# Q67.Program to find the common elements in two sets using a while loop 
# set1 = {1, 2, 3, 4, 5} 
# set2 = {3, 4, 5, 6, 7} 
# def find_common_elements(set1, set2):
#     common_elements = set()  # Convert set1 to a list to use it with a while loop
#     set1_list = list(set1)
#     index = 0                # Use a while loop to iterate through set1_list
#     while index < len(set1_list):
#         if set1_list[index] in set2:
#             common_elements.add(set1_list[index])
#         index += 1
#     return common_elements
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# common_elements = find_common_elements(set1, set2)
# print("Common elements:", common_elements)


# Q68.Program to check if a number is a perfect number or not using while loop 
# def is_perfect_number(number):
#     sum_of_divisors = 0
#     divisor = 1
#     while divisor <= number // 2:
#         if number % divisor == 0:
#             sum_of_divisors += divisor
#         divisor += 1       # Check if sum of divisors is equal to the number
#     if sum_of_divisors == number:
#         return True
#     else:
#         return False
# num = 28
# if is_perfect_number(num):
#     print(f"{num} is a perfect number.")
# else:
#     print(f"{num} is not a perfect number.")

# Q69.Program to find the length of the longest substring without repeating 
# characters in a given string using while loop 

# def longest_unique_substring(s):
#     # Create a set to store characters in the current window
#     char_set = set()
#     max_length = 0
#     start = 0  # Start index of the window   
#     while start < len(s):
#         # If the current character is not in the set, add it
#         if s[start] not in char_set:
#             char_set.add(s[start])
#             max_length = max(max_length, len(char_set))
#             start += 1
#         else:
#             # If the character is already in the set, remove the leftmost character
#             char_set.remove(s[start - len(char_set)])
    
#     return max_length

# # Example usage
# input_string = "abcabcbb"
# result = longest_unique_substring(input_string)
# print("Length of the longest substring without repeating characters:",result)

# s1="nani" , s2="nana" to  print=>na :

# def luc(a,b):
#     pre= ""
#     for i in range(min(len(a), len(b))):
#         if a[i] == b[i]:
#             pre+= a[i]
#         else:
#             break
#     return pre
# s1 = "nani"
# s2 = "nana"
# out=luc(s1,s2)
# print(out)

# S1='NANI'
# S2='NANA'
# a=set(S1)
# b=set(S2)
# print("".join(list(a&b)))


# l1=[1,2,3,4,5,7]  and  l2=[7,3,8,9,10,1]  =>  o/p : [3,7,1]

# l1=[1,2,3,4,5,7]
# l2=[7,3,8,9,10,1]
# a=set(l1)
# b=set(l2)
# print(type(l1))
# print(type(l2))
# c=a.intersection(b)
# d=list(c)
# print(d)

# # s1="Hello"   s2="world"  then output is => Hweolrllod

# def mer(s1,s2):
#           i=0
#           j=0
#           res=''
#           while i<len(s1) and j<len(s2):
#                res=res+s1[i]+s2[j]
#                i=i+1
#                j=j+1
#           return res       
# print(mer('hello','world'))

# # input=[1,2,3,4,5,7] , target=9 then should be print [3,4] is index numbers :
  
# def define(l,target):
#         for i in range(len(l)):
#                 for j in range(i+1,len(l)):
#                         if l[i]+l[j]==target:
#                                 return[i,j]
# l=[1,2,3,4,5,7] 
# target=9
# ou=define(l,target)
# print(ou)

# l=[1,2,3,4,5,7]
# target=9
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==target:
#             print([i,j])
#             break 

# Q99.Write a program for number game 



# Q100.Write a program to print ‘Thank you’ for n times          
n=int(input("Enter no.: "))
for i in range(n):
     i='Thank you'
     print(i)