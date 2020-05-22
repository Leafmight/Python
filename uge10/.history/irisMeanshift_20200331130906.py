import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())


df = pd.DataFrame(iris_data,columns=['Species_I. virginica'])
print(df)
for d in iris_data['Species_I. virginica']:
    if(d==1):
        iris_data.plot.scatter(x=0,y=1, c='r')
#df.loc[df['Species_I. virginica']]
#if(iris_data.isin({'Species_I. virginica': [1]})=='True'):
#    iris_data.plot.scatter(x=0,y=1, c='r')
plt.show()