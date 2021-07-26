import pytest
from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction


class TestAppium:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
        # desired_caps['dontStopAppOnReset'] = True  # 页面停留在那个页面  参数化用例的时候  这个就要关掉
        desired_caps['noReset'] = True  # 启动app时不要清除app里的原有的数据
        desired_caps['skipDeviceInitialization'] = True  # Appium启动时跳过初始化设置
        desired_caps['unicodeKeyBoard'] = True  # 默认的英文模式可以设置为中文模式(缺一不可)
        desired_caps['resetKeyBoard'] = True  # 默认的英文模式可以设置为中文模式
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)

    def teardown(self):
        pass
        # self.driver.back()  # 返回到上一个页面
        # self.driver.quit()
    @pytest.mark.skip
    def test_myinfo(self):
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("未登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.searchbox:id/home_tab_item_textview").text("未登录")').click()
        self.driver.find_element_by_id('com.baidu.searchbox:id/ars').click()
        sleep(5)

    @pytest.mark.skip
    def test_scroll_find_element(self):  # 固定写法
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.baidu.searchbox:id/tab_indi_title").text("小说")').click()  # 多项定位查找
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().'
                                                        'text("太平客栈").instance(0));').click()  # 滚动查找
        sleep(15)
    @pytest.mark.parametrize('searchkey',
                             [('alibaba'),
                              ('xiaomi')]
                             )  #  参数化用例
    def test_search(self,searchkey):
        self.driver.find_element(MobileBy.ID, 'com.baidu.searchbox:id/baidu_searchbox').click()
        self.driver.find_element(MobileBy.ID, 'com.baidu.searchbox:id/input_root').send_keys(searchkey)

        locator = self.driver.find_element(MobileBy.ID, 'com.baidu.searchbox:id/title_groupview')
        locator.click()


if __name__ == '__main__':
    pytest.main()
