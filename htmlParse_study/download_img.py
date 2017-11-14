# 批量下载图片
import requests
import time
from bs4 import BeautifulSoup

from contextlib import closing
path = 'C:/Users/huyongyong/Desktop/test/'

def download_img():
    img_list = html_parse()
    print(img_list)
    i = 0
    for img in img_list:
        print('now downloading:' + img)
        pic = requests.get(img)
        fp = open(path+str(i)+'.jpg', 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1

def get_img_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    time.sleep(5)
    return data
def html_parse():
    download_img_list = []
    for pageNo in range(0, 12):
        if pageNo == 0:
            url = 'http://www.ivsky.com/tupian/ziranfengguang/'
        else:
            url = 'http://www.ivsky.com/tupian/ziranfengguang/index_'+str(pageNo)+'.html'
        print(url)
        html = get_img_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find('ul', attrs={'class', 'ali'})
        for li in ul.find_all('li'):
            imgUrl = li.find('img').get('src')
            download_img_list.append(imgUrl)
    return download_img_list
if __name__ == '__main__':
    download_img()