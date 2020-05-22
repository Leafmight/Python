import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt
from itertools import cycle


headers = ["weight", "height", "typez"]

data = pd.read_csv("rodents.csv", names = headers,header=None, skiprows=1)


# Convert gender to 0 or 1
label_enc =preprocessing.LabelEncoder()
data['typez'] = label_enc.fit_transform(data['typez'].astype(str))
data.head()

y = data["typez"]



x = data.drop("typez",axis='columns')


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)


model = DecisionTreeClassifier(criterion="gini", max_leaf_nodes=2, random_state=0)

model.fit(x_train, y_train)

y_predicted = model.predict(x_test)
ac = accuracy_score(y_test,y_predicted)
print(ac)

y[y != 0] = -1
y[y == 0] = 1


trainings_data = [(d[:2], l) for d, l in zip(x, y)]

def plot_data(data, w_line=None):
    """
    show data in 2d petal length vs width and target being 1 or -1 (indicating if flower is iris setosa or not.)
    Parameters:
    data: array of type tuple(array[petal_height, petal_width], target) target is either 1 or -1
    w_line: a visual line to seperate the 2 clusters. If none is provided it will not show
    """
    # print(data[:10])
    data_points, class_labels = list(zip(*data))
    data_points = np.array(data_points)
    class_labels = np.array(class_labels)

    colors = cycle('bgrcmy')
    for l, col in zip(np.unique(class_labels), colors):
        d =  data_points[class_labels == l]
        x = d[:,0]
        y = d[:,1]
        plt.scatter(d[:,0], d[:,1], c=col, label=l)
    
    if w_line:                  # only plot a division line if one exists
        l = np.linspace(0, 8.5) # 50 evenly spaced numbers for the x axis
        m, b = w_line           # m = slope, b = intercept
        plt.plot(l, m * l + b, 'y-', lw=2) # lw is line width

    plt.axis([0, 8.5, 0, 5])
    plt.title('Iris Characteristics')
    plt.xlabel('length')
    plt.ylabel('width')
    plt.legend()
