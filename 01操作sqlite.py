#coding=utf-8

"""
1.导入sqlite3模块
2.创建连接sqlite3.connect()
3.创建游标对象
4.编写创建表的sql语句
5.执行sql
6.关闭游标和连接
"""
#导入模块
import sqlite3
#创建连接
con=sqlite3.connect("D:\sqlite3Demo\demo.db")
#创建游标对象
cur=con.cursor()
#编写删除的sql语句
sql="delete from t_person where pon=?"
#执行sql
try:
    cur.execute(sql,(1,))
    #提交事务
    con.commit()
    print("修改成功")
except Exception as e:
    print(e)
    print("修改失败")
    con.rollback()
finally:
    #关闭连接
    con.close()

