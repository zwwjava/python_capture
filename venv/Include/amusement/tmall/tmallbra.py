# -*- coding:utf-8 -*-
# Author: zww

from Include.commons.common import Common
from bs4 import BeautifulSoup

def getData(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body #获取body
    data = body.find('div',{'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        date = day.find('h1').string
        temp.append(date) #添加日期
        inf = day.find_all('p')
        weather = inf[0].string #天气
        temp.append(weather)
        temperature_highest = inf[1].find('span').string #最高温度
        temperature_low = inf[1].find('i').string  # 最低温度
        temp.append(temperature_highest)
        temp.append(temperature_low)
        final.append(temp)
    print('getDate success')
    return final

def getRateDetail(common,itemId,currentPage):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(
        itemId) + '&sellerId=2451699564&order=3&currentPage=' + str(currentPage) + '&append=0callback=jsonp336'
    # itemId 产品id ； sellerId 店铺id 字段必须有值，但随意值就行
    html = common.getUrlContent(url)  # 获取网页信息

    html = html.replace('jsonp1278(','')
    html = html.replace(')','')
    html = html.replace('false','"false"')
    html = html.replace('true','"true"')
    # 将JSON格式的评论数据转换为字典对象
    tmalljson = json.loads(c)
    return tmalljson

if __name__ == '__main__':
    common = Common()
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=' + str(itemId) +'&sellerId=2451699564&order=3&currentPage=' + str(currentPage) + '&append=0callback=jsonp336'
    # itemId 产品id  ； sellerId 店铺id 字段必须有值，但随意值就行
    html = common.getUrlContent(url)    # 获取网页信息
    result = getData(html)  # 解析网页信息，拿到需要的数据
    common.writeData(result, 'D:/py_work/venv/Include/amusement/weather.csv') #数据写入到 csv文档中
    # createTable() #表创建一次就好了，注意
    sql = 'insert into WEATHER(w_id, w_date, w_detail, w_temperature_low, w_temperature_high) value(null, %s,%s,%s,%s)'
    common.patchInsertData(sql, result) #批量写入数据
    print('my frist python file')