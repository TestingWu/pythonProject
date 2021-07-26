import pytest
from appium import webdriver
from hamcrest import *


class TestGetAtt:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
        desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在那个页面
        desired_caps['noReset'] = 'true'  # 启动app时不要清除app里的原有的数据
        desired_caps['skipDeviceInitialization'] = 'true'  # Appium启动时跳过初始化设置
        desired_caps['unicodeKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式(缺一不可)
        desired_caps['resetKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(100)
    def teardown(self):
        pass
    @pytest.mark.skip
    def test_get_att(self):
        # search_ele = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.baidu.searchbox:id/baidu_searchbox")')
        search_ele = self.driver.find_element_by_id('com.baidu.searchbox:id/search_box_text_1')
        print(search_ele.get_attribute('resource-id'))  # 属性获取
        assert_that(10, equal_to(10))  # 断言
        assert_that(10, close_to(10, 3))  # 7/13之间的数都不会报异常
        assert_that('string that', contains_string('string'))  # 包含
