import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())

iris_data.plot.skatter(x=0,y=1, c='red')
plt.show()