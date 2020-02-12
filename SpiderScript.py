#found duplicates from existing code
#testing for single product different rating & page
#test product: huawei v30 basic set blue

from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import numpy as np
import requests
import json
import csv
import io

def commentSave(list_comment):
    file = io.open('test 5.csv','w',encoding="utf-8", newline = '')
    writer = csv.writer(file)
    writer.writerow(['ID','Nickname','Bought Time','Comment Time','Like','Reply','Phone Color','Phone Memory','Set','Rating','Content','url'])
    for i in range(len(list_comment)):
        writer.writerow(list_comment[i])
    file.close()
    print('Saved')

#get displayed comments
def getCommentData(maxPage):
    sig_comment = []
    global list_comment
    cur_page = 0
    while cur_page < maxPage:
        cur_page += 1
        #in default setting JD displays comments for all product color/types/packages under the same product ID(need to be checked might be case by case)
        #under score = 0, all coments with rating from 1 - 5 are displayed
        #link for displayed comments
        url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1&productId=%s&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc, cur_page)
        try:
            response = requests.get(url=url, headers=headers)
            time.sleep(np.random.rand()*2)
            jsonData = response.text
            startLoc = jsonData.find('{')
            #print(jsonData[::-1])//字符串逆序
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            pageLen = len(jsonData['comments'])
            print('Page Number: %s'%cur_page)
            for j in range(0,pageLen):
                userId = jsonData['comments'][j]['id']#ID
                nickName = jsonData['comments'][j]['nickname']#nickName
                boughtTime = jsonData['comments'][j]['referenceTime']#Bought Time
                creationTime = jsonData['comments'][j]['creationTime']#Comment Time
                voteCount = jsonData['comments'][j]['usefulVoteCount']#Like
                replyCount = jsonData['comments'][j]['replyCount']#Reply
                phoneColor = jsonData['comments'][j]['productColor']#Phone Color
                phoneMemory = jsonData['comments'][j]['productSize']#Phone Color
                phoneSet = jsonData['comments'][j]['productSales']#Phone Color
                starStep = jsonData['comments'][j]['score']#Rating
                content = jsonData['comments'][j]['content']#Content
                sig_comment.append(userId) #follow the order of column labels
                sig_comment.append(nickName)
                sig_comment.append(boughtTime)
                sig_comment.append(creationTime)
                sig_comment.append(voteCount)
                sig_comment.append(replyCount)
                sig_comment.append(phoneColor)
                sig_comment.append(phoneMemory)
                sig_comment.append(phoneSet)
                sig_comment.append(starStep)
                sig_comment.append(content)
                sig_comment.append(url)
                list_comment.append(sig_comment)
                sig_comment = []
        except:
            time.sleep(5)
            cur_page -= 1
            print('Wrong URL/Website not loading/Errors in #try, reconnecting in 5 sec')
    return list_comment

def getFoldCommentData(maxPage):
    sig_comment = []
    global list_comment
    cur_page = 0
    while cur_page < maxPage:
        cur_page += 1
        #in default setting JD displays comments for all product color/types/packages under the same product ID(need to be checked might be case by case)
        #under score = 0, all coments with rating from 1 - 5 are displayed
        #link for folded comments
        url = 'https://club.jd.com/comment/getProductPageFoldComments.action?callback=jQuery2&productId=100010501298&score=0&sortType=6&page=%s&pageSize=5&_=1581492569799'%(cur_page)
        try:
            response = requests.get(url=url, headers=headers)
            time.sleep(np.random.rand()*2)
            jsonData = response.text
            startLoc = jsonData.find('{')
            #print(jsonData[::-1])//字符串逆序
            jsonData = jsonData[startLoc:-2]
            jsonData = json.loads(jsonData)
            pageLen = len(jsonData['comments'])
            print('Page Number: %s'%cur_page)
            for j in range(0,pageLen):
                userId = jsonData['comments'][j]['id']#ID
                nickName = jsonData['comments'][j]['nickname']#nickName
                boughtTime = jsonData['comments'][j]['referenceTime']#Bought Time
                creationTime = jsonData['comments'][j]['creationTime']#Comment Time
                voteCount = jsonData['comments'][j]['usefulVoteCount']#Like
                replyCount = jsonData['comments'][j]['replyCount']#Reply
                phoneColor = jsonData['comments'][j]['productColor']#Phone Color
                phoneMemory = jsonData['comments'][j]['productSize']#Phone Color
                phoneSet = jsonData['comments'][j]['productSales']#Phone Color
                starStep = jsonData['comments'][j]['score']#Rating
                content = jsonData['comments'][j]['content']#Content
                sig_comment.append(userId) #follow the order of column labels
                sig_comment.append(nickName)
                sig_comment.append(boughtTime)
                sig_comment.append(creationTime)
                sig_comment.append(voteCount)
                sig_comment.append(replyCount)
                sig_comment.append(phoneColor)
                sig_comment.append(phoneMemory)
                sig_comment.append(phoneSet)
                sig_comment.append(starStep)
                sig_comment.append(content)
                sig_comment.append(url)
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
    productid = ['100010131982','100005850089','100005850091','100010501298','100010501300']
    list_comment = [[]]
    sig_comment = []
    for proc in productid:
         #from page 0 to max page
        url1 = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1&productId=%s&score=0&sortType=6&page=%s&pageSize=10&isShadowSku=0&fold=1'%(proc,0)
        print(url1)
        response = requests.get(url=url1, headers=headers)
        jsonData = response.text
        startLoc = jsonData.find('{')
        jsonData = jsonData[startLoc:-2]
        jsonData = json.loads(jsonData)
        print("Total Pages:%s"%jsonData['maxPage'])
        getCommentData(jsonData['maxPage'])
    
        url2 = 'https://club.jd.com/comment/getProductPageFoldComments.action?callback=jQuery2&productId=%s&score=0&sortType=6&page=%s&pageSize=5&_=1581492569799'%(proc,0)
        print(url2)
        response = requests.get(url=url2, headers=headers)
        jsonData = response.text
        startLoc = jsonData.find('{')
        jsonData = jsonData[startLoc:-2]
        jsonData = json.loads(jsonData)
        print("Total Pages:%s"%jsonData['maxPage'])
        getFoldCommentData(jsonData['maxPage'])
        #commentSave(list_comment)
    print("Done Scraping")
    commentSave(list_comment)
