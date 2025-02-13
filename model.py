import numpy as np
import pandas as pd
import pickle

dataset = pd.read_csv(r'D:\swarna\DEPLOY_ML\salary_prediction.csv')

X = dataset.iloc[:,:3]

y = dataset.iloc[:,-1]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2,9,6]]))
                        
