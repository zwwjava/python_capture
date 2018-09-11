# -*- coding:utf-8 -*-
# Author: zww
import itchat
import requests

KEY = '71f9d9d2dd364ad8b28bd56527470176'
# 回复信息
@itchat.msg_register(['Text', 'Picture', 'Sharing', 'Video', 'Card'])
def text_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    # defaultReply = '不想说话了！\n来自旺旺的语音助理'
    defaultReply = '不想说话了！' + "*"
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text']) + "*"
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
    return reply or defaultReply

@itchat.msg_register(['Text', 'Picture', 'Video', 'Card'], isGroupChat=True)
def text_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    # defaultReply = '不想说话了！\n来自旺旺的语音助理'
    if msg.User.NickName == "RJJS职业战队" or msg.User.NickName == "阿里A3研发部":
        defaultReply = '不想说话了！' + "*"
        # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text']) + "*"
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        # 有内容一般就是指非空或者非None，你可以用`if a: print('True')`来测试
        return reply or defaultReply

def get_response(msg):
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
    except Exception as e:
        print('插入时发生异常' + e)
        # 将会返回一个None
        return


itchat.auto_login(hotReload=True)  # 登录，会下载二维码给手机扫描登录，hotReload设置为True表示以后自动登录
itchat.run()  # 让itchat一直运行