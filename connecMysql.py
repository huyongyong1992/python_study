import pymysql

# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 插入数据库
def insert_database():
    # 插入之前查询此人是否存在数据库中
    try:
        select_sql = "SELECT * FROM python_user WHERE FIRST_NAME = '%s' " % ('Mbc')
        cursor.execute(select_sql)
        rs = cursor.fetchall()
        if rs:
            print('this person exsited')
        else:
            print('No this person')
            sql = """INSERT INTO python_user(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mbc', 'Young', 26, 'F', 5000)"""
            execute_def(sql)
    except:
        print('error')

# 创建数据库
def create_database():
    sql = """CREATE TABLE IF NOT EXISTS TEST(
             id INT NOT NULL AUTO_INCREMENT,
             NAME CHAR(20),
             AGE INT , 
             ADDRESS CHAR(20), 
             COMPONY CHAR(20),
             PRIMARY KEY(id))"""
    execute_def(sql)
# 删除数据库中的数据
def delete_database():
    sql = "DELETE FROM python_user WHERE AGE > '%d'" % (23)
    execute_def(sql)

# 更改数据库中的数据
def update_database():
    sql = "UPDATE python_user SET AGE = AGE+1 WHERE SEX = '%s'" % ('M')
    execute_def(sql)

# 查询数据库中的数据
def select_database():
    sql = "SELECT * FROM python_user WHERE AGE > '%d' AND SEX = '%s'" % (21, 'M')
    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            print(row)
    except:
        print("Error: unable to fetch data")


def execute_def(sql):
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        print('error')
        db.rollback()
if __name__ == '__main__':
    insert_database()