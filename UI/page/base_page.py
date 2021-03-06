import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _black_list = [(By.ID, 'com.xueqiu.android:id/iv_action_back')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    '''在进行自动化操作的时候  有些时候会显示弹框，就会影响自动化操作，因此就要进行对弹框
    的异常捕获'''

    def find(self, locator, value):
        # return self._driver.find_element(locator, value)
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
                return self.find(locator, value)

    def steps(self, path):  # 完成对yaml的解析
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if 'by' in step.keys():
                element = self.find(step['by'], step['locator'])
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    element.click()
