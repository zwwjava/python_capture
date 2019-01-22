# encoding: utf-8
# author zww

from bs4 import BeautifulSoup
from Include.commons.common import Common

def getData(html_text, name, solo, double, squad):
    index = 1
    final = []
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body
    data = body.find('div', {'class': 'modeSummary'})
    sections = data.find_all('section')

    for section in sections:
        temp = []
        tpp = section.find('div', {'class': 'tpp'})
        vaild = tpp.find('p', {'class': 'grade-name'})
        if not vaild:
            index += 1
            print('empty data')
            continue

        grade = tpp.find('p', {'class': 'grade-name'}).string
        temp.append(grade.strip())  # 添加等级
        temp.append(name)  # 添加名称
        kdLab = tpp.find('div', {'class': 'kd stats-item stats-top-graph'})
        kd = kdLab.find('p').string
        temp.append(kd.strip())  # 添加KD
        winratioLab = tpp.find('div', {'class': 'winratio'})
        winratio = winratioLab.find('p').string
        temp.append(winratio.strip().replace('%', ''))  # 添加吃鸡率
        top10Lab = tpp.find('div', {'class': 'top10s'})
        top10 = top10Lab.find('p').string
        temp.append(top10.strip().replace('%', ''))  # 添加top10
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
        temp.append(headshots.strip().replace('%', ''))  # 添加爆头率
        survivalLab = tpp.find('div', {'class': 'survival'})
        survival = survivalLab.find('p').string
        temp.append(survival.strip())  # 添加存活时间
        if index == 1:
            solo.append(temp)
        elif index == 2:
            double.append(temp)
        elif index == 3:
            squad.append(temp)
        index += 1
    final.append(temp)
    print('getData success')
    return final

if __name__ == '__main__':
    common = Common()
    hostUrl = 'https://dak.gg/profile/'
    endUrl = '/2018-09/as'
    nameList = {'HRHLXL520', 'zhufuhengniubi', 'LittleNice_', 'Z_W_W_Z_S'}
    solo = []
    double = []
    squad = []
    for name in nameList:
        url = hostUrl + name + endUrl
        html = common.getUrlContent(url)
        result = getData(html, name, solo, double, squad)
        # common.writeData(result, 'D:/workSpace/pySpace/venv/Include/CJ/runned.csv')

    solosql = "insert into solo(solo_uuid, level, user_name, KD, win_rate, top_ten_rate, average_demage, count_game, most_kill, head_shot_rate, survived) value(null, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dousql = "insert into doub(doub_uuid, level, user_name, KD, win_rate, top_ten_rate, average_demage, count_game, most_kill, head_shot_rate, survived) value(null, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    squadsql = "insert into squad(squad_uuid, level, user_name, KD, win_rate, top_ten_rate, average_demage, count_game, most_kill, head_shot_rate, survived) value(null, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    common.patchInsertData(solosql, solo)
    common.patchInsertData(dousql, double)
    common.patchInsertData(squadsql, squad)
    print('success')