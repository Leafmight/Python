import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 


iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

fig = plt.figure()
virginica = iris_data.loc[iris_data['Species_I. virginica']==1 ]
versicolor = iris_data.loc[iris_data['Species_I. versicolor']==1]
setosa = iris_data.loc[iris_data['Species_I. setosa']==1]

ax1= virginica.plot.scatter(x=0, y=1, c='r')
ax2 = versicolor.plot.scatter(x=0, y=1, c='b')
ax3 = setosa.plot.scatter(x=0, y=1, c='g')

print(ax1 == ax2 == ax3)
