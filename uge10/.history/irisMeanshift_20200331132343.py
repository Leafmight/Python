import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from itertools import cycle
from sklearn.cluster import MeanShift, estimate_bandwidth

iris_data = pd.read_excel('iris_data.xlsx')
print(iris_data.head())

iris_data = pd.get_dummies(iris_data,columns=['Species'])
print(iris_data.head())



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

labels, cluster_centers, n_clusters = mean_shift(iris_data)


colors = cycle('bgrcmy')
for k, col in zip(range(n_clusters), colors):
    my_members = (labels == k)
    
    
    x = iris_data[my_members, 0]
    
    iris_data.plot.scatter(x=x,y=1,c=col)
    
    

plt.show()




if(iris_data[4:]):
    iris_data.plot.scatter(x=0,y=1,c='r')

plt.show()
