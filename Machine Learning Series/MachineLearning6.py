#Gradient Boosting
# pretty powerful
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('melb_data.csv')

cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']

X = data[cols_to_use]
y = data.Price

X_train, X_valid, y_train, y_valid = train_test_split(X,y)

from xgboost import XGBRegressor

#n_estimators = the number of models to include typically from 100-1000, too low causes underfitting, too high causes overfitting
#learning_rate = .1 normally, setting lower makes later models matter less and less
#n_jobs should be set to number of cores on computer to make fitting take less time to run
my_model = XGBRegressor(n_estimators = 1000, learning_rate = .05, n_jobs=6)

# early_stopping_rounds stops adding new models after they get worse n times in a row
my_model.fit(X_train, y_train, early_stopping_rounds =7, eval_set =[(X_valid, y_valid)], verbose=False)

from sklearn.metrics import mean_absolute_error

predictions = my_model.predict(X_valid)

print('MAE:', mean_absolute_error(predictions,y_valid))
