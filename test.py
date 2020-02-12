import requests

url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1&productId=100010501300&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"
headers = {
    'Accept': '*/*',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Referer':"https://item.jd.com/100000177760.html#comment"}
r = requests.get(url,headers=headers)
print(r.text)
