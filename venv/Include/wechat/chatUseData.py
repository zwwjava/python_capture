# -*- coding:utf-8 -*-
# Author: zww
from Include.commons.common import Common
import json
import datetime
import urllib.request
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import pickle


common = Common() #这是个我自己封装的工具类
key = 'cc186c9881b94b42b886a6d634c63002'
key_jh = '777d35900bffe58af88f56069b12785c'
# 提取故事的第一天
readBookStartDay = datetime.datetime(2019, 3, 30)
# 提取情话的第一天
qinghuaStartDay = datetime.datetime(2019, 3, 19)
# 天气计算开始时间
weatherStartDay = datetime.datetime(2019, 4, 14)
cityList = [ '九江', '九江', '九江','九江', '九江', '九江', '九江','九江', '九江', '九江', '九江', '九江','九江', '九江', '九江', '九江','九江', '九江', '九江'];
class DataUtil():

    # 获取天气信息
    def getWeatherData(self, cityname):
        today = datetime.datetime.now()
        dayCount = (today - weatherStartDay).days
        # cityname = cityList[dayCount]
        # 阿凡达数据
        url = ' http://api.avatardata.cn/Weather/Query?key=' + key + '&cityname=' + cityname
        # 聚合数据
        url_jh = 'http://v.juhe.cn/weather/index?key=' + key_jh + '&cityname=' + cityname
        results = common.get(url)
        text = self.parseInfo_afd(results)
        print(text)
        return text

    # 简单的数据封装
    def parseInfo_afd(self, jsons):
        # 将string 转换为字典对象
        jsonData = json.loads(jsons)
        textInfo = '早上好，今天又是元气满满的一天哟.\n'
        data = jsonData['result']['weather'][0]['date']
        week = jsonData['result']['weather'][0]['week']
        nongli = jsonData['result']['weather'][0]['nongli']
        city_name = jsonData['result']['realtime']['city_name']
        lowTemperature = jsonData['result']['weather'][0]['info']['dawn'][2]
        highTemperature = jsonData['result']['weather'][0]['info']['day'][2]
        weather = jsonData['result']['weather'][0]['info']['day'][1]
        wind = jsonData['result']['weather'][0]['info']['day'][4]

        textInfo = textInfo + '今天是' + data + '号\n'
        textInfo = textInfo + '农历:' + nongli + ',星期' + week + '\n'
        textInfo = textInfo + city_name + '气温：' + lowTemperature + '-' + highTemperature + '度，' + weather + ' ' + wind + '\n\n'
        textInfo = textInfo + '穿衣指数：' + jsonData['result']['life']['info']['chuanyi'][0] + ' - ' + jsonData['result']['life']['info']['chuanyi'][1] + '\n\n'
        textInfo = textInfo + '运动指数：' + jsonData['result']['life']['info']['yundong'][0] + ' - ' + jsonData['result']['life']['info']['yundong'][1] + '\n\n'
        textInfo = textInfo + '感冒指数：' + jsonData['result']['life']['info']['ganmao'][0] + ' - ' + jsonData['result']['life']['info']['ganmao'][1]  + '\n\n'
        textInfo = textInfo + '紫外线指数：' + jsonData['result']['life']['info']['ziwaixian'][0] + ' - ' + jsonData['result']['life']['info']['ziwaixian'][1]  + '\n\n'
        textInfo = textInfo + 'by：小可爱的贴心秘书' + '\n'
        return textInfo

    def parseInfo_jh(self, jsons):
        # 将string 转换为字典对象
        jsonData = json.loads(jsons)
        textInfo = '又是元气满满的一天哟.\n'
        data = jsonData['result']['today']['date_y']
        week = jsonData['result']['today']['week']
        city_name = jsonData['result']['today']['city']
        temperature = jsonData['result']['today']['temperature']
        weather = jsonData['result']['today']['weather']
        wind = jsonData['result']['today']['wind']

        textInfo = textInfo + '今天是' + data + ',' + week + '\n\n'
        textInfo = textInfo + city_name + '气温：' + temperature + ' ' + weather + ' ' + wind + '\n\n'
        textInfo = textInfo + '穿衣指数：' + jsonData['result']['today']['dressing_advice'] + '\n\n'
        textInfo = textInfo + '运动指数：' + jsonData['result']['today']['exercise_index'] + '\n\n'
        textInfo = textInfo + '旅游指数：' + jsonData['result']['today']['travel_index'] + '\n\n'
        textInfo = textInfo + '紫外线指数：' + jsonData['result']['today']['uv_index'] + '\n\n'
        textInfo = textInfo + 'by：小可爱的贴心秘书' + '\n'
        return textInfo

    # 睡前故事
    def getBookInfo(self, filePath):
        radioList = [] #微信每次最多只能发送的字符是有限制的，我每25行发送一次信息
        tempInfo = '睡前故事：刘瑜 - 《送你一颗子弹》.\n\n'
        readFlag = False #是否读取
        today = datetime.datetime.now()
        dayCount = (today - readBookStartDay).days + 1
        for line in open(filePath, encoding='utf-8'):
            if (line.find('night.' + str(dayCount)) > -1): # 开始读数据
                readFlag = True
                continue
            if (line.find('night.' + str(dayCount+1)) > -1): # 读完一天数据结束
                break
            if readFlag:
                # 预计文本长度 微信每次最多只能发送的字符是有限制的
                length = len(tempInfo) + len(line)
                if length > 1500:
                    radioList.append(tempInfo)
                    tempInfo = ''
                tempInfo += line
        tempInfo += '\n晚安\n' + 'by：小可爱的贴心秘书' + '\n'
        radioList.append(tempInfo)
        # common.txtToMp3(radioList) #文字生成语音 发送语音
        print(radioList)
        return radioList

    # 每日一句
    def getDaily(self):
        nowDay = datetime.datetime.now().strftime('%Y-%m-%d');
        tempInfo = '早安：\n'
        url = "http://open.iciba.com/dsapi/"   # 官方提供的API
        results = common.get(url)
        resultsData = json.loads(results)
        content = resultsData['content']
        note = resultsData['note']
        translation = resultsData['translation']
        translation = translation.replace("小编的话", "多说一句")
        tempInfo += content + '\n'
        tempInfo += note + '\n\n'
        tempInfo += translation + '\n'
        tempInfo += '\n爱你！\n'
        print(tempInfo)
        return tempInfo

    # 每日情话
    def getQinghua(self, filePath):
        tempInfo = '晚安：\n'
        readFlag = False  # 是否读取
        today = datetime.datetime.now()
        dayCount = (today - qinghuaStartDay).days + 1
        for line in open(filePath, encoding='utf-8'):
            if (line.find('night.' + str(dayCount)) > -1): # 开始读数据
                readFlag = True
                continue
            if (line.find('night.' + str(dayCount+1)) > -1): # 读完一天数据结束
                break
            if readFlag:
                tempInfo += line

        tempInfo += '\n爱你！\n'
        print(tempInfo)
        return tempInfo

    # 每日美图
    def getBingPhoto(self, index):
        # index 对应的是 必应 index天的壁纸
        url = ' http://www.bing.com/HPImageArchive.aspx?format=js&idx=' + index + '&n=1&nc=1469612460690&pid=hp&video=1'
        html = urllib.request.urlopen(url).read().decode('utf-8')

        photoData = json.loads(html)
        # 这是壁纸的 url
        photoUrl = 'https://cn.bing.com' + photoData['images'][0]['url']
        photoReason = photoData['images'][0]['copyright']
        photoReason = photoReason.split(' ')[0]
        photo = urllib.request.urlopen(photoUrl).read()

        # 下载壁纸刀本地
        with open('./bing.jpg', 'wb') as f:
            # img = open_url(photoUrl)
            if photo:
                f.write(photo)
        print("图片已保存")

        # 把壁纸的介绍写到壁纸上
        # 设置所使用的字体
        font = ImageFont.truetype("simhei.ttf",35)
        imageFile = "./bing.jpg"
        im1 = Image.open(imageFile)
        # 画图，把壁纸的介绍写到壁纸上
        draw = ImageDraw.Draw(im1)
        draw.text((im1.size[0]/2.5, im1.size[1]-50), photoReason, (255, 255, 255), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(im1)  # Just draw it!
        # 另存图片
        im1.save("./bing.jpg")

msg_information = {}
if __name__ == '__main__':

    dataUtil = DataUtil()
    dataUtil.getDaily()
    # dataUtil.getBingPhoto('3')
    # stroy = dataUtil.getBookInfo('./送你一颗子弹.txt')

    # qinghua = dataUtil.getQinghua('./qinghua.txt')
    # for line in open('送你一颗子弹.txt', encoding='utf-8'):
    #     print(line)
    #     b = line != ' \n'
    # for txt in stroy:
    #     print(txt)
    # msg_information['001'] = '001'
    # msg_information['002'] = '002'
    # msg_information['003'] = '003'
    # msg_information['004'] = '004'
    # msg_information['005'] = '005'
    # msg_information['006'] = '006'
    # print(len(msg_information))
    # # msg_information.popitem()
    # keys = list(msg_information.keys())
    # msg_information.pop(keys[0])
    # print(msg_information)
    # msg_information['001'] = '001'
    # print(msg_information)


    # with open('./送你1颗子弹.txt',encoding='utf-8',mode =  'w') as f:
    #     for line in open('./送你一颗子弹.txt', encoding='utf-8'):
    #         if line != ' \n':
    #             f.writelines(line)


