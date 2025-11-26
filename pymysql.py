# -*- coding: utf-8 -*-
import pymysql
    #创建与数据库的连接
db=pymysql.connect(host="localhost",
    user="root1",      # MySQL 用户名
    password="root1",  # MySQL 密码
    database="python_db")
    #创建游标对象cursor
cursor=db.cursor()
    #使用execute()方法执行sql,如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS student")
    #创建表的sql
sql="""
    CREATE TABLE t_student(
        sno int primary key AUTO_INCREMENT,
        sname varchar(30) not null,
        age int(2),
        score FLOAT(3,1)
)
"""
    #执行创建表的sql
try:
     #执行创建表的sql
    cursor.execute(sql)
    print("创建表成功")
except Exception as e:
    print(e)
    print("创建表失败")
finally:
    #关闭连接
    db.close()