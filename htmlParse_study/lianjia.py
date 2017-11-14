import requests
import time
from bs4 import BeautifulSoup
import pymysql

def download_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Refer': 'https://hz.lianjia.com/ershoufang/',
    }
    data = requests.get(url, headers=headers).content
    time.sleep(20)
    return data
def main():

    for pageNo in range(0, 58):
        if pageNo == 0:
            url = 'https://hz.lianjia.com/ershoufang/p6'
        else:
            url = 'https://hz.lianjia.com/ershoufang/pg'+str(pageNo)+'p6'
        print(url)
        html = download_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', class_='sellListContent')  # 房源列表
        for li in ul.find_all('li'):
            html = li.find('a', attrs={'class', 'img'}).get('href')
            imgUrl = li.find('img', attrs={'class', 'lj-lazy'}).get('data-original')
            title = li.find('div', attrs={'class', 'title'}).find('a').get_text()
            houseInfo = li.find('div', attrs={'class', 'houseInfo'}).get_text()
            buildTime = li.find('div', attrs={'class', 'positionInfo'}).get_text()
            address = li.find('div', attrs={'class', 'positionInfo'}).find('a').get_text()
            followInfo = li.find('div', attrs={'class', 'followInfo'}).get_text()
            if li.find('span', attrs={'class', 'subway'}):
                subway = li.find('span', attrs={'class', 'subway'}).get_text()
            else:
                subway = '无'
            if li.find('span', attrs={'class', 'taxfree'}):
                buyTime = li.find('span', attrs={'class', 'taxfree'}).get_text()
            else:
                buyTime = '无'
            totalPrice = li.find('div', attrs={'class', 'totalPrice'}).find('span').get_text()
            unitPrice = li.find('div', attrs={'class', 'unitPrice'}).find('span').get_text()
            sql = "INSERT INTO lianjiaershouhouse(html, imgUrl, title , houseInfo, buildTime, address, followInfo, suway, buyTime, totalPrice, unitPrice)" \
                  " VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                  % (html, imgUrl, title, houseInfo, buildTime, address, followInfo, subway, buyTime, totalPrice, unitPrice)

            execute_db(sql)
db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study', charset='utf8')
cursor = db.cursor()
def execute_db(sql):
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        print('error')
        db.rollback()
    # finally:
    #     db.close()

if __name__ == '__main__':
    main()