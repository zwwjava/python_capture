# encoding: utf-8
# author zww

from Include.commons.common import Common
from pyecharts import Bar

common = Common()
def showSize():
    results = common.queryData("""select count(*) from bra where bra_size like '%A' 
                union all select count(*) from bra where bra_size like '%B' 
                union all select count(*) from bra where bra_size like '%C' 
                union all select count(*) from bra where bra_size like '%D' 
                union all select count(*) from bra where bra_size like '%E' 
                union all select count(*) from bra where bra_size like '%F' 
                union all select count(*) from bra where bra_size like '%G'""")  # 获取每个罩杯数量
    attr = ["A罩杯", 'G罩杯', "B罩杯", "C罩杯", "D罩杯", "E罩杯", "F罩杯"]
    v1 = [results[0][0], results[6][0], results[1][0], results[2][0], results[3][0], results[4][0], results[5][0]]
    pie = Pie("内衣罩杯", width=1300, height=620)
    pie.add("", attr, v1, is_label_show=True)
    pie.render('size.html')
    print('success')

def showColor():
    results = common.queryData("""select count(*) from bra where bra_color like '%肤%' 
            union all select count(*) from bra where bra_color like '%灰%' 
            union all select count(*) from bra where bra_color like '%黑%' 
            union all select count(*) from bra where bra_color like '%蓝%' 
            union all select count(*) from bra where bra_color like '%粉%' 
            union all select count(*) from bra where bra_color like '%红%' 
            union all select count(*) from bra where bra_color like '%紫%'  
            union all select count(*) from bra where bra_color like '%绿%' 
            union all select count(*) from bra where bra_color like '%白%' 
            union all select count(*) from bra where bra_color like '%褐%' 
            union all select count(*) from bra where bra_color like '%黄%' """)  # 获取每个罩杯数量
    attr = ["肤色", '灰色', "黑色", "蓝色", "粉色", "红色", "紫色", '绿色', "白色", "褐色", "黄色"]
    v1 = [results[0][0], results[1][0], results[2][0], results[3][0], results[4][0], results[5][0], results[6][0],
          results[7][0], results[8][0], results[9][0], results[10][0]]
    pieColor = Pie("内衣颜色", width=1300, height=620)
    pieColor.add("", attr, v1, is_label_show=True)
    pieColor.render('color.html')
    print('success')

def showSentiment():
    results = common.queryData("""select count(*), sentiment from bra where `comment` not like '此用户没有填写评论%' and sentiment != 0 GROUP BY sentiment""")  #
    attr = []
    v1 = []
    for result in results:
        sentiment = str(result[1])
        attr.append(sentiment)
        v1.append(result[0])


    bar = Bar("坐标轴标签旋转示例")
    bar.add("", attr, v1, xaxis_interval=5, xaxis_rotate=0, yaxis_rotate=0)
    bar.render()


def showComment():
    results = common.queryData("""select comment from bra where `comment` not like '此用户没有填写评论%' LIMIT 1000 """)  # 获取评论
    text = ""
    for result in results:
        text = text + result[0]

    common.wordCloudShow(text, "..\\tmall\\wechat1.png", "..\\tmall\\wechat_cloud1.png", "white", 50, 1000, 860)

def fixData():
    results = common.queryData("""select bra_id, comment from bra where `comment` not like '此用户没有填写评论%' and sentiment = 0 """)  # 获取评论
    for result in results:
        sen = common.showSentiments(result[1])
        "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        common.insertData("update bra set sentiment = '%f' where bra_id = '%s' " % (sen, result[0]))

if __name__ == '__main__':
    showSentiment()





