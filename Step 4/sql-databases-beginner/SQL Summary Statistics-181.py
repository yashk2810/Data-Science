## 1. Counting in Python ##

import sqlite3
conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query = 'select * from facts;'
cursor.execute(query)
facts = cursor.fetchall()
print(facts)
facts_count = len(facts)

## 2. Counting in SQL ##

conn = sqlite3.connect("factbook.db")
c = conn.cursor()
query = "select count(birth_rate) from facts;"
c.execute(query)
birth_rate_count = c.fetchall()[0][0]
print(birth_rate_count)

## 3. Min and max in SQL ##

conn = sqlite3.connect("factbook.db")
min_population_growth = conn.execute('select min(population_growth) from facts;').fetchall()[0][0]
print(min_population_growth)

max_death_rate = conn.execute('select max(death_rate) from facts;').fetchall()[0][0]
print(max_death_rate)

## 4. Sum and average in SQL ##

conn = sqlite3.connect("factbook.db")
total_land_area = conn.execute('select sum(area_land) from facts;').fetchall()[0][0]
print(total_land_area)

avg_water_area = conn.execute('select avg(area_water) from facts;').fetchall()[0][0]
print(avg_water_area)

## 5. Multiple aggregation functions ##

conn = sqlite3.connect("factbook.db")
facts_stats = conn.execute('select avg(population), sum(population), max(birth_rate) from facts;').fetchall()

## 9. Arithmetic in SQL ##

conn = sqlite3.connect("factbook.db")
population_growth_millions = conn.execute('select population_growth / 1000000.0 from facts;').fetchall()

## 10. Arithmetic between columns ##

conn = sqlite3.connect("factbook.db")
next_year_population = conn.execute('select (population * population_growth) + population from facts;').fetchall()