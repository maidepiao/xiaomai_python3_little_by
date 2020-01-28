import sqlite3
import random
conn = sqlite3.connect('star.db')
cursor = conn.cursor()
insert_sql = 'insert into user(id,name) values(%d,"%s")'%(random.randint(1,100),'小麦')
print(insert_sql)
#insert_sql =  'insert into user(id,name) values (%s,%s)'
cursor.execute(insert_sql)
query_sql = 'select * from user'
cursor.execute(query_sql)
print(cursor.fetchall())
update_sql = 'update user set name = "%s" where name="小麦"'%('大麦',)
cursor.execute(update_sql)
cursor.execute(query_sql)
print(cursor.fetchall())
many_sql = "insert into user(id,name) values(?,?) "
data = [(1,'python'),(2,'pycharm'),(3,'pygame')]
cursor.executemany(many_sql,data)
cursor.execute(query_sql)
print(cursor.fetchall())
cursor.close()
conn.close()