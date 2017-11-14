import requests
import time
from bs4 import BeautifulSoup
import pymysql
from openpyxl import Workbook

# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study')
cursor = db.cursor()
def execute_def(sql):
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        print('error')
        db.rollback()
    finally:
        db.close()

def insert_def(i, m, o, p):
    sql = "INSERT INTO top250(name, star_con, score , info) VALUES ('%s', '%s', '%s', '%s')" % (i, m, o, p)
    execute_def(sql)
def main():
    insert_def('a', 'b', 'c', 'd')


if __name__ == '__main__':
    main()
