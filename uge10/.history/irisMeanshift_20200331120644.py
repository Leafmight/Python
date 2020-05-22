import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

iris_data.plot.scatter(x = 5, y = 6)
plt.show()