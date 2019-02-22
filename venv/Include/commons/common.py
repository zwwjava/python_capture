# -*- coding:utf-8 -*-
# Author: zww
import requests
import time
import random
import socket
import http.client
import pymysql
import csv
import jieba
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
from snownlp import SnowNLP
from aip import AipSpeech


# 百度AI 账号信息
APP_ID = '15569705'
API_KEY = 'U1DZPCSmO2YwtyHy7egVw1Q8'
SECRET_KEY = 'eSGmrcldRtzYSo8O9FQkjTKAn0nvytf3 '

# 封装requests
class Common(object):
    def get(self, url, data=None):
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'user-agent': "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            'cache-control': 'max-age=0'
        }  # request 的请求头
        timeout = random.choice(range(80, 180))
        while True:
            try:
                rep = requests.get(url, headers=header, timeout=timeout)  # 请求url地址，获得返回 response 信息
                break
            except socket.timeout as e:  # 以下都是异常处理
                print('3:', e)
                time.sleep(random.choice(range(8, 15)))
            except socket.error as e:
                print('4:', e)
                time.sleep(random.choice(range(20, 60)))
            except http.client.BadStatusLine as e:
                print('5:', e)
                time.sleep(random.choice(range(30, 80)))
            except http.client.IncompleteRead as e:
                print('6:', e)
                time.sleep(random.choice(range(5, 15)))
        print('request success')
        return rep.text  # 返回的 Html 全文

    def post(self, url, data=None):
        header = {
            'user-agent': "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            'cache-control': 'max-age=0'
        }  # request 的请求头
        while True:
            try:
                rep = requests.post(url, data, headers=header)  # 请求url地址，获得返回 response 信息
                break
            except socket.timeout as e:  # 以下都是异常处理
                print('3:', e)
                time.sleep(random.choice(range(8, 15)))
            except socket.error as e:
                print('4:', e)
                time.sleep(random.choice(range(20, 60)))
            except http.client.BadStatusLine as e:
                print('5:', e)
                time.sleep(random.choice(range(30, 80)))
            except http.client.IncompleteRead as e:
                print('6:', e)
                time.sleep(random.choice(range(5, 15)))
        print('request success')
        return rep.text  # 返回的 Html 全文

    def writeData(self, data, url):
        with open(url, 'a', errors='ignore', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(data)
        print('write_csv success')

    def queryData(self, sql):
        db = pymysql.connect("localhost", "zww", "960128", "test")
        cursor = db.cursor()
        results = []
        try:
            cursor.execute(sql)    #执行查询语句
            results = cursor.fetchall()
        except Exception as e:
            print('查询时发生异常' + e)
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
        return results
        print('insert data success')

    def insertData(self, sql):
        # 打开数据库连接
        db = pymysql.connect("localhost", "zww", "960128", "test")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        print(sql)
        try:
            # sql = "INSERT INTO WEATHER(w_id, w_date, w_detail, w_temperature) VALUES (null, '%s','%s','%s')" % (data[0], data[1], data[2])
            # sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
            cursor.execute(sql)    #单条数据写入
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print('插入时发生异常' + e)
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
        print('insert data success')

    def patchInsertData(self, sql, datas):
        # 打开数据库连接
        db = pymysql.connect("localhost", "zww", "960128", "test")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        try:
            # 批量插入数据
            # cursor.executemany('insert into WEATHER(w_id, w_date, w_detail, w_temperature_low, w_temperature_high) value(null, %s,%s,%s,%s)',datas)
            cursor.executemany(sql, datas)

            # 提交到数据库执行
            db.commit()
        except Exception as e:
            print('插入时发生异常' + e)
            # 如果发生错误则回滚
            db.rollback()
        # 关闭数据库连接
        db.close()
        print('insert data success')

    def wordCloudShow(self, txt, pngName, toDirect, backgroundColor, maxFontSize, width, height):
        wordlist_jieba = jieba.cut(txt, cut_all=True)
        wl_space_split = " ".join(wordlist_jieba)

        d = os.path.dirname(__file__)
        alice_coloring = np.array(Image.open(os.path.join(d, pngName)))
        my_wordcloud = WordCloud(background_color=backgroundColor, max_words=2000, mask=alice_coloring,
                                 max_font_size=maxFontSize, random_state=42, width=width, height=height,
                                 font_path='C:/Windows/Fonts/STFANGSO.ttf').generate(wl_space_split)

        image_colors = ImageColorGenerator(alice_coloring)
        plt.imshow(my_wordcloud.recolor(color_func=image_colors))
        plt.imshow(my_wordcloud)
        plt.axis("off")
        plt.show()
        my_wordcloud.to_file(os.path.join(d, toDirect))

    def showSentiments(self, txt):
        temp = SnowNLP(txt)
        print(temp.sentiments)
        return temp.sentiments

    # txt 为list
    def txtToMp3(self, txts):
        print('开始进行文件转MP3')
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        with open('Passing through your world.mp3', 'wb') as f:
            for txt in txts:
                print('正在进行文件转MP3...')
                result = client.synthesis(txt, 'zh', 1, {'pit': 3,'spd': 4,'vol': 5, 'per': 3})
                # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
                if not isinstance(result, dict):
                    f.write(result)

if __name__ == '__main__':
    common = Common()
    common.txtToMp3(["night.3。。初恋是一个人的兵荒马乱。。night.3。。初恋是一个人的兵荒马乱。。night.3。。初恋是一个人的兵荒马乱。。"])