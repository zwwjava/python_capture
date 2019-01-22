# -*- coding:utf-8 -*-
# Author: zww
from Include.commons.common import Common

common = Common()
MOBILE = '13767222921'
class EvilSendMES():
    def sendOne(self, mobile):
        url = "http://bbs.mydigit.cn/registe.php"
        data = {
            "action":"auth",
            "setp":"1",
            "mobile":mobile
        }
        response = common.post(url,data)
        print(response)

    def sendOne(self, mobile):
        url = "http://bbs.mydigit.cn/registe.php"
        data = {
            "action":"auth",
            "setp":"1",
            "mobile":mobile
        }
        response = common.post(url,data)
        print(response)


if __name__ == '__main__':
    evil = EvilSendMES()
    evil.sendOne(MOBILE)