import sqlite3

conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query = "select * from facts order by population asc limit 10;"

cursor.execute(query)

print(cursor.fetchall())