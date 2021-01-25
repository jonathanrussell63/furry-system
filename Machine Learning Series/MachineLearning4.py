#including pipelines to process the data
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split


data = pd.read_csv('melb_data.csv')

y = data.Price
X = data.drop(['Price'], axis=1)

X_train_full, X_valid_full, y_train, y_valid = train_test_split(X,y,train_size = .8, test_size=.2,random_state=0)


categorical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique()<10 and X_train_full[cname].dtype=='object']

numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

my_cols = categorical_cols + numerical_cols

X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()

# imputes missing values in numerical data, and imputes missing values and applies a one-hot encoding to categorical data

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

#Step 1: Define Preprocessing Steps

#preprocessing for numerical data
numerical_transformer = SimpleImputer(strategy = 'constant')

#preprocessing for categorical data
categorical_transformer = Pipeline(steps = [
('imputer', SimpleImputer(strategy = 'most_frequent')),
('onehot', OneHotEncoder(handle_unknown = 'ignore'))
	])

#bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
	transformers = [
('num', numerical_transformer, numerical_cols),
('cat', categorical_transformer, categorical_cols)
	])

#Step 2: Define the Model
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(n_estimators = 100, random_state=0)

#Step 3: Create and Evaluate the Pipeline
from sklearn.metrics import mean_absolute_error

my_pipeline = Pipeline(steps = [('preprocessor', preprocessor),
	('model', model)
	])

my_pipeline.fit(X_train,y_train)

preds = my_pipeline.predict(X_valid)

score = mean_absolute_error(y_valid, preds)

print('MAE:', score)