# encoding: utf-8
# author zww

from Include.commons.common import Common
import jieba
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image

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

def showComment():
    results = common.queryData("""select comment from bra where `comment` not like '此用户没有填写评论%' LIMIT 1000 """)  # 获取评论
    text = ""
    for result in results:
        text = text + result[0]
    wordlist_jieba = jieba.cut(text, cut_all=True)
    wl_space_split = " ".join(wordlist_jieba)

    d = os.path.dirname(__file__)
    alice_coloring = np.array(Image.open(os.path.join(d, "wechat1.png")))
    my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                             max_font_size=50, random_state=42, width=1000, height=860,
                             font_path='C:/Windows/Fonts/STFANGSO.ttf').generate(wl_space_split)

    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    my_wordcloud.to_file(os.path.join(d, "wechat_cloud1.png"))

if __name__ == '__main__':
    showComment()




