## 2. Holdout validation ##

import numpy as np
admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)

random_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[random_index]
train = shuffled_admissions[:515]
test = shuffled_admissions[515:]
print(shuffled_admissions.head())

## 3. Accuracy ##

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]

lm = LogisticRegression()
t = lm.fit(train[['gpa']], train['actual_label'])
test['predicted_label'] = lm.predict(test[['gpa']])

matches = test['actual_label'] == test['predicted_label']
accuracy = len(test[matches]) / len(test)
print(accuracy)

## 4. Sensitivity and specificity ##

model = LogisticRegression()
model.fit(train[["gpa"]], train["actual_label"])
labels = model.predict(test[["gpa"]])
test["predicted_label"] = labels
matches = test["predicted_label"] == test["actual_label"]
correct_predictions = test[matches]
accuracy = len(correct_predictions) / len(test)

tp = test[(test['actual_label'] == 1) & (test['predicted_label'] == 1)]
fn = test[(test['actual_label'] == 1) & (test['predicted_label'] == 0)]
sensitivity = len(tp) / (len(tp) + len(fn))
print(sensitivity)

tn = test[(test['actual_label'] == 0) & (test['predicted_label'] == 0)]
fp = test[(test['actual_label'] == 0) & (test['predicted_label'] == 1)]
specificity = len(tn) / (len(tn) + len(fp))
print(specificity)

## 6. ROC curve ##

import matplotlib.pyplot as plt
%matplotlib inline
from sklearn import metrics

probabilities = model.predict_proba(test[['gpa']])
fpr, tpr, thresholds = metrics.roc_curve(test['actual_label'], probabilities[:,1])
print(fpr, tpr, thresholds)
plt.plot(fpr, tpr)
plt.show()

## 7. Area under the curve ##

# Note the different import style!
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(test['actual_label'] ,probabilities[:,1])
print(auc_score)