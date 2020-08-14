from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

scrolljsone = "var q=document.documentElement.scrollTop=500"
scrolljstwo = "var q=document.documentElement.scrollTop=1500"
scrolljs = "var q=document.documentElement.scrollTop=10000"

class XueXiUtils():

    def scrollDow(self, driver):
        # 将滚动条移动到页面的底部
        driver.execute_script(scrolljsone)
        sleep(5)
        driver.execute_script(scrolljstwo)
        sleep(5)
        driver.execute_script(scrolljs)

        #打开文章阅读
    def xuexiwenzhang(self, driver, index):
        driver.get('https://www.xuexi.cn/')
        sleep(4)
        zhongyaoLink = driver.find_elements_by_class_name("_3wnLIRcEni99IWb4rSpguK")
        self.clickLink(zhongyaoLink[index+0], driver, 60)
        self.clickLink(zhongyaoLink[index+1], driver, 60)
        self.clickLink(zhongyaoLink[index+2], driver, 60)
        self.clickLink(zhongyaoLink[index+3], driver, 60)
        self.clickLink(zhongyaoLink[index+4], driver, 60)
        self.clickLink(zhongyaoLink[index+5], driver, 60)
        self.clickLink(zhongyaoLink[index+6], driver, 60)

    def clickLink(self, wenzhang, driver, timeout):
        print('打开一个tab页---------------')
        wenzhang.click()
        sleep(3)
        # 获取所有窗口句柄
        all_h = driver.window_handles
        # 切换最后窗口句柄
        driver.switch_to.window(all_h[1])
        self.scrollDow(driver)
        sleep(timeout)
        driver.close()
        # 切换第一个窗口句柄
        driver.switch_to.window(all_h[0])

    #打开文章阅读
    def clostTab(self, driver):
        # 获取所有窗口句柄
        all_h = driver.window_handles
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

    # 打开文章阅读
    def clostLastTab(self, driver):
        # 获取所有窗口句柄
        all_h = driver.window_handles
        # 切换最后窗口句柄
        driver.switch_to.window(all_h[1])
        driver.close()
        # 切换第一个窗口句柄
        driver.switch_to.window(all_h[0])

    #打开视频阅读
    def xuexishipin(self, driver, index):
        driver.get('https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#1novbsbi47k-5')
        sleep(5)
        zhongyaoLink = driver.find_elements_by_css_selector('.Iuu474S1L6y5p7yalKQbW.grid-cell')
        self.clickLink(zhongyaoLink[index+0], driver, 180)
        self.clickLink(zhongyaoLink[index+1], driver, 180)
        self.clickLink(zhongyaoLink[index+2], driver, 180)
        self.clickLink(zhongyaoLink[index+3], driver, 180)
        self.clickLink(zhongyaoLink[index+4], driver, 180)
        self.clickLink(zhongyaoLink[index+5], driver, 180)
        self.clickLink(zhongyaoLink[index+6], driver, 180)



if __name__ == '__main__':

    dataUtil = XueXiUtils()
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(r'D:\SoftWare\Python\chromedriver.exe', 0, option)
    #首页登录
    driver.get('https://pc.xuexi.cn/points/my-study.html')
    sleep(60)
    index = 7
    while True:
        dataUtil.xuexiwenzhang(driver, index)
        # dataUtil.clostTab(driver)
        dataUtil.xuexishipin(driver, index)
        # dataUtil.clostTab(driver)
        index = index + 7
        sleep(86400)