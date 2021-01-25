# simple practice on my GettingFit file
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('GetFit.csv')

features = ['Ran', 'Walked', 'Pushups', 'Situps', 'Pullups', 'Dips','Anti-Push','Abs', 'Bench']
X = data[features]
y = data.Eaten
X.fillna(value = 0, inplace=True)

X_train, X_valid, y_train, y_valid = train_test_split(X,y,train_size = .8, random_state = 2)

from xgboost import XGBRegressor
model = XGBRegressor(n_estimators = 1000, learning_rate = .2, n_jobs=6)



model.fit(X_train, y_train, early_stopping_rounds = 8, eval_set = [(X_valid, y_valid)], verbose = False)


from sklearn.model_selection import cross_val_score

scores =  -1*cross_val_score(model,X,y, cv=5, scoring = 'neg_mean_absolute_error')

print('Score: \n', scores.mean())

