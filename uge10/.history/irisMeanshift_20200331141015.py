import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle


iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

virginica = iris_data.loc[iris_data['Species_I. virginica']==1]
versicolor = iris_data.loc[iris_data['Species_I. versicolor']==1]
setosa = iris_data.loc[iris_data['Species_I. setosa']==1]

plt.scatter(x= virginica['Sepal lenght'], y=virginica['Sepal width'], color='r')
plt.scatter(x= versicolor['Sepal lenght'], y=versicolor['Sepal width'], color='g')
plt.scatter(x= setosa['Sepal lenght'], y=setosa['Sepal width'], color='b')
plt.show()
