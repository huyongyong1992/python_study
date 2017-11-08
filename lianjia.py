import json
import time
import requests
import xlwt

def get_house_info():
    # 循环100页，每一页爬取职位列表信息
    for pageNo in range(1, 101):
        # 请求参数
        params = {
            'type': 1,
            'query': 'https://hz.lianjia.com/ershoufang/pg'+str(pageNo)
        }
        print(params['query'])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Host': 'hz.lianjia.com',
            'Referer': 'https://hz.lianjia.com/ershoufang/pg'+str(pageNo),
            'Cookie': 'select_city=330100; all-lj=826650ca2d8980f8a49f6d8acab99d41; lianjia_uuid=940ff291-7048-427f-a0ae-95bcea872f72; UM_distinctid=15f9a2759fae3-0fc5c2eb72d0d2-3b3e5906-1fa400-15f9a2759fb20; _ga=GA1.2.2043551227.1510119793; _gid=GA1.2.810777045.1510119793; CNZZDATA1253492436=1029596203-1510117427-https%253A%252F%252Fwww.baidu.com%252F%7C1510117427; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1510119791; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1510120246; _smt_uid=5a02996f.294e85b6; CNZZDATA1254525948=274108717-1510116130-https%253A%252F%252Fwww.baidu.com%252F%7C1510116130; CNZZDATA1255633284=1038044724-1510118789-https%253A%252F%252Fwww.baidu.com%252F%7C1510118789; CNZZDATA1255604082=971648280-1510116245-https%253A%252F%252Fwww.baidu.com%252F%7C1510116245; lianjia_ssid=b2fd0b9c-b332-432a-8249-7a8be84fee0a'
        }
        url = 'https://hz.lianjia.com/api/newhouserecommend?type=1&query=https%3A%2F%2Fhz.lianjia.com%2Fershoufang%2Fpg'+str(pageNo)+'%2F'
        print(url)


        # 通过get获取详情页信息
        result = requests.get(url, headers=headers).json()
        time.sleep(2)
        print(result)
        # #把爬取到的信息写入json文件
        line = json.dumps(result['data'])
        with open('lianjia.json', 'ab+') as fp:
            fp.write(line.encode('utf-8'))
        return result
# 通过xlwt(python操作office的模块)设置utf编码格式，并返回一个excel对象'book'
# book = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet = book.add_sheet('链家二手房信息', cell_overwrite_ok=True)
# sheet.write(0, 0, '位置')
# sheet.write(0, 1, '楼层')
# sheet.write(0, 2, '面积')
# sheet.write(0, 3, '结构')
# sheet.write(0, 2, '总价')
# sheet.write(0, 3, '单价')
# 定义一个全局的行数n，为了下面parser_to_excel方法写入excel时可以找到从哪一行开始写入
# n=1
# def json2excel():
#     json = get_house_info()['data']
#     print(json)
#     for item in json:
#         global n
#         sheet.write(0, 0, item['address'])
#         sheet.write(0, 1, '楼层')
#         sheet.write(0, 2, item['resblock_frame_area'])
#         sheet.write(0, 3, item['rooms'])
#         sheet.write(0, 2, item['show_price'])
#         sheet.write(0, 3, item['price'])
#         n = n+1
#     book.save(u'链家.xlsx')  # 保存


if __name__ == '__main__':
    get_house_info()
