import numpy as np 
import pandas as pd 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
from sklearn import preprocessing


headers = ["weight", "height", "types"]

data = pd.read_csv("rodents.csv", names = headers)


data.head()

y = data["types"]

print("------------------------",y)

x = data.drop("types",axis='columns')

print("------------------------",x)
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3)

print("++++++++++++++++++")
print(x_train, x_test, y_train, y_test)
print("++++++++++++++++++")



model = DecisionTreeClassifier(criterion="gini", max_leaf_nodes=2, random_state=0)

model.fit(x_train, y_train)

y_predicted = model.predict(x_test)

print(accuracy_score(y_test,y_predicted))
