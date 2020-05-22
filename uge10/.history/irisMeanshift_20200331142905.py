import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle
from sklearn.cluster import MeanShift
from sklearn.cluster import MeanShift, estimate_bandwidth

def mean_shift(data, n_samples=1000):
    bandwidth = estimate_bandwidth(data, quantile=0.2, 
                                   n_samples=n_samples)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(data)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters = len(labels_unique)

    print('Number of estimated clusters : {}'.format(n_clusters))
    
    return labels, cluster_centers, n_clusters


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
print(estimate_bandwidth(virginica,quantile=0.2))
print(estimate_bandwidth(versicolor,quantile=0.2))
print(estimate_bandwidth(setosa,quantile=0.2))
print(estimate_bandwidth(iris_data,quantile=0.2))
analyzer = MeanShift(bandwidth=1) 
print(analyzer.fit(iris_data))
print(mean_shift(iris_data))