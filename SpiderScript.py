from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io

def commentSave(list_comment):
    file = io.open('JD.csv','w',encoding="utf-8", newline = '')
    writer = csv.writer(file)
    writer.writerow(['ID','Nickname','Bought Time','Comment Time','Like','Reply','Phone Type','Rating','Content'])
    for i in range(len(list_comment)):
        writer.writerow(list_comment[i])
    file.close()
    print('Saved')

def getCommentData(maxPage):
    sig_comment = []
    global list_comment
    cur_page = 0
    while cur_page < maxPage:
        cur_page += 1
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&score=%s&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,i,cur_page)
        try:
            response = requests.get(url=url, headers=headers)
            time.sleep(np.random.rand()*2)
            jsonData = response.text
            startLoc = jsonData.find('{')
            #print(jsonData[::-1])//字符串逆序
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            pageLen = len(jsonData['comments'])
            print(url)
            for j in range(0,pageLen):
                userId = jsonData['comments'][j]['id']#ID
                nickName = jsonData['comments'][j]['nickname']#nickName
                boughtTime = jsonData['comments'][j]['referenceTime']#Bought Time
                creationTime = jsonData['comments'][j]['creationTime']#Comment Time
                voteCount = jsonData['comments'][j]['usefulVoteCount']#Like
                replyCount = jsonData['comments'][j]['replyCount']#Reply
                referenceName = jsonData['comments'][j]['referenceName']#Phone Type
                starStep = jsonData['comments'][j]['score']#Rating
                content = jsonData['comments'][j]['content']#Content
                sig_comment.append(userId) #follow the order of column labels
                sig_comment.append(nickname)
                sig_comment.append(referenceTime)
                sig_comment.append(creationTime)
                sig_comment.append(usefulVoteCount)
                sig_comment.append(replyCount)
                sig_comment.append(referenceName)
                sig_comment.append(score)
                sig_comment.append(content)
                list_comment.append(sig_comment)
                sig_comment = []
        except:
            time.sleep(5)
            cur_page -= 1
            print('Wrong URL/Website not loading/Errors in #try, reconnecting in 5 sec')
    return list_comment

if __name__ == "__main__":
    global list_comment
    ua=UserAgent()
    # headers={"User-Agent":ua.random}
    headers = {
    'Accept': '*/*',
    "User-Agent":ua.random,
    'Referer':"https://item.jd.com/100000177760.html#comment"
    }
    #product details: color/set/storage
    productid = ['35216&productId=5089271','136061&productId=5089275','22778&productId=5475612','7021&productId=6784504']
    list_comment = [[]]
    sig_comment = []
    for proc in productid:#all products in terms of color/set/storage
        i = -1
        while i < 7:#all scores
            i += 1
            if(i == 6):
                continue
             #from page 0 to max page
            url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&score=%s&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,i,0)
            print(url)
            try:
                response = requests.get(url=url, headers=headers)
                jsonData = response.text
                startLoc = jsonData.find('{')
                jsonData = jsonData[startLoc:-2]
                jsonData = json.loads(jsonData)
                print("最大页数%s"%jsonData['maxPage'])
                getCommentData(jsonData['maxPage'])
            except:
                i -= 1
                print("wating---")
                time.sleep(5)
                #commentSave(list_comment)
    print("Done Scraping")
    commentSave(list_comment)
