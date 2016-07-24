## 2. Array comparisons ##

countries_canada = world_alcohol[:,2] == 'Canada'
years_1984 = world_alcohol[:,0] == '1984'

## 3. Selecting elements ##

country_is_algeria = (world_alcohol[:,2] == 'Algeria')
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with multiple conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing values ##

string_with_1986 = world_alcohol[:,0] == '1986'
world_alcohol[string_with_1986,0] = '2014'

replace = world_alcohol[:,3] == 'Wine'
world_alcohol[replace,3] = 'Grog'

## 6. Replacing empty strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = '0'

## 7. Converting data types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total alcohol consumption in a year ##

temp = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada') 
canada_1986 = (world_alcohol[temp])

replace = canada_1986[:,4] == ''
canada_1986[replace] = '0'
canada_alcohol = canada_1986[:,4]
canada_alcohol = canada_alcohol.astype(float)


total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating consumption for each country ##

totals = {}
t = world_alcohol[:,0] == '1989'
year = world_alcohol[t]
for country in countries:
    temp = year[:,2] == country
    country_consumption = year[temp]
    
    replace = country_consumption[:,4] == ''
    country_consumption[replace,4] = '0'
    
    f = country_consumption[:,4]
    f = f.astype(float)
    
    s = f.sum()
    
    totals[country] = s

print(totals)



## 11. Finding the country that drinks the most ##

highest_value = 0
highest_key = None

for key,value in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = key

print(highest_key)