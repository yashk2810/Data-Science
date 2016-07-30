import sqlite3

conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query_land = "select sum(area_land) from facts;"

query_water = 'select sum(area_water) from facts;'

query_ratio = 'select sum(area_land)/sum(area_water) from facts;'

cursor.execute(query_ratio)
print(cursor.fetchall())

