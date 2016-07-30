## 3. Connect to the database ##

import sqlite3
conn = sqlite3.connect('jobs.db')

## 6. Running a query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

q = "select Major from recent_grads;"
cursor.execute(q)
majors = cursor.fetchall()
print(majors[0:3])

## 8. Fetching a specific number of results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select Major,Major_category from recent_grads;"
cursor.execute(query)
five_results = cursor.fetchmany(5)

## 9. Closing the connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

import sqlite3

conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()
query = 'select Major from recent_grads order by Major DESC;'
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()
conn.close()