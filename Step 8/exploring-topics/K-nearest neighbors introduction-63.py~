## 1. A look at the data ##

import pandas
with open("nba_2013.csv", 'r') as csvfile:
    nba = pandas.read_csv(csvfile)

# The names of the columns in the data.
print(nba.columns.values)

## 3. Euclidean distance ##

selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

def calc_distance(row):
    return (sum((selected_player[distance_columns] - row[distance_columns]) ** (2))) ** (1/2)
    
lebron_distance = nba.apply(calc_distance, axis=1)
print(lebron_distance)

## 4. Normalizing columns ##

nba_numeric = nba[distance_columns]
nba_normalized = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()

## 5. Finding the nearest neighbor ##

from scipy.spatial import distance

# Fill in NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for lebron james.
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between lebron james and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
sort_distances = euclidean_distances.sort_values()
closest = sort_distances.iloc[1:2]
most_similar_to_lebron = nba.iloc[closest.index[0]]['player']
print(most_similar_to_lebron)

## 7. Using sklearn ##

# The columns that we will be making predictions with.
x_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf']
# The column that we want to predict.
y_column = ["pts"]

from sklearn.neighbors import KNeighborsRegressor
# Create the knn model.
knn = KNeighborsRegressor(n_neighbors=5)
# Fit the model on the training data.
knn.fit(train[x_columns], train[y_column])
# Make predictions on the test set using the fit model.
predictions = knn.predict(test[x_columns])

## 8. Computing error ##

actual = test[y_column]
mse = (((predictions - actual) ** 2).sum()) / len(predictions)
print(mse)
