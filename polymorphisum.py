# Method overloading:
# class Myclass:
#     def myFuntion(self,a=8,b=9,c=None):
#         print(a,b,c)
# myclass=Myclass()
# myclass.myFuntion(1,2,3)
# myclass.myFuntion(1,2,34)
# myclass.myFuntion(1,3)
# myclass.myFuntion()

# 
# class Preethi:
#     def ammulu(self,a="adithya",b="praneeth",c="jeevan",d="nandhini"):
#         print(a,b,c,d)
# obj=Preethi()
# obj.ammulu(1,2,3,4)
# obj.ammulu(3,4)
# obj.ammulu(1,2)
# obj.ammulu(2,3)
# obj.ammulu(1,4)

# class Student():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self,a=None,b=None,c=None):
#         s=0
#         if (a!=None,b!=None,c!=None):
#             s=a+b+c
#         elif(a!=None and b!=None):
#             s=a+b
#         else:
#             s=c
#             return s
# s1=Student(50,30) 
# print(s1.sum(20,30,80))
# print(s1.sum(20,30))
# print(s1.sum(30))       

# Method overriding :
# class Father():
#     def show(self,a,b):
#         print("Main")
#         c=a+b
#         print(c)
#         return
# class Son(Father):
#     def show(self,a,b):
#         print("Subclass")
#         c=a+b
#         print(c)    
#         return c