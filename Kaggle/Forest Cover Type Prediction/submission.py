import pandas as pd
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
# print(train.head())

features = list(train.columns)
features.remove('Cover_Type')
features.remove('Id')

alg = RandomForestClassifier(random_state=1, n_estimators=250)

kf = cross_validation.KFold(train.shape[0], n_folds=3, random_state=1)
scores = cross_validation.cross_val_score(alg, train[features], train['Cover_Type'], cv=kf)
print(scores.mean())

# alg.fit(train[features], train['Cover_Type'])
# predictions = alg.predict(test[features])

# predictions = predictions.astype(int)
# sub = pd.DataFrame({'Id': test['Id'], 'Cover_Type': predictions})
# sub.to_csv('kaggle.csv', index=False)