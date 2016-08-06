## 2. Introduction to the data ##

import pandas as pd

columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
cars = pd.read_table('auto-mpg.data', delim_whitespace=True, names=columns)

print(cars)

## 3. Exploratory data analysis ##

import matplotlib.pyplot as plt
%matplotlib inline

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.scatter(cars['weight'], cars['mpg'])
ax2.scatter(cars['acceleration'], cars['mpg'])
plt.show()

## 5. Scikit-learn ##

# Single NumPy array (398 elements).
print(cars["weight"].values)
# NumPy matrix (398 rows by 1 column).
print(cars[["weight"]].values)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(cars[['weight']], cars[['mpg']])

## 6. Making predictions ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars[["mpg"]])

predictions = lr.predict(cars[['weight']])
print(predictions[:5])
print(cars['mpg'].values[:5])

## 7. Plotting the model ##

plt.scatter(cars['weight'], cars['mpg'], color='red')
plt.scatter(cars['weight'], predictions, color='blue')
plt.show()

## 8. Error metrics ##

lr = LinearRegression()#fit_intercept=True)
lr.fit(cars[["weight"]], cars[["mpg"]])
predictions = lr.predict(cars[["weight"]])

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(cars['mpg'], predictions)
print(mse)

## 9. Root mean squared error ##

mse = mean_squared_error(cars["mpg"], predictions)
rmse = mse**(1/2)
print(rmse)