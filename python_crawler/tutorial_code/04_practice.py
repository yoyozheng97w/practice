import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

url =f'https://www.ptt.cc/bbs/Gossiping/index.html'

# 建立 headers
load_dotenv()
useragent = os.getenv("USER_AGENT")
headers = {'User-Agent' : useragent}

# 向伺服器發出請求
res = requests.get(url, headers=headers)
# res.text 會是看起來像 html 的 str
# 把此 str 變成 bs4 的物件，就可以對此物件操作 bs4 裡的函式
soup = BeautifulSoup(res.text, 'html.parser')

article = soup.select('div[class="title"]')
print(article)

# 找出文章列表裡的所有文章連結，並對每個連結 request
for each_article in article:
    lnk = "https://www.ptt.cc" + each_article.a['href']
    res_each_lnk = requests.get(lnk, headers=headers)
    print(lnk)
    each_soup = BeautifulSoup(res_each_lnk.text, 'html.parser')
    tmp = each_soup.select_one('div[class="article-metaline"]')
    print(tmp.findAll('span')[1].text)
    print()