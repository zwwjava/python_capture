from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

class XueXiUtils():

    #打开文章阅读
    def xuexiwenzhang(self, driver):
        driver.get('https://www.xuexi.cn/')
        sleep(2)
        zhongyaoLink = driver.find_elements_by_class_name("_3wnLIRcEni99IWb4rSpguK")
        zhongyaoLink[0].click()
        sleep(121)
        zhongyaoLink[1].click()
        sleep(122)
        zhongyaoLink[2].click()
        sleep(123)
        zhongyaoLink[3].click()
        sleep(124)
        zhongyaoLink[4].click()
        sleep(125)
        zhongyaoLink[5].click()
        sleep(126)


    #打开文章阅读
    def clostTab(self, driver):
        # 获取所有窗口句柄
        all_h = driver.window_handles
        print(all_h)
        # 切换最后窗口句柄
        driver.switch_to.window(all_h[1])
        driver.close()
        driver.switch_to.window(all_h[2])
        driver.close()
        driver.switch_to.window(all_h[3])
        driver.close()
        driver.switch_to.window(all_h[4])
        driver.close()
        driver.switch_to.window(all_h[5])
        driver.close()
        driver.switch_to.window(all_h[6])
        driver.close()
        # 切换第一个窗口句柄
        driver.switch_to.window(all_h[0])


    #打开视频阅读
    def xuexishipin(self, driver):
        driver.get('https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
        sleep(2)
        zhongyaoLink = driver.find_elements_by_css_selector('.Iuu474S1L6y5p7yalKQbW.grid-cell')
        zhongyaoLink[0].click()
        sleep(181)
        zhongyaoLink[1].click()
        sleep(182)
        zhongyaoLink[2].click()
        sleep(183)
        zhongyaoLink[3].click()
        sleep(184)
        zhongyaoLink[4].click()
        sleep(185)
        zhongyaoLink[5].click()
        sleep(186)

    def xuexishipinT(self, driver):
        driver.get('https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
        sleep(2)
        zhongyaoLink = driver.find_elements_by_css_selector('.Iuu474S1L6y5p7yalKQbW.grid-cell')
        zhongyaoLink[0].click()
        sleep(181)
        zhongyaoLink[1].click()
        sleep(182)
        zhongyaoLink[2].click()
        sleep(183)
        zhongyaoLink[3].click()
        sleep(184)
        zhongyaoLink[4].click()
        sleep(185)
        zhongyaoLink[5].click()
        sleep(186)


if __name__ == '__main__':

    dataUtil = XueXiUtils()
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(r'D:\SoftWare\Python\chromedriver.exe', 0, option)
    #首页登录
    driver.get('https://pc.xuexi.cn/points/my-study.html')
    sleep(36000)
    while true:
        dataUtil.xuexiwenzhang(driver)
        dataUtil.clostTab(driver)
        dataUtil.xuexishipin(driver)
        dataUtil.clostTab(driver)
        sleep(86400)