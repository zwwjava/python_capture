# -*- coding:utf-8 -*-
# Author: zww
from Include.commons.common import Common
import json
import datetime

common = Common()
key = 'cc186c9881b94b42b886a6d634c63002'
readBookStartDay = datetime.datetime(2018, 9, 29)
class DataUtil():

    def getWeatherData(self, cityname):
        url = ' http://api.avatardata.cn/Weather/Query?key=' + key + '&cityname=' + cityname
        results = common.getUrlContent(url)
        text = self.parseInfo(results)
        print(text)
        return text

    def parseInfo(self, jsons):
        # 将string 转换为字典对象
        jsonData = json.loads(jsons)
        textInfo = '又是元气满满的一天哟.\n'
        data = jsonData['result']['weather'][0]['date']
        week = jsonData['result']['weather'][0]['week']
        nongli = jsonData['result']['weather'][0]['nongli']
        city_name = jsonData['result']['realtime']['city_name']
        lowTemperature = jsonData['result']['weather'][0]['info']['dawn'][2]
        highTemperature = jsonData['result']['weather'][0]['info']['day'][2]
        weather = jsonData['result']['weather'][0]['info']['day'][1]
        wind = jsonData['result']['weather'][0]['info']['day'][4]

        textInfo = textInfo + '今天是' + data + '\n'
        textInfo = textInfo + '农历:' + nongli + ',星期' + week + '\n'
        textInfo = textInfo + city_name + '气温：' + lowTemperature + '-' + highTemperature + '度，' + weather + ' ' + wind + '\n'
        textInfo = textInfo + '紫外线指数：' + jsonData['result']['life']['info']['ziwaixian'][0] + ' - ' + jsonData['result']['life']['info']['ziwaixian'][1] + '\n\n'
        textInfo = textInfo + '穿衣指数：' + jsonData['result']['life']['info']['chuanyi'][0] + ' - ' + jsonData['result']['life']['info']['chuanyi'][1] + '\n\n'
        textInfo = textInfo + '运动指数：' + jsonData['result']['life']['info']['yundong'][0] + ' - ' + jsonData['result']['life']['info']['yundong'][1]  + '\n\n'
        textInfo = textInfo + '感冒指数：' + jsonData['result']['life']['info']['ganmao'][0] + ' - ' + jsonData['result']['life']['info']['ganmao'][1]
        return textInfo

    def getBookInfo(self, filePath):
        textInfo = '睡前故事：张嘉佳 - 《从你的全世界路过》.\n\n'
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
                textInfo += line
        textInfo += '\n晚安'
        print(textInfo)
        return textInfo

if __name__ == '__main__':
    dataUtil = DataUtil()
    # dataUtil.getWeatherData('南昌')
    str = dataUtil.getBookInfo('./从你的全世界路过.txt')