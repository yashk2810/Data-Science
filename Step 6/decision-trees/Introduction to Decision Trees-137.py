## 2. Our dataset ##

import pandas

# Set index_col to False to avoid pandas thinking that the first column is row indexes (it's age).
income = pandas.read_csv("income.csv", index_col=False)
print(income.head(5))

## 3. Converting categorical variables ##

# Convert a single column from text categories into numbers.
col = pandas.Categorical.from_array(income["workclass"])
income["workclass"] = col.codes
print(income["workclass"].head(5))

for n in ["education", "marital_status", "occupation", "relationship", "race", "sex", "native_country", "high_income"]:
    con = pandas.Categorical.from_array(income[n])
    income[n] = con.codes

print(income.head)

## 5. Performing a split ##

# Enter your code here.
private_incomes = income[income['workclass'] == 4]
print(private_incomes.shape)
public_incomes = income[income['workclass'] != 4]
print(public_incomes.shape)

## 8. Entropy ##

import math
# We'll do the same calculation we did above, but in Python.
# Passing 2 as the second parameter to math.log will take a base 2 log.
entropy = -(2/5 * math.log(2/5, 2) + 3/5 * math.log(3/5, 2))
print(entropy)

v_0 = income['high_income'].value_counts()[0]
v_1 = income['high_income'].value_counts()[1]
total = len(income)
prob_0 = v_0 / total
prob_1 = v_1 / total

income_entropy = -((prob_0 * math.log(prob_0, 2)) + (prob_1 * math.log(prob_1, 2)))
print(income_entropy)

## 9. Information gain ##

import numpy

def calc_entropy(column):
    """
    Calculate entropy given a pandas Series, list, or numpy array.
    """
    # Compute the counts of each unique value in the column.
    counts = numpy.bincount(column)
    # Divide by the total column length to get a probability.
    probabilities = counts / len(column)
    
    # Initialize the entropy to 0.
    entropy = 0
    # Loop through the probabilities, and add each one to the total entropy.
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    
    return -entropy

# Verify our function matches our answer from earlier.
entropy = calc_entropy([1,1,0,0,1])
print(entropy)

information_gain = entropy - ((.8 * calc_entropy([1,1,0,0])) + (.2 * calc_entropy([1])))
print(information_gain)

left_split = income[income['age'] <= income['age'].median()]
right_split = income[income['age'] > income['age'].median()]

lse = (len(left_split) / len(income['high_income'])) * calc_entropy(left_split['high_income'])
rse = (len(right_split) / len(income['high_income'])) * calc_entropy(right_split['high_income'])

age_information_gain = calc_entropy(income['high_income']) - (lse + rse)
print(age_information_gain)

## 10. Finding the best split ##

def calc_information_gain(data, split_name, target_name):
    """
    Calculate information gain given a dataset, column to split on, and target.
    """
    # Calculate original entropy.
    original_entropy = calc_entropy(data[target_name])
    
    # Find the median of the column we're splitting.
    column = data[split_name]
    median = column.median()
    
    # Make two subsets of the data based on the median.
    left_split = data[column <= median]
    right_split = data[column > median]
    
    # Loop through the splits, and calculate the subset entropy.
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / data.shape[0]) 
        to_subtract += prob * calc_entropy(subset[target_name])
    
    # Return information gain.
    return original_entropy - to_subtract

# Verify that our answer is the same as in the last screen.
print(calc_information_gain(income, "age", "high_income"))

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]
information_gains = []

for i in columns:
    information_gains.append(calc_information_gain(income, i, 'high_income'))
print(information_gains)

max_gain = information_gains.index(max(information_gains))
highest_gain = columns[max_gain]
print(highest_gain)
