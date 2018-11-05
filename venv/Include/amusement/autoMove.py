# -*- coding:utf-8 -*-
# Author: zww
# 英雄联盟自动刷人机
import pyautogui as pag
import time
import random

screenWidth, screenHeight = pag.size()
#暂停10秒 进入LOL界面
time.sleep(5)
# print(str(screenWidth) + ' ;' + str(screenHeight))
while True:
    randdomWidth = random.randint(200, screenWidth-200)
    randomHeight = random.randint(200, screenHeight-200)
    print(str(randdomWidth) + ' ;' + str(randomHeight))
    pag.moveTo(randdomWidth, randomHeight, 0.5)
    # pag.click(button='right')
    pag.typewrite('q')
    time.sleep(5)

# print(pag.position())