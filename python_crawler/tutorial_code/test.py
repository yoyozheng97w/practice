from urllib import request

url = 'http://httpbin.org/get'
res = request.urlopen(url)

# print(f"res.read: \n{res.read()}")
# b 開頭表其型態為 bytes，
# 使用 decode('utf8') 將 bytes 轉為字串，
# 輸出為整齊的 HTML 原始碼
# 輸出結果為看起來像 json 檔的 string
print(f"res.read: \n{res.read().decode('utf8')}")