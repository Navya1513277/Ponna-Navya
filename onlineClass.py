
# name=str(input("Enter your name: "))
# num=input("Enter your mobile number:")
# address=str(input("Enter your address:"))
# mail=input("Enter your mail: ")



# 19-11-25:
# complex -> real & imaginary part:
# x=3+4j
# print(x)
# print(type(x))
# print(x.real)
# print(x.imag)

# y=complex(input("Enter the num: "))
# print(y)
# print(type(y))


# # boolean:
# a=True
# print(type(a))

# # user input:
# b=bool(input("Enter the statement:"))
# print(type(b))
# print(b3)

# DATA STRUCTURE:
# x=99
# print(type(x))

# # # list []
# a=[1,2,3,4,5,9]
# print(a)
# print(type(a))
# b=len(a)
# print(b)

# b=[1,2,3,4,7]
# print(type(b))

# a[1]=20
# print(a)
# a[-1]=30
# print(a)
# a[3]='hai'
# print(a)

# #  20-11-15:
# #  tuple( )
# x=(2,4,6,7)
# print(type(x))
# print(x)

# a=("hello","hai",)
# print(a)
# print(type(a))
# print(len(a))

# a=(True,False,True,False)
# print(a)

# a=("xx","rr","gg","tt")
# print(a[2])
# print(a[-1])

# # ṣets{ }
# a={'hello',1,True,False,0,'hello',9,9,9}
# print(type(a))
# print(a)

# # dictionary{ }
# d={'name':"Navya",'city':"tpt",'state':"Ap"}
# print(d)
# print(type(d))


# import pandas as pd
# import nump as np
# import matplotelib.pyplot as plt
# x=pd.read_csv("D:\NAVYA navi")
# print(x)

# libraries
 
# pandas
 
#  To install pandas library " pip install pandas"
 
 
# In pandas we ddo have two keyword
 
# " dataframne"  "series"
 
# import pandas as pd
 
# x = {'Employee name':['shabnam','keerti','durga','sujata'], 'Employee age ' : [27,34,26,30], 'employee salary':[300000,500000,400000,350000]}
 
# y = pd.DataFrame(x, index = [1,2,3,4])
 
# print(y)
 
 
 
# import pandas as pd
# x = [1,2,3,4,5]
# y = pd.Series(x, index = [1,2,3,4,5])
# print(y)
# # x=pd.read_csv("D:\\kishore\\data.csv")

# import numpy as np
# x=np.read_csv("D:\\kishore\\data.csv")
# x=[99,88,55,43,33,8]
# # y=np.series(x,length[99,88,55,43,33,8])
# print(x)

# import numpy as np
# c=np.array([[[12,22,33,4],[6,8,7,34]],[[9,89,55,4],[3,6,7,8]]])

# c=np.array([[[1,2,3,4,5],[9,8,7,6,6],[6,9,81,31,4]],[[88,12,22,3,5],[11,13,9,15,17],[6,8,9,3,11]]])
# print(c)

# indexing --------- extracting signle element from the given array ---- single dimesion  
# import numpy as np
# a = np.array([10, 11, 51,8])
# print(a[0])

# import numpy as np
# b = np.array([14, 32, 73, 24])
# print(a[1])
# arr=np.concatenation((a,b))
 
# # extracting two dimension ---- here two list are there it means indexing 0 is first list and indexing 1 is second list 
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[1, 4])
# import numpy as np
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('5th element on 2nd row: ', arr[1, 4])

# # three diemsional extraction -----------
# import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[1, 0, 2])
 
# # joining can be done using0-----concatenate
# import numpy as np
# x = np.array([1, 2, 3])
# y= np.array([4, 5, 6])
# arr = np.concatenate((x,y))
# print(arr) 

# # joining can be done using0-----concatenate
# import numpy as np
# x = np.array([1, 2, 3])
# y= np.array([4, 5, 6])
# arr = np.concatenate((x,y))
# print(arr)

# # spliting --array_split
# import numpy as np
# x= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# newarr = np.array_split(x, 2)
# print(newx)
 
# # spliting --array_split
# import numpy as np
# arr = np.array([11,22,33,44,556,7,9])
# newarr = np.array_split(arr, 2)
# print(newarr)
 
# import numpy as np
# i= np.array([11,22,33,44,556,7,89,66])
# a= np.where(i%2==1)
# print(a) 


# conditions
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 2)
# print(x)
 
# import numpy as np 
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)


# data distribution -------------
 
# normal data distribution
 
 
# uniform data distribution
 
 
# import numpy 
# import matplotlib.pyplot as plt
# x = numpy.random.uniform(0.0, 6, 25)
# print(x)
# plt.hist(x)
# plt.show() 


# polynomial regression : it will display graph in the curved form , it is only one dimesional 
# step-1: 
# import necessary libraries 
# import numpy 
# import matplotlib.pyplot as plt 
# a=[12,22,33,44,55,66,77,999,111]
# b=[11,222,33,44,777,88,90,80,70,59,400,22,343,12,89,876,567]
# print(len(a))
# print(len(b))
# mymodel = numpy.poly1d(numpy.polyfit(a,b))
# print(mymodel)
# plt.scatter(a,b)
# plt.plot(myline, mymodel(myline))
# plt.show()
# step-2

# initialize inputs and outputs

 
 
# find the length of x and y to check whether both legth is same or not 
# print(len(x))
# print(len(y))

 
# step-3
# applying inputs to ploynomial regression
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 10))
 
# here 10 is nothing but curved represention of graph which predicted values
# if you want to display the polynomic=al predicted values then we have to print the mymodel 
# print(mymodel)
 