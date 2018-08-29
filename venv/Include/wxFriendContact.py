# encoding: utf-8

import itchat


def get_friends():
    friends = itchat.get_friends(update=True)  # 获取微信好友列表，如果设置update=True将从服务器刷新列表
    for i in friends:
        print(i)


def main():
    itchat.auto_login(hotReload=True)  # 登录，会下载二维码给手机扫描登录，hotReload设置为True表示以后自动登录
    get_friends()
    itchat.run()  # 让itchat一直运行


if __name__ == "__main__":
    main()