import requests
import re
import time
import codecs
from openpyxl import Workbook
from bs4 import BeautifulSoup
import pymysql
wb = Workbook()
dest_filename = '电影.xlsx'
ws1 = wb.active
ws1.title = "电影top250"


# 连接数据库
db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study')
# 使用 cursor() 方法创建一个游标对象 cursor
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

DOWNLOAD_URL = 'http://movie.douban.com/top250/'

def download_page(url):
    """获取url地址页面内容"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    time.sleep(20)
    return data

def get_list(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    ol = soup.find('ol', class_='grid_view')
    name = []  # 名字
    star_con = []  # 评价人数
    score = []  # 评分
    info_list = []  # 短评
    for i in ol.find_all('li'):
        detail = i.find('div', attrs={'class': 'hd'})
        movie_name = detail.find(
            'span', attrs={'class': 'title'}).get_text()  # 电影名字
        level_star = i.find(
            'span', attrs={'class': 'rating_num'}).get_text()  # 评分
        star = i.find('div', attrs={'class': 'star'})
        star_num = star.find(text=re.compile('评价'))  # 评价

        info = i.find('span', attrs={'class': 'inq'})  # 短评
        if info:  # 判断是否有短评
            info_list.append(info.get_text())
        else:
            info_list.append('无')
        score.append(level_star)

        name.append(movie_name)
        star_con.append(star_num)
    page = soup.find('span', attrs={'class': 'next'}).find('a')  # 获取下一页
    if page:
        return name, star_con, score, info_list, DOWNLOAD_URL + page['href']
    return name, star_con, score, info_list, None


def main():
    url = DOWNLOAD_URL
    name = []
    star_con = []
    score = []
    info = []
    while url:
        doc = download_page(url)
        movie, star, level_num, info_list, url = get_list(doc)
        print(movie, star, level_num, info_list, url)
        name = name + movie
        star_con = star_con + star
        score = score + level_num
        info = info + info_list
    for (i, m, o, p) in zip(name, star_con, score, info):
        print(i, m, o, p)

        sql = "INSERT INTO top250(name,star_con, score, info) VALUES ('%s', '%s', '%s', '%s')" % (i, m, o, p)
        execute_def(sql)


if __name__ == '__main__':
    main()
