# encoding: utf-8
# author zww

from pyecharts import Radar
from Include.commons.common import Common


if __name__ == '__main__':
    common = Common()
    results = common.queryData("select * from squad") #获取四排战绩

    # 初始化雷达图
    schema = [
        ("KD", 1.6), ("吃鸡率", 6), ("Top10", 45),
        ("场均伤害", 220), ("最多击杀", 9), ("爆头率", 35)
    ]
    radar = Radar(width=1300, height=620)
    radar.config(schema)
    # 设置样例颜色
    range_color = ['#313695', '#a50026', '#74add1', '#fdae61', '#e0f3f8', '#ffffbf',
                   '#fee090', '#f46d43']
    index = 0
    for result in results:
        data = [[str(result[3]),str(result[4]),str(result[5]),str(result[6]),str(result[8]),str(result[9])]]
        radar.add(result[2], data, item_color=range_color[index])
        index += 1

    radar.render()
    print('success')


