# import numpy as np
# # x=np.read_csv("C:\\Users\\Navya\\Downloads.csv")
# import pandas as pd
# x=pd.read_csv("C:\\Users\\Navya\\Downloads.csv")

# x = pd.read_csv("D:\\kishore\\Popular_Spotify_Songs.csv")
# # conditions (<,>,==)
# x[x['album_total_tracks']<10]


# import pandas as pd
# import numpy as np
# # import matplotlib.pyplot as plt 
# x=pd.read_csv("D:\\kishore\\Popular_Spotify_Songs.csv")
# x['Stress_Level'] = x['Stress_Level'].str.capitalize()
# x['Stress_Level'] = x['Stress_Level'].str.lower()
# x['Stress_Level'] = x['Stress_Level'].str.upper()
# x.plot(x='Study_Hours_Per_Day', y='Physical_Activity_Hours_Per_Day', kind='line')
# x['Study_Hours_Per_Day'].plot(kind='hist') 

# x['Stress_Level'] = x['Stress_Level'].str.capitalize()
# x['Stress_Level'] = x['Stress_Level'].str.lower()
# x['Stress_Level'] = x['Stress_Level'].str.upper()
# x.plot(x='Study_Hours_Per_Day', y='Physical_Activity_Hours_Per_Day', kind='line')
 
 
# import matplotlib.pyplot as plt
# a=[2,4,5,6,7,8,9]
# b=[11,22,44,3,555,77]
# plt.plot(x,y, color="green",marker="*",markerfacecolor="red")



# # STEP-1: IMPOORTING NECESSARY LIBRARIES
# import matplotlib.pyplot as plt
# from scipy import stats
# # STEP-2: INITAILIZING INPUTS AND OUTPUTS
# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# # STEP-3: APPLYING INPUTS AND OUTPUTS TO THE LINEAR REGRESIION TECHNIQUE
# slope, intercept, r, p, std_err = stats.linregress(x, y)
# # STEP-4: DEFINING PREDICTION
# def myfunc(x):
#   return slope * x + intercept
# polynomial regression : it will display graph in the curved form , it is only one dimesional 




# # step-1: 
# # import necessary libraries 
# import numpy # mathemtical and statistical clauclations 
# import matplotlib.pyplot as plt # graphical representation
# # step-2
# # initialize inputs and outputs
# a= [12,22,33,44,55,66,77,999,111]
# b= [11,222,33,44,777,88,90,80,70]
# # find the length of x and y to check whether both legth is same or not 
# print(len(a))
# print(len(b))
# # step-3
# # applying inputs to ploynomial regression 
# mymodel = numpy.poly1d(numpy.polyfit(a,b, 10))
# # here 10 is nothing but curved represention of graph which predicted values
# # if you want to display the polynomic=al predicted values then we have to print the mymodel 
# print(mymodel)
# # step-5: plotting the graph by integrating inputs and predicted values 
# plt.scatter(a,b)
# plt.plot(myline, mymodel(myline))
# plt.show()



# x=df1[['Quantity','UnitPrice']]
# y=df1['TotalAmount']
# z=linear_model.LinearRegression()
# z.fit(x,y)
# predicted_output=z.predict([[3,106]])
# print(predicted_output)
 
"""
#step-1:import necessary librbries  
import  pandas as pd 
import numpy as np
# step-2: uploading datatset 
dataset = pd.read_csv("D:\\kishore\\Popular_Spotify_Songs.csv")
#step-3: intializing inputs and outputs
x = dataset[['track_number','artist_followers']]
y = dataset['album_total_tracks']
x = x.to_numpy()

y = y.to_numpy()

y=y.reshape(-1,1)
 
#step-4:train and test the data 

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.3,random_state=42)
# step-5: apply trained data to the regression techniue 

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()

model.fit(xtrain,ytrain)
# step-6: find out prediction 

ypred = model.predict(xtest)

print(ypred)
data = pd.DataFrame(data={"predicted output":ypred.flatten()})
"""

def common_chars(str1, str2):
    # Remove spaces and convert to sets for case-sensitive comparison
    set1 = set(str1.replace(" ", ""))
    set2 = set(str2.replace(" ", ""))
    
    common = set1.intersection(set2)
    
    if len(common) == 0:
        return -1
    else:
        return "".join(sorted(common))

# Sample input
str1 = "I like Python"
str2 = "Java is a very popular language"
print(common_chars(str1, str2))  # Output: lieyon