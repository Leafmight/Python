import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

titanic_data.drop(['Sepal length','Sepal width','Petal length','Petal width'],'columns',inplace=True)
data_1d = np.rint(iris_data).astype(np.uint8)
y = np.zeros(np.shape(iris_data))
iris_data.plot.scatter(data_1d, y)
plt.show()