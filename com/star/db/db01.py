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