# -*- coding:utf-8 -*-
# Author: zww
import requests
import time
import random
import socket
import http.client
import pymysql
import csv

# 封装requests
class Common(object):
    def getUrlContent(self, url, data=None):
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
                # rep.encoding = 'utf-8'
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
        db = pymysql.connect("localhost", "zww", "960128", "zwwdb")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        try:
            # sql = "INSERT INTO WEATHER(w_id, w_date, w_detail, w_temperature) VALUES (null, '%s','%s','%s')" % (data[0], data[1], data[2])
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
