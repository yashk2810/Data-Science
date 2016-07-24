## 2. Lists of lists ##

import csv
f = open('world_alcohol.csv','r')
reader = csv.reader(f)
world_alcohol = list(reader)

years=[]
for i in world_alcohol:
    years.append(i[0])
years = years[1:]

total=0
for i in years:
    total+=float(i)

avg_year = total / len(years)


## 4. Using NumPy ##

import numpy as np
world_alcohol = np.genfromtxt('world_alcohol.csv', delimiter=',')

## 5. Creating arrays ##

import numpy as np
vector = np.array([10,20,30])

matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

## 6. Array shape ##

vector = numpy.array([10, 20, 30])
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
vector_shape = vector.shape
matrix_shape = matrix.shape

## 7. Data types ##

world_alcohol_dtype = world_alcohol.dtype

## 9. Reading in the data properly ##

import numpy as np
world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=True)

print(world_alcohol)

## 10. Indexing arrays ##

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

## 11. Slicing arrays ##

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

## 12. Slicing one dimension ##

first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10,:]

## 13. Slicing arrays ##

first_twenty_regions = world_alcohol[0:20,1:3]