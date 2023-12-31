
# Iris Flower Classification

*   Create the dataset
*   Build the Model
*   Train the Model
*   Make Predictions
"""

# Commented out IPython magic to ensure Python compatibility.
# importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# importing Warning to avoid confusions

import warnings
warnings.filterwarnings('ignore')

# Load the data

data=pd.read_csv("/content/Iris.csv")
data.head()

"""Structure of the Data"""

data.shape

"""Central Tendency of the Data"""

data.describe()

data.info()

# get the attributes

data.columns

"""Missing Values"""

data.isnull().sum()

"""It is clear the there is no missing values in the dataset"""

data['Species']

data.Species.value_counts()

"""Training and Testing the data"""

X= data.iloc[:,1:5]
print(X)

y=data.iloc[:,5:]
print(y)

# Split the data to train and test dataset


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("X_train: ",X_train.shape)
print("X_test:  ",X_test.shape)
print("y_train: ",y_train.shape)
print("y_test:  ",y_test.shape)

"""Consider the Model

*   Logistic Regression

"""

from sklearn.linear_model import LogisticRegression

# An instance for the LogisticRegression model
regressor = LogisticRegression()

# Train the model on our train dataset
regressor.fit(X,y)

# Train the model with the training set

regressor.fit(X_train,y_train)

predictions = regressor.predict(X)
y_pred=regressor.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,y_pred))

"""Try with an another Model

Decision Tree
"""

from sklearn import tree

classifier=tree.DecisionTreeClassifier()

classifier.fit(X_train,y_train)

predictions=classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test,predictions))



"""# Conclusion

In conclusion the Accuracy is 100 % by using Logistic Regression and 96 % by using Decision Tree Algorithm.


*   Logistic regression is one of the best Clssification Algorithm used to Clasification.
"""
