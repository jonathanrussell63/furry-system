import pandas as pd
import sklearn
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

def score_dataset(X_train, X_valid, y_train, y_valid):
	model = RandomForestRegressor(n_estimators=100, random_state=0, min_samples_leaf = 5)
	model.fit(X_train, y_train)
	preds = model.predict(X_valid)
	return mean_absolute_error(y_valid, preds)
#Now we can begin to work on categorical data
#deleting the categorical data. Only do so if it is unimportant.
#label encoding = assigning a number to the categories. Only works if there is a natural ordering (ordinal variables):
#never<sometimes<most of the time<always
#one-hot encoding. creates new columns with a 1/0 in the columns depending on the presence/absence of each possible value. 
#similar to label encoding but doesn't assume a natural order (nominal variables). Best for small number of possibilities

data =pd.read_csv('melb_data.csv')
# Separate target from predictors
y = data.Price
X = data.drop(['Price'], axis=1)

# Divide data into training and validation subsets
X_train_full, X_valid_full, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                                random_state=1)

# Drop columns with missing values (simplest approach)
cols_with_missing = [col for col in X_train_full.columns if X_train_full[col].isnull().any()] 
X_train_full.drop(cols_with_missing, axis=1, inplace=True)
X_valid_full.drop(cols_with_missing, axis=1, inplace=True)

# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality_cols = [cname for cname in X_train_full.columns if X_train_full[cname].nunique() < 10 and 
                        X_train_full[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_full.columns if X_train_full[cname].dtype in ['int64', 'float64']]

# Keep selected columns only
my_cols = low_cardinality_cols + numerical_cols
X_train = X_train_full[my_cols].copy()
X_valid = X_valid_full[my_cols].copy()


#list of categorical variables
s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

#
#
#
#
#
#
#

#label encoding
label_X_train = X_train.copy()
label_X_valid = X_valid.copy()

label_encoder = LabelEncoder()

for col in object_cols:
	label_X_train[col] = label_encoder.fit_transform(X_train[col])
	label_X_valid[col] = label_encoder.fit_transform(X_valid[col])





#print("MAE from Approach 2 (Label Encoding):") 
#print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))





drop_X_train = X_train.select_dtypes(exclude = ['object'])
drop_X_valid = X_valid.select_dtypes(exclude = ['object'])

#print('MAE1: ')
#print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))

#
#
#
#
#
#
#


#one hot encoder

from sklearn.preprocessing import OneHotEncoder

# All categorical columns
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely label encoded
good_label_cols = [col for col in object_cols if 
                   set(X_train[col]) == set(X_valid[col])]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))

# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in good_label_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(good_label_cols)-set(low_cardinality_cols))



OH_encoder = OneHotEncoder(handle_unknown ='ignore', sparse=False)
OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

#onehot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index


#remove categorical colums:
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)


#add onehot encoded columns to numerical features, this lets it do the ML all together
OH_X_train = pd.concat([num_X_train, OH_cols_train],axis=1) 
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

print("MAE from Approach 3 (One-Hot Encoding):") 
print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))