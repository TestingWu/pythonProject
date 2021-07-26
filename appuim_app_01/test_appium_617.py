import pytest
from appium import webdriver
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium:
    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.baidu.searchbox'
        desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
        # desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在那个页面
        desired_caps['noReset'] = 'true'  # 启动app时不要清除app里的原有的数据
        desired_caps['skipDeviceInitialization'] = 'true'  # Appium启动时跳过初始化设置
        desired_caps['unicodeKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式(缺一不可)
        desired_caps['resetKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.back()  # 返回到上一个页面
        self.driver.quit()
    @pytest.mark.skip
    def test_appium(self):
        self.driver.find_element_by_id('com.baidu.searchbox:id/search_box_text_1').click()
        sleep(3)
        self.driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput').send_keys('阿里巴巴')


        '''显示等待,可以判断该元素是否是可点击，如果可点击，那就点击该元素'''
        locator = (MobileBy.ID, 'com.baidu.searchbox:id/id_sug_item_basic_content')
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        self.driver.find_element(*locator).click()



        sleep(3)
    def test_arrt(self):
        element = self.driver.find_element_by_id('com.baidu.searchbox:id/search_box_text_1')
        search_enabled = element.is_enabled()  # 判断是否可用
        # element.is_selected()   # 判断是否被选中
        # element.is_displayed()  # 判断是否可见
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id('com.baidu.searchbox:id/SearchTextInput').send_keys('阿里巴巴')
    def test_touchaction(self):
        action = TouchAction(self.driver)
        window_rect =self.driver.get_window_rect()  # 获取当前页面的屏幕宽度和高度
        width = window_rect['width']
        height = window_rect['height']
        x1 =int(width/2)
        y_start = int(height*4/5)
        y_start1 = int(height*1/5)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_start1).release().perform()



if __name__ == '__main__':
    pytest.main()
