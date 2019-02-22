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

common = Common()
key = 'cc186c9881b94b42b886a6d634c63002'
key_jh = '777d35900bffe58af88f56069b12785c'
readBookStartDay = datetime.datetime(2019, 2, 15)
class DataUtil():

    def getWeatherData(self, cityname):
        url = ' http://api.avatardata.cn/Weather/Query?key=' + key + '&cityname=' + cityname
        url_jh = 'http://v.juhe.cn/weather/index?key=' + key_jh + '&cityname=' + cityname
        results = common.get(url)
        text = self.parseInfo_afd(results)
        print(text)
        return text

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
        textInfo = textInfo + 'by：小可爱专属秘书' + '\n\n'
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
        textInfo = textInfo + 'by：小可爱专属秘书' + '\n'
        return textInfo

    def getBookInfo(self, filePath):
        radioList = []
        row = 0
        textInfo = '睡前故事：张嘉佳 - 《从你的全世界路过》.\n\n'
        tempInfo = '睡前故事：张嘉佳 - 《从你的全世界路过》.\n\n'
        file = open(filePath)
        readFlag = False
        today = datetime.datetime.now()
        dayCount = (today - readBookStartDay).days + 1
        for line in open(filePath):


            # if (line == '\n'):
            #     continue
            if (line.find('night.' + str(dayCount)) > -1):
                readFlag = True
                continue
            if (line.find('night.' + str(dayCount+1)) > -1):
                break
            if readFlag:
                row += 1
                textInfo += line
                tempInfo += line

                if row == 25:
                    radioList.append(tempInfo)
                    tempInfo = ''
                    row = 0
        textInfo += '\n晚安'
        tempInfo += '\n晚安'
        radioList.append(tempInfo)
        # common.txtToMp3(radioList)
        # print(textInfo)
        return radioList

    def getBingPhoto(self, index):
        url = ' http://www.bing.com/HPImageArchive.aspx?format=js&idx=' + index + '&n=1&nc=1469612460690&pid=hp&video=1'
        html = urllib.request.urlopen(url).read().decode('utf-8')

        photoData = json.loads(html)
        photoUrl = 'https://cn.bing.com' + photoData['images'][0]['url']
        photoReason = photoData['images'][0]['copyright']
        photoReason = photoReason.split(' ')[0]
        photo = urllib.request.urlopen(photoUrl).read()

        with open('./bing.jpg', 'wb') as f:
            # img = open_url(photoUrl)
            if photo:
                f.write(photo)
        print("图片已保存")
        # 设置所使用的字体
        font = ImageFont.truetype("simhei.ttf",35)

        # 打开图片
        imageFile = "./bing.jpg"
        im1 = Image.open(imageFile)

        # 画图
        draw = ImageDraw.Draw(im1)
        draw.text((im1.size[0]/2.5, im1.size[1]-50), photoReason, (255, 255, 255), font=font)  # 设置文字位置/内容/颜色/字体
        draw = ImageDraw.Draw(im1)  # Just draw it!

        # 另存图片
        im1.save("./bing.jpg")
msg_information = {}
if __name__ == '__main__':
    dataUtil = DataUtil()
    dataUtil.getWeatherData('九江')
    # # dataUtil.getBingPhoto('2')
    # stroy = dataUtil.getBookInfo('./从你的全世界路过.txt')
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


    # with open('./2018.12.25.1.txt',encoding='utf-8',mode =  'w') as f:
    #     for line in open('./2018.12.25.txt', encoding='utf-8'):
    #         newLine = "20190122" + line[8:len(line)]
    #         f.writelines(newLine)


