# -*- coding:utf-8 -*-
# Author: zww
# 英雄联盟自动刷人机
import pyautogui as pag
import time
import random

def getRGBByPosition():
    time.sleep(5)
    img = pag.screenshot()
    print(img.getpixel(pag.position()))

def getRGB(x, y):
    img = pag.screenshot()
    print(img.getpixel((x, y)))

def getPositon():
    time.sleep(5)
    print(pag.position())

if __name__ == '__main__':
    screenWidth, screenHeight = pag.size()
    # 暂停10秒 进入LOL界面
    time.sleep(10)
    # print(str(screenWidth) + ' ;' + str(screenHeight))q
    while True:
        randdomWidth = random.randint(200, screenWidth - 200)
        randomHeight = random.randint(200, screenHeight - 200)
        randomSleep = random.randint(50, 200)
        randomDuration = random.randint(3, 10)
        print(str(randdomWidth) + ' ;' + str(randomHeight) + ' ;' + str(randomSleep))
        pag.moveTo(randdomWidth, randomHeight, randomDuration/10)
        pag.click(button='right')
        time.sleep(randomDuration)
        pag.typewrite('q')
        time.sleep(randomSleep)