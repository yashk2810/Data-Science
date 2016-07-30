## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
q = "create table notes(id integer primary key, body text, title text)"
cur.execute(q)
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
q = "create table notes(id integer primary key, body text, title text)"
cur.execute(q)
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute('create table facts(id integer primary key, country text, value integer)')
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect('dbname=dq user=dq')
cur = conn.cursor()
conn.autocommit=True
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute('select * from notes;')
print(cur.fetchall())

conn.close()

## 8. Creating a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit=True
cur = conn.cursor()
cur.execute('create database income owner dq')
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect('dbname=dq user=dq')
conn.autocommit=True
cur = conn.cursor()
cur.execute('drop database income;')
conn.close()