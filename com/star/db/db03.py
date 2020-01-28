import sqlite3
conn = sqlite3.connect('star.db')
cursor = conn.cursor()
insert_sql =  'insert into user(id,name) values (%s,%s)'
cursor.execute(insert_sql,(1,'小麦'))
