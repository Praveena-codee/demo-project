## import dependenacies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import flask
from flask import request
#from flask_cors import CORS
import pickle
from flask import Flask, jsonify
from sklearn.linear_model import LogisticRegression


#### Read the csv file into a pandas DataFrame

df = pd.read_csv("Resources/activities.csv")
df.head(10)


df = df.dropna()
df = df.drop_duplicates()
df.head(10)

df.shape

X = df.loc[:,['activities','devicesBR','devicescount','usage','Rules','enforce','behaviour','rate']]
y = df.ratesleep

X.head()

from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
X.loc[:,['activities','devicesBR','devicescount','usage','Rules','enforce','behaviour','rate']]= \
X.loc[:,['activities','devicesBR','devicescount','usage','Rules','enforce','behaviour','rate']].apply(enc.fit_transform)

X.head()

y.head()

##Barplot to visualize the number of samples for each category in the target variable
df['ratesleep'].value_counts().plot.bar( rot=30, color="green", width=0.5)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn import tree
model = tree.DecisionTreeClassifier()

model.fit(X, y)

from sklearn.datasets import make_regression

X,y = make_regression(n_samples=9, n_features=1, bias=100)
plt.scatter(X, y)

##Is bath, often, mean rating good ?

model.predict([[1,7,0,0,0,1,7,8]])

### Extracting model for flask
import joblib
joblib.dump(model,'sleep_analysis.ml')

# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()

log_reg = LogisticRegression()
log_reg.fit(X, y)

# #Fitting model with trainig data
# regressor.fit(X, y)

inputt=[int(x) for x in "0 1 2 3 4 5 6 7 8".split(' ')]
final=[np.array(inputt)]

b = log_reg.predict_proba(final)

# Saving model to disk
pickle.dump(log_reg, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1,7,0,0,0,1,7,8]]))