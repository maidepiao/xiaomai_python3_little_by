import pymysql
import random

conn = pymysql.connect(host='192.168.244.100',
                       user='test',
                       password='123456',
                       db='star',
                       cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO `user` (`id`, `name`) VALUES (%s, %s)"
        cursor.execute(sql, (random.randint(10,100), '小麦快跑'))
        conn.commit()
except pymysql.err.DataError:
    conn.rollback()
finally:
    conn.close()

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

import sqlite3
conn = sqlite3.connect('star.db')
cursor = conn.cursor()
insert_sql =  'insert into user(id,name) values (%s,%s)'
cursor.execute(insert_sql,(1,'小麦'))