import pandas as pd
import sklearn 
from sklearn.model_selection import train_test_split

#predicting league victors based on first 10 minutes of game
#incorporating validation data

file_path = 'high_diamond_ranked_10min.csv'
data = pd.read_csv(file_path)

y = data.blueWins
#little bit of preprocessing data by adding new columns
data['wardDiff'] = data['redWardsPlaced']-data['blueWardsPlaced']
data['killDiff'] = data['redKills']-data['blueKills']
data['buffDiff'] = data['redEliteMonsters']-data['blueEliteMonsters']
data['minionDiff'] =data['redTotalMinionsKilled']-data['blueTotalMinionsKilled']
features = ['redGoldDiff', 'redExperienceDiff', 'redTotalJungleMinionsKilled','wardDiff','killDiff','buffDiff','minionDiff','blueFirstBlood']

X=data[features]





X_train_full, X_valid_full, y_train, y_valid = train_test_split(X,y,train_size = .8, test_size=.2,random_state=0)


#scaling the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

sc.fit(X_train_full)
X_train_full = sc.transform(X_train_full)
X_valid_full = sc.transform(X_valid_full)

#Step 1
from sklearn.linear_model import LogisticRegression
from xgboost import XGBRegressor

model = LogisticRegression(C=.05, warm_start= True,penalty='l2', fit_intercept=False, max_iter = 10000)

model.fit(X_train_full, y_train)
#Step 2 Evaluate Perfomance
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score




preds = model.predict(X_valid_full)

from sklearn.model_selection import cross_val_score
scores =  cross_val_score(model,X,y, cv=5, scoring = 'accuracy')


print(scores.mean())

