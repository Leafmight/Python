import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report



headers = ["weight", "height", "type"]

data = pd.read_csv("rodents.csv", header = None, names = headers, skiprows=1)


data.head()

y = data["type"]

print("------------------------",y)

x = data.drop("type",axis='columns')

print("------------------------",x)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)

model = DecisionTreeClassifier(criterion="gini", max_leaf_nodes=3, random_state=0)

model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

print(accuracy_score(y_test,y_predicted))
