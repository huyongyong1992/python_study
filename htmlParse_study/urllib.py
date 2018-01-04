from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.baidu.com'

html = urlopen(url)
bsObj = BeautifulSoup(html)
print(bsObj)
# imageLocation = bsObj.find("a", {"id", "logo"}).find('img')['src']
# urlretrieve(imageLocation, "logo.jpg")