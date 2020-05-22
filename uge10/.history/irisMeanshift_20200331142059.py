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

plt.scatter(x= virginica['Sepal length'], y=virginica['Sepal width'], color='r')
plt.scatter(x= versicolor['Sepal length'], y=versicolor['Sepal width'], color='g')
plt.scatter(x= setosa['Sepal length'], y=setosa['Sepal width'], color='b')
#plt.show()

from sklearn.cluster import estimate_bandwidth
print(estimate_bandwidth(virginica),quantile=0.2)
print(estimate_bandwidth(versicolor),quantile=0.2)
print(estimate_bandwidth(setosa),quantile=0.2)
print(estimate_bandwidth(iris_data),quantile=0.2)