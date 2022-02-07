# Importing the libraries

#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
import pickle


df = pd.read_csv('cars.csv')

X = df.drop(['current price','v.id'], axis=1)
y = df['current price']


#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#Fitting model with trainig data
lr.fit(X, y)

# Saving model to disk
pickle.dump(lr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2, 9, 6]]))