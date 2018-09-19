# -*- coding:utf-8 -*-
# Author: zww

from Include.commons.common import Common
import jieba
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
import json

common = Common()

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
    itemId = input("输入你想查询的产品id: ");
    maxPage = getLastPage(itemId)  # 获取商品评论最大页数
    num = 1
    commentList = []
    while num <= maxPage and num < 20:  # 每个商品的评论我最多取20 页，每页有20条评论，也就是每个商品最多只取 400 个评论
        try:
            # 抓取某个商品的某页评论数据
            tmalljson = getCommentDetail(itemId, num)
            rateList = tmalljson['rateDetail']['rateList']

            n = 0
            while (n < len(rateList)):
                rateContent = rateList[n]['rateContent']
                commentList.append(rateContent)
                n += 1
            print(num)
            num += 1
        except Exception as e:
            num += 1
            print(e)
            continue

    text = "".join(commentList)
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)

    d = os.path.dirname(__file__)
    alice_coloring = np.array(Image.open(os.path.join(d, "shopCart.jpg")))
    my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                             max_font_size=50, random_state=42, width=1000, height=860,
                             font_path='C:/Windows/Fonts/STFANGSO.ttf').generate(wl_space_split)

    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    my_wordcloud.to_file(os.path.join(d, "shopCart1.png"))