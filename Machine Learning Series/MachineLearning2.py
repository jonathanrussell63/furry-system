import pandas as pd
import sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

#working with columns with empty values
from sklearn.impute import SimpleImputer

file_path = 'melb_data.csv'
data = pd.read_csv(file_path)
#removes entries with missing y value
data.dropna(axis=0, subset=['Price'], inplace=True) 

y = data.Price
features = ['Rooms', 'Distance', 'Postcode', 'Bedrooms', 'Bathroom', 'Car', 'Landsize', 'YearBuilt','BuildingArea']
X = data[features]

train_X, val_X, train_y, val_y = train_test_split(X,y,random_state=0, test_size = .14)

def score_dataset(train_X, val_X, train_y, val_y):
	model = RandomForestRegressor(n_estimators = 100, random_state=0,min_samples_leaf = 10)
	model.fit(train_X, train_y)
	prediction = model.predict(val_X)
	return mean_absolute_error(val_y, prediction)

#drop columns with missing values (not ideal since you can lose lots of good data)

#cols_missing = [col for col in train_X.columns
#				if train_X[col].isnull().any()]

#print(cols_missing)
#reduced_train_X = train_X.drop(cols_missing, axis=1)
#reduced_val_X = val_X.drop(cols_missing, axis=1)

#print('MAE from Approach 1 (drop columns with missing values): ')
#print(score_dataset(reduced_train_X, reduced_val_X, train_y, val_y))



#imputation = setting empty values to a certain value, can extend by adding another column saying 'previously empty: True/False'

#my_imputer = SimpleImputer()
#imputed_train_X = pd.DataFrame(my_imputer.fit_transform(train_X))
#imputed_val_X = pd.DataFrame(my_imputer.transform(val_X))
#imputation removes column names (normally, I don't think so here), so you have to replace them:
#imputed_train_X.columns = features
#imputed_val_X.columns =features

#print('MAE from Approach 2 (Imputation): ')
#print(score_dataset(imputed_train_X, imputed_val_X, train_y, val_y))

#imputation extension
#copying the data so we have original before imputation

X_train_plus = train_X.copy()
X_valid_plus = val_X.copy()

cols_missing = [col for col in train_X.columns
				if train_X[col].isnull().any()]

for col in cols_missing:
	X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
	X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

my_imputer = SimpleImputer(strategy = 'mean' ) #strategy can be constant, median, mean, or most_frequent. Use fill_value parameter for constant
imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

print('MAE from Approach 3 (Extension to Imputation):')
print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, train_y, val_y))

#rows x columns
#print(train_X.shape) 
#tells how many values dropped from each column
#missing_val_count_by_column = (train_X.isnull().sum())
#print(missing_val_count_by_column[missing_val_count_by_column > 0])