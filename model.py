import pickle
import pandas as pd
import numpy as np
print("HI")

dataset = pd.read_csv('salary_prediction.csv')
X = dataset.iloc[:,:3]
y = dataset.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X,y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))
