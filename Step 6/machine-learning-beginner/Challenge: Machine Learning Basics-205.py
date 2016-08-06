## 2. Data cleaning ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)

df = cars.loc[cars['horsepower'] != '?']
df['horsepower'] =  df['horsepower'].astype(float)
filtered_cars = df
print(filtered_cars)
print(filtered_cars.dtypes)

## 3. Data Exploration ##

import matplotlib.pyplot as plt
%matplotlib inline

# good way to plot graphs instead of ax1 and ax2
filtered_cars.plot('horsepower', 'mpg', kind='scatter', c='red')
filtered_cars.plot('weight', 'mpg', kind='scatter', c='blue')
plt.show()

## 4. Fitting a model ##

import sklearn
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
# lr.fit(x, y)
lr.fit(filtered_cars[['horsepower']], filtered_cars[['mpg']])

## 5. Plotting the predictions ##

#predictions = lr.predict(filtered_cars['horsepower'])

plt.scatter(filtered_cars['horsepower'], predictions, color='red')
plt.scatter(filtered_cars['horsepower'], filtered_cars['mpg'], color='blue')
plt.show()

## 6. Error metrics ##

from sklearn.metrics import mean_squared_error

# mse(y_true, y_predicted)
mse = mean_squared_error(filtered_cars['mpg'], predictions)
rmse = mse**(1/2)

print(mse, rmse)