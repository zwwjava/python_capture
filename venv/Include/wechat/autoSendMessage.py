# -*- coding:utf-8 -*-
# Author: zww

import itchat
import re
# jieba分词
import jieba
# wordcloud词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image

class WeChat():

    KEY = '71f9d9d2dd364ad8b28bd56527470176'

    def login(self):
        itchat.auto_login(hotReload=True)  # 登录，会下载二维码给手机扫描登录，hotReload设置为True表示以后自动登录
        itchat.run()  # 让itchat一直运行

    # 回复信息
    @itchat.msg_register(itchat.content.TEXT)
    def tuling_robot(self, msg):
        # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
        defaultReply = '不想说话了！'
        # 如果图灵Key出现问题，那么reply将会是None
        reply = self.getget_response(msg['Text'])
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
        return reply or defaultReply

    def get_response(self, msg):
        # 构造了要发送给服务器的数据
        apiUrl = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': KEY,
            'info': msg,
            'userid': 'wechat-robot',
        }
        try:
            r = requests.post(apiUrl, data=data).json()
            return r.get('text')
        # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
        # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        except:
            # 将会返回一个None
            return

    def getFriend(self, name):
        friends = itchat.search_friends(name = name)  # 获取微信好友列表，如果设置update=True将从服务器刷新列表
        userName = friends[0]['UserName']
        return userName

    def getFriends(self):
        friends = itchat.get_friends(update=True)[0:]
        return friends

    def ratio(self, friends):
        # 初始化计数器，有男有女，当然，有些人是不填的
        male = female = other = 0

        # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
        # 1表示男性，2女性
        for i in friends[1:]:
            sex = i["Sex"]
            if sex == 1:
                male += 1
            elif sex == 2:
                female += 1
            else:
                other += 1

        # 总数算上，好计算比例啊～
        total = len(friends[1:])
        # 好了，打印结果
        print(u"男性好友：%.2f%%" % (float(male) / total * 100))
        print(u"女性好友：%.2f%%" % (float(female) / total * 100))
        print(u"其他：%.2f%%" % (float(other) / total * 100))

    def signature(self, friends):
        tList = []
        for i in friends:
            signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
            rep = re.compile("1f\d.+")
            signature = rep.sub("", signature)
            tList.append(signature)
        text = "".join(tList)
        wordlist_jieba = jieba.cut(text, cut_all=True)
        wl_space_split = " ".join(wordlist_jieba)

        d = os.path.dirname(__file__)
        alice_coloring = np.array(Image.open(os.path.join(d, "wechat1.png")))
        my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                                 max_font_size=50, random_state=42,width=1000,height=860,
                                 font_path='C:/Windows/Fonts/STFANGSO.ttf').generate(wl_space_split)

        image_colors = ImageColorGenerator(alice_coloring)
        plt.imshow(my_wordcloud.recolor(color_func=image_colors))
        plt.imshow(my_wordcloud)
        plt.axis("off")
        plt.show()
        my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))

        # 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
        # my_wordcloud = WordCloud(background_color="white", max_words=2000,
        #                          max_font_size=40, random_state=42,
        #                          font_path='C:/Windows/Fonts/STFANGSO.ttf').generate(wl_space_split)
        # plt.imshow(my_wordcloud)
        # plt.axis("off")
        # plt.show()

    def sendMessage(self, message, name):
        itchat.send(message, toUserName=name)

if __name__ == "__main__":
    wechat = WeChat()
    wechat.login()
    # item = wechat.getFriend('阿勇')
    # wechat.sendMessage("我是zww的python微信助手", item)
    # friends = wechat.getFriends()
    # wechat.signature(friends)

