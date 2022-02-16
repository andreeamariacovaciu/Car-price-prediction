# Importing the libraries

import pandas as pd
import pickle


df = pd.read_csv('cars.csv')

X = df.drop(['current price','v.id'], axis=1)
y = df['current price']


#Since we have a very small dataset, we will train our model with all availabe data.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

#Fitting model with trainig data
lr.fit(X, y)

#Finding the most important 6 features
coef=lr.coef_
coefser=pd.Series(coef)
important_features=coefser.abs().nlargest(6)
df_important_features=X.iloc[:,[a for a in important_features.index]]
important_features_name=df_important_features.columns

lr1=LinearRegression()
lr1.fit(df_important_features,y)

# Saving model to disk
pickle.dump(lr1, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
