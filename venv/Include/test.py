# encoding: utf-8
import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup

class commonUtil:
    def get_content(self, url, data = None):
        header={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'content-type': 'text/html; charset=UTF-8',
            'cache-control': 'no-cache, private'
        }
        timeout = random.choice(range(80, 180))
        while True:
            try:
                rep = requests.get(url, headers=header, timeout=timeout)
                rep.encoding = 'utf-8'
                break
            except socket.timeout as e:
                print( '3:', e)
                time.sleep(random.choice(range(8,15)))

            except socket.error as e:
                print( '4:', e)
                time.sleep(random.choice(range(20, 60)))

            except http.client.BadStatusLine as e:
                print( '5:', e)
                time.sleep(random.choice(range(30, 80)))

            except http.client.IncompleteRead as e:
                print( '6:', e)
                time.sleep(random.choice(range(5, 15)))
        print('getContent success')
        return rep.text

    def getData(self, html_text):
        final = []
        bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
        body = bs.body #获取body
        data = body.find('div',{'class': 'modeSummary'})
        sections = data.find_all('section')

        for section in sections:
            temp = []
            tpp = section.find('div',{'class': 'tpp'})
            grade = tpp.find('p',{'class': 'grade-name'}).string
            temp.append(grade.strip()) #添加等级
            kdLab = tpp.find('div', {'class': 'kd stats-item stats-top-graph'})
            kd = kdLab.find('p').string
            temp.append(kd.strip())  # 添加KD
            winratioLab = tpp.find('div', {'class': 'winratio'})
            winratio = winratioLab.find('p').string
            temp.append(winratio.strip())  # 添加吃鸡率
            top10Lab = tpp.find('div', {'class': 'top10s'})
            top10 = top10Lab.find('p').string
            temp.append(top10.strip())  # 添加top10
            dealsLab = tpp.find('div', {'class': 'deals'})
            deal = dealsLab.find('p').string
            temp.append(deal.strip())  # 添加平均伤害
            gamesLab = tpp.find('div', {'class': 'games'})
            games = gamesLab.find('p').string
            temp.append(games.strip())  # 添加游戏局数
            mostkillsLab = tpp.find('div', {'class': 'mostkills'})
            mostkills = mostkillsLab.find('p').string
            temp.append(mostkills.strip())  # 添加单句最高杀人数
            headshotsLab = tpp.find('div', {'class': 'headshots'})
            headshots = headshotsLab.find('p').string
            temp.append(headshots.strip())  # 添加爆头率
            survivalLab = tpp.find('div', {'class': 'survival'})
            survival = survivalLab.find('p').string
            temp.append(survival.strip())  # 添加存活时间
            final.append(temp)
        print('getData success')
        return final

    def write_data(self, data, name):
        file_name = name
        with open(file_name, 'a', errors='ignore', newline='') as f:
                f_csv = csv.writer(f)
                f_csv.writerows(data)
        print('step3')

if __name__ == '__main__':
    common = commonUtil()
    hostUrl = 'https://dak.gg/profile/'
    endUrl = '/2018-08/as'
    nameList = {'HRHLXL520', 'zhufuhengniubi', 'LittleNice_', 'Z_W_W_Z_S'}
    for name in nameList:
        url = hostUrl + name + endUrl
        html = common.get_content(url)
        result = common.getData(html)
        common.write_data(result, 'F:/Python/workspace/venv/Include/CJ/weather.csv')
    print('success')