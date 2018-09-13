# -*- coding:utf-8 -*-
# Author: zww

from Include.commons.common import Common
from bs4 import BeautifulSoup
import json
import re
import pymysql

common = Common()

# 获取商品id
def getProductIdList():
    url = 'https://list.tmall.com/search_product.htm?q=内衣' # q参数 是查询的关键字
    html = common.getUrlContent(url)  # 获取网页信息
    soup = BeautifulSoup(html,'html.parser')
    idList = []
    # 用Beautiful Soup提取商品页面中所有的商品ID
    productList = soup.find_all('div', {'class': 'product'})
    for product in productList:
        idList.append(product['data-id'])
    return idList

# 获取商品评论数据
def getCommentDetail(itemId,currentPage):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(
        itemId) + '&sellerId=2451699564&order=3&currentPage=' + str(currentPage) + '&append=0callback=jsonp336'
    # itemId 产品id ； sellerId 店铺id 字段必须有值，但随意值就行
    html = common.getUrlContent(url)  # 获取网页信息
    # 删掉返回的多余信息
    html = html.replace('jsonp128(','') #需要确定是不是 jsonp128
    html = html.replace(')','')
    html = html.replace('false','"false"')
    html = html.replace('true','"true"')

    # 将string 转换为字典对象
    tmalljson = json.loads(html)
    return tmalljson

# 获取商品评论最大页数
def getLastPage(itemId):
    tmalljson = getCommentDetail(itemId,1)
    return tmalljson['rateDetail']['paginator']['lastPage'] #最大页数

if __name__ == '__main__':
    productIdList = getProductIdList() #获取商品id
    initial = 0
    while initial < len(productIdList) - 30:  # 总共有60个商品，我只取了前30个
        try:
            itemId = productIdList[initial]
            print('----------', itemId, '------------')
            maxPage = getLastPage(itemId) #获取商品评论最大页数
            num = 1
            while num <= maxPage and num < 20: #每个商品的评论我最多取20 页，每页有20条评论，也就是每个商品最多只取 400 个评论
                try:
                    # 抓取某个商品的某页评论数据
                    tmalljson = getCommentDetail(itemId, num)
                    rateList = tmalljson['rateDetail']['rateList']
                    commentList = []
                    n = 0
                    while (n < len(rateList)):
                        comment = []
                        # 商品描述
                        colorSize = rateList[n]['auctionSku']
                        m = re.split('[:;]', colorSize)
                        rateContent = rateList[n]['rateContent']
                        dtime = rateList[n]['rateDate']
                        comment.append(m[1])
                        comment.append(m[3])
                        comment.append('天猫')
                        comment.append(rateContent)
                        comment.append(dtime)
                        commentList.append(comment)
                        n += 1
                    print(num)
                    sql = "insert into bras(bra_id, bra_color, bra_size, resource, comment, comment_time)  value(null, %s, %s, %s, %s, %s)"
                    common.patchInsertData(sql, commentList) # mysql操作的批量插入
                    num += 1
                except Exception as e:
                    num += 1
                    print(e)
                    continue
            initial += 1
        except Exception as e:
            print(e)
