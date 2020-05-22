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

def pla(training_data, no_iterations=10000, eta=0.5):
    """
    Find the proper weights to use in the perceptron based on data and target
    Parameters:
    training_data: list of vectors, as predictors zipped with a target value
    no_iterations: number of times to adjust the weights to get them as close as possible to the optimal number
    eta: the learning rate (prevent learning to go pendulum from one extreme error to the opposite)
    """
    
    dim = len(training_data[0][0]) # len = 2 (petal width and height)
    weights =  np.random.random(dim) # error and weights (for x and y) start out as random numbers
    
    # initial_error
    error = np.random.random()
    weight_history = [np.copy(weights)]

    for i in range(no_iterations):
        #pdb.set_trace()
        #breakpoint()
        inp_vec, expected_label = training_data[i % len(training_data)] # expected labels are 1 or -1
        perceptron_output = perceptron(inp_vec, weights) # perceptron output id a decimal between 0 and 1
        error = expected_label - perceptron_output       # error 
        weights += eta * error * inp_vec # accumulate the weights
        weight_history.append(np.copy(weights))
        
    return weights, weight_history 
        

learned_weights, weight_history = pla(trainings_data)
# print(weight_history)
print(learned_weights)
