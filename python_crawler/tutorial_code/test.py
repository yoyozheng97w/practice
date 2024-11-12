from urllib import request
from bs4 import BeautifulSoup

url ='https://www.ptt.cc/bbs/joke/index.html'

# 使用 headers
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
print(res)

# 不為字串，為 BeautifulSoup 物件
# soup = BeautifulSoup(res)       # 會有警告，因 parser 不明確
soup = BeautifulSoup(res, 'html.parser')

# find(), findAll()

# # html 中，<div id="action-bar-container"> </div> 裡的東西
# action_bar_find = soup.find('div', {'id' : 'action-bar-container'})
# # print(action_bar_find)
# tmp_div = action_bar_find.find('div')   # 不用 list

# action_bar = soup.findAll('div', {'id' : 'action-bar-container'})
# # print(action_bar)

# # 在 action_bar 中找第一個 <div>
# tmp_div = action_bar[0].find('div')
# # print(tmp_div)
# tmp_div_div = action_bar[0].div.div
# # print(tmp_div_div)

# # 在 action_bar 中找所有 <a>
# tmp_a_all = action_bar[0].findAll('a')
# # print(tmp_a_all)

# # 在 action_bar 中找第一個 <a>
# tmp_a = action_bar[0].find('a')
# # print(tmp_a)

# # 取出 tmp_a 的內容，
# # 例子：
# #   tmp_a = <a class="btn selected" href="/bbs/joke/index.html">看板</a>
# #   tmp_a.text = "看板"
# tmp_text_in_a = tmp_a.text
# tmp_String_in_a = tmp_a.string
# # print(tmp_text_in_a)

# # 取出標籤裡的東西，用法像字典，但其實不是字典
# tmp_url = tmp_a['href']
# # print("https://www.ptt.cc" + tmp_url)
# #--------------------------------------------------------

# # select_one(), select()

# action_bar_sel = soup.select('div[id="action-bar-container"]')
# # action_bar_sel = soup.select('div#action-bar-container')

# tmp_next_sibling = action_bar_sel[0].div.div.next_sibling.next_sibling
# # print(tmp_next_sibling)

# tmp_siblings = tmp_next_sibling.a.next_siblings
# for i in tmp_siblings:
#     print(i.text)