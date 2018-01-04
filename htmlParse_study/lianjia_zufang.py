import pymysql
import requests
import time
from bs4 import BeautifulSoup

db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study', charset='utf8')
cursor = db.cursor()
# 创建数据库
def create_database():
    sql = """CREATE TABLE IF NOT EXISTS lianjiazufang(
             id INT NOT NULL AUTO_INCREMENT,
             detail_html CHAR(255),
             imgUrl CHAR(255) , 
             title CHAR(255), 
             region CHAR(255),
             room CHAR(255),
             size CHAR(255),
             orientation CHAR(255),
             variety CHAR(255),
             varietyUrl CHAR(255),
             floor CHAR(255),
             buildTime CHAR(255),
             subway CHAR(255),
             isKanfang CHAR(255),
             isJingZhuang CHAR(255),
             price CHAR(255),
             update_time CHAR(255),
             see_people CHAR(255),
             PRIMARY KEY(id))"""
    execute_def(sql)
def execute_def(sql):
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
def download_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Refer': 'https://hz.lianjia.com/zufang/',
    }
    data = requests.get(url, headers=headers).content
    time.sleep(20)
    return data

def main():
    for pageNo in range(0, 101):
        if pageNo == 0:
            url = 'https://hz.lianjia.com/zufang/'
        else:
            url = 'https://hz.lianjia.com/zufang/pg'+str(pageNo)

        print(url)
        html = download_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find('ul', class_='house-lst') #class是关键字  ,或写为soup.find('ul', {'class':'house-lst'})
        # find_all(tag,attributes,recursive,text,limit,keywords)
        # find(tag,attributes,recursive,text,limit,keywords)
        # tag:标签名或标签名列表 eg:  'h1' or {'h1','h2'}
        # attributes:属性和属性值对 eg: {'class','class1'} or {'class',{'class2',}}
        # recursive:递归参数（boolean,默认为true） true会去查找该标签的所有子标签，false只查找文档的一级标签
        # text:用标签的文本去匹配 eg: bs.find_all(text="text1")
        # limit: find相当于find_all limit 为1的情形(取前limit项)
        # keywords: 选择那些具有指定属性的标签  eg: bs.find_all(id="id1")
        for li in list.find_all('li'):
            detail_html = li.find('div', attrs={'class', 'pic-panel'}).find('a').get('href')
            imgUrl = li.find('img').get('data-img')
            title = li.find('h2').find('a').get('title')
            region = li.find('span', attrs={'class', 'region'}).get_text()
            room = li.find('span', attrs={'class', 'zone'}).get_text()
            size = li.find('span', attrs={'class', 'meters'}).get_text()
            orientation = li.find('div', attrs={'class', 'where'}).find_all('span')[4].get_text()
            variety = li.find('div', attrs={'class', 'con'}).get_text().split('/')[0]
            varietyUrl = li.find('div', attrs={'class', 'con'}).find('a').get('href')
            floor = li.find('div', attrs={'class', 'con'}).get_text().split('/')[1]
            buildTime = li.find('div', attrs={'class', 'con'}).get_text().split('/')[2]

            if li.find('span', attrs={'class', 'fang-subway-ex'}):
                subway = li.find('span', attrs={'class', 'fang-subway-ex'}).find('span').get_text()
            else:
                subway = '无'
            if li.find('span', attrs={'class', 'haskey-ex'}):
                isKanfang = li.find('span', attrs={'class', 'haskey-ex'}).find('span').get_text()
            else:
                isKanfang = '无'
            if li.find('span', attrs={'class', 'decoration-ex'}):
                isJingZhuang = li.find('span', attrs={'class', 'decoration-ex'}).find('span').get_text()
            else:
                isJingZhuang = '无'

            price = li.find('div', attrs={'class', 'price'}).find('span').get_text()
            update_time = li.find('div', attrs={'class', 'price-pre'}).get_text()
            see_people = li.find('div', attrs={'class', 'square'}).find('span').get_text()
            sql = "INSERT INTO lianjiazufang(detail_html, imgUrl, title , region, room, size, orientation, variety, varietyUrl, floor, buildTime, subway, isKanfang, isJingZhuang, price, update_time, see_people)" \
                      " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                      % (detail_html, imgUrl, title, region, room, size, orientation, variety, varietyUrl, floor, buildTime, subway, isKanfang, isJingZhuang, price, update_time, see_people)
            execute_def(sql)
            # print(detail_html, imgUrl, title, region, room, size, orientation, variety, varietyUrl, floor, buildTime, subway, isKanfang, isJingZhuang, price, update_time, see_people)

if __name__ == '__main__':
    main()
