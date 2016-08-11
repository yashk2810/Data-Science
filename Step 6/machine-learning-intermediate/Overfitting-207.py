## 3. Bias-variance tradeoff ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def train_and_test(cols):
    lr = LinearRegression()
    x = cols
    y = filtered_cars['mpg']
    lr.fit(x, y)
    predictions = lr.predict(x)
    
    mse = mean_squared_error(y, predictions)
    variance = np.var(predictions)
    
    return(mse, variance)

cyl_mse, cyl_var = train_and_test(filtered_cars[['cylinders']])
weight_mse, weight_var = train_and_test(filtered_cars[['weight']])

print(cyl_mse, cyl_var)
print(weight_mse, weight_var)

## 4. Multivariate models ##

# Our implementation for train_and_test, takes in a list of strings.
def train_and_test(cols):
    # Split into features & target.
    features = filtered_cars[cols]
    target = filtered_cars["mpg"]
    # Fit model.
    lr = LinearRegression()
    lr.fit(features, target)
    # Make predictions on training set.
    predictions = lr.predict(features)
    # Compute MSE and Variance.
    mse = mean_squared_error(filtered_cars["mpg"], predictions)
    variance = np.var(predictions)
    return(mse, variance)

one_mse, one_var = train_and_test(["cylinders"])
print(one_mse, one_var)

two_mse, two_var = train_and_test(["cylinders", "displacement"])
print(two_mse, two_var)

three_mse, three_var = train_and_test(["cylinders", "displacement", "horsepower"])
print(three_mse, three_var)

four_mse, four_var = train_and_test(["cylinders", "displacement", "horsepower", 'weight'])
print(four_mse, four_var)

five_mse, five_var = train_and_test(["cylinders", "displacement", "horsepower", 'weight', 'acceleration'])
print(five_mse, five_var)

six_mse, six_var = train_and_test(["cylinders", "displacement", "horsepower", 'weight', 'acceleration', 'model year'])
print(six_mse, six_var)

seven_mse, seven_var = train_and_test(["cylinders", "displacement", "horsepower", 'weight', 'acceleration', 'model year', 'origin'])
print(seven_mse, seven_var)

## 5. Cross validation ##

from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import cross_val_score
import numpy as np

def train_and_cross_val(cols):
    lr = LinearRegression()
    
    mean_se = []
    vari = []
    
    kf = KFold(len(filtered_cars), 10, shuffle=True, random_state=3)
    
    for train_index, test_index in kf:
        train_x = filtered_cars.iloc[train_index][cols]
        test_x = filtered_cars.iloc[test_index][cols]
        
        train_y = filtered_cars.iloc[train_index]['mpg']
        test_y = filtered_cars.iloc[test_index]['mpg']
        
        lr.fit(train_x, train_y)
        predictions = lr.predict(test_x)
        
        mse = mean_squared_error(test_y, predictions)
        variance = np.var(predictions)
        
        mean_se.append(mse)
        vari.append(variance)
    
    avg_mse = np.mean(mean_se)
    avg_variance = np.mean(vari)
    
    return(avg_mse, avg_variance)
    
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
print(two_mse, two_var)

three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
print(three_mse, three_var)

four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", 'weight'])
print(four_mse, four_var)

five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", 'weight', 'acceleration'])
print(five_mse, five_var)

six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", 'weight', 'acceleration', 'model year'])
print(six_mse, six_var)

seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", 'weight', 'acceleration', 'model year', 'origin'])
print(seven_mse, seven_var)

## 6. Plotting cross-validation error vs. cross-validation variance ##

# We've hidden the `train_and_cross_val` function to save space but you can still call the function!
import matplotlib.pyplot as plt 
%matplotlib inline
        
two_mse, two_var = train_and_cross_val(["cylinders", "displacement"])
three_mse, three_var = train_and_cross_val(["cylinders", "displacement", "horsepower"])
four_mse, four_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight"])
five_mse, five_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration"])
six_mse, six_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration", "model year"])
seven_mse, seven_var = train_and_cross_val(["cylinders", "displacement", "horsepower", "weight", "acceleration","model year", "origin"])

plt.scatter([2,3,4,5,6,7], [two_mse, three_mse, four_mse, five_mse, six_mse, seven_mse], c='red')
plt.scatter([2,3,4,5,6,7], [two_var, three_var, four_var, five_var, six_var, seven_var], c='blue')
plt.show()