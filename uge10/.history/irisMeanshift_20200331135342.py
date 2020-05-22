import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle
from sklearn.cluster import MeanShift, estimate_bandwidth

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

fig = plt.figure()
virginica = iris_data.loc[iris_data['Species_I. virginica']==1 ]
versicolor = iris_data.loc[iris_data['Species_I. versicolor']==1]
setosa = iris_data.loc[iris_data['Species_I. setosa']==1]

virginica.plot.scatter(x=0, y=1, c='r')
versicolor.plot.scatter(x=0, y=1, c='b')
setosa.plot.scatter(x=0, y=1, c='g')

plt.figure.show()
