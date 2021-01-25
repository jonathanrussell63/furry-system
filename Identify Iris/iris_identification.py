import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

data = pd.read_csv('irisdata.csv')

X = data.drop(['type'], axis=1)
y = data.type



#encoding iris categories to pick from
label_encoder = LabelEncoder()
y=label_encoder.fit_transform(y)

X_train, X_valid, y_train, y_valid = train_test_split(X,y, train_size = .8, test_size = .2, random_state =2)


from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps = [
('preprocessor', SimpleImputer()),
('model', LogisticRegression(max_iter=10000))
	]) 

from sklearn.model_selection import cross_val_score
scores =  cross_val_score(my_pipeline,X.round(),y, cv=5, scoring = 'accuracy')


print(scores.mean())

