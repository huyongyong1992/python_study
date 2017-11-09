#coding=utf-8
import json
import time
import requests
# import xlwt
import pymysql

def get_movie_info():
    # 循环100页，每一页爬取职位列表信息
    movies = []
    for pageNo in range(0, 15):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/explore',
            'Cookie': 'bid=g628ydwcuu8; gr_user_id=fe4f95e8-b073-4a47-acd6-4e956c42e8f7; ll="118172"; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1510125939%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=4A6BE3CFF0916D24B2633D36CF28B58A|32109afda2a6c1eb9727702aaba8f2e4; _pk_id.100001.4cf6=862f472cfacdc383.1510125939.1.1510126165.1510125939.; _pk_ses.100001.4cf6=*; __utma=30149280.1219586927.1494215547.1510021111.1510125931.6; __utmb=30149280.1.10.1510125931; __utmc=30149280; __utmz=30149280.1507690615.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.2069988832.1510125939.1510125939.1510125939.1; __utmb=223695111.0.10.1510125939; __utmc=223695111; __utmz=223695111.1510125939.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
        }
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+str(pageNo*20)

        # 通过get获取详情页信息
        result = requests.get(url, headers=headers).json()
        movies = movies+(result['subjects'])
        time.sleep(2)
    # #把爬取到的信息写入json文件
    line = json.dumps(movies)
    db = pymysql.connect(host='127.0.0.1', port=3306, user='young', password='123456', database='python_study', charset='utf8')
    cursor = db.cursor()
    for list in movies:
        # SQL 插入语句
        rate = list['rate']
        title = list['title']
        url = list['url']
        id = list['id']
        is_new = str(list['is_new'])
        # print("INSERT INTO douban(RATE,TITLE, IMG_URL, M_ID, IS_NEW) VALUES ('%s', '%s', '%s', '%s', '%s' )" % (rate, title, url, id, is_new))
        sql = "INSERT INTO douban(RATE,TITLE, IMG_URL, M_ID, IS_NEW) VALUES ('%s', '%s', '%s', '%s', '%s' )" % (rate, title, url, id, is_new)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            print('error')
            db.rollback()
        # db.close()
    # with open('movie.json', 'ab+') as fp:
    #     fp.write(line.encode('utf-8'))

if __name__ == '__main__':
    get_movie_info()
