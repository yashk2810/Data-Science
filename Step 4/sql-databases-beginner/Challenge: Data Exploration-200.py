## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
pop_avg = conn.execute('select avg(population) from facts;').fetchall()[0][0]
pop_growth_avg = conn.execute('select avg(population_growth) from facts;').fetchall()[0][0]
birth_rate_avg = conn.execute('select avg(birth_rate) from facts;').fetchall()[0][0]
death_rate_avg = conn.execute('select avg(death_rate) from facts;').fetchall()[0][0]
