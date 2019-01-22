# -*- coding:utf-8 -*-
# Author: zww
import urllib.request,re,sys,os
import json

def open_url(url):
    # 根据当前URL创建请求包
    req = urllib.request.Request(url)
    # 添加头信息，伪装成浏览器访问
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
    # 发起请求
    response = urllib.request.urlopen(req)
    # 返回请求到的HTML信息
    return response.read()

if __name__ == '__main__':
    # 有一串json加载进了一张jpg和相关信息
    url = ' http://www.bing.com/HPImageArchive.aspx?format=js&idx=' + str(-1) + '&n=1&nc=1469612460690&pid=hp&video=1'
    html = urllib.request.urlopen(url).read().decode('utf-8')

    photoData = json.loads(html)
    photoUrl = 'https://cn.bing.com' + photoData['images'][0]['url']
    photo = urllib.request.urlopen(photoUrl).read()

    with open('./bing.jpg', 'wb') as f:
        # img = open_url(photoUrl)
        if photo:
            f.write(photo)
    print("图片已保存")

