import pandas as pd
import sklearn 
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing,svm
#after like an hour I get how DecisionTreeRegressor works. You give it information, and it tries to find the closest match. 
#So if you give it all the data it can be correct 100% of the time since it just compares.

#I spiffed it up with beign able to do Calls/Puts (rather important) based on labeling encoding

file_path = 'SPY_Trades.csv'
data = pd.read_csv(file_path)
data.fillna(-99999, inplace=True)
y = data.Option_trade_price
feature_names = ['Price_strike','Call_Put', 'AbsIV','AbsDelta','AbsGamma','AbsTheta','Underlying_ask_price','AbsVega','AbsRho']
X = data[feature_names]



X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.75, test_size=0.25,
                                                                random_state=1000)


low_cardinality_cols = [cname for cname in X if X[cname].nunique() < 3 and 
                        X_train_full[cname].dtype == "object"]
numerical_cols = [cname for cname in X.columns if X[cname].dtype in ['int64', 'float64']]

my_cols = low_cardinality_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

label_X_train = X_train.copy()
label_X_valid = X_valid.copy()

label_encoder = LabelEncoder()

for col in object_cols:
	label_X_train[col] = label_encoder.fit_transform(X_train[col])
	label_X_valid[col] = label_encoder.fit_transform(X_valid[col])
#this allows you to only train with a certain percent of your data. You save the rest to compare the accuracy to.

model = RandomForestRegressor(n_estimators = 100,min_samples_leaf = 15,random_state=1)

model.fit(label_X_train,y_train)

predictions = model.predict(label_X_valid)

predictions=np.round(predictions, decimals =2)




print(round(mean_absolute_error(predictions[100:110], y_valid[100:110]),2))

print(predictions[100:110])
print(y_valid[100:110])