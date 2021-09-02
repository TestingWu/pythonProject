import inspect
import json
import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from UI_shizhan.page.wrapper import handle_black


class BasePage:
    # 弹窗 处理的定位列表
    _params = {}
    # _black_list = [
    #     (By.XPATH, '//*[@text="确认"]'),
    #     (By.XPATH, '//*[@text="下次再说"]'),
    #     (By.XPATH, '//*[@text="确认"]'),
    # ]
    # _max_num = 3
    # _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def screenshot(self, name):  # 截图
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

        # try:
        #     element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
        #         locator, value)
        #     # if isinstance(locator, tuple):
        #     #     element = self._driver.find_element(*locator)
        #     # else:
        #     #     element = self._driver.find_element(locator, value)
        #     # 找到之前 _error_num
        #     self._error_num = 0
        #     # 隐式等待回复原来的等待
        #     self._driver.implicitly_wait(10)
        #     return element
        # except Exception as e:
        #     # 出现异常， 将隐式等待设置小一点，快速的处理弹框
        #     self._driver.implicitly_wait(1)
        #     # 判断异常处理次数
        #     if self._error_num > self._max_num:
        #         raise e
        #     self._error_num += 1
        #     # 处理黑名单里面的弹框
        #     for ele in self._black_list:
        #         logging.info(ele)
        #         elelist = self._driver.find_elements(*ele)
        #         if len(elelist) > 0:
        #             elelist[0].click()
        #             # 处理完弹框，再将去查找目标元素
        #             return self.find(locator, value)
        #     raise e

    @handle_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        if isinstance(locator, tuple):
            element_text = self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text
        # try:
        #     element_text = self._driver.find_element(*locator).text if isinstance(locator,
        #                                                                           tuple) else self._driver.find_element(
        #         locator, value).text
        #     self._error_num = 0
        #     self._driver.implicitly_wait(10)
        #     return element_text
        # except Exception as e:
        #     self._driver.implicitly_wait(1)
        #     if self._error_num > self._max_num:
        #         raise e
        #     self._error_num += 1
        #     for ele in self._black_list:
        #         elelist = self._driver.find_elements(*ele)
        #         if len(elelist) > 0:
        #             elelist[0].click()
        #             return self.find_and_get_text(locator, value)
        #     raise e

    def steps(self, path):
        with open(path, encoding='utf-8') as f:

            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]

        '''序列替换'''
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f'${{{key}}}', value)  # ${+key+}
        steps = json.loads(raw)

        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if 'click' == action:
                    self.find(step['by'], step['locator']).click()
                if 'send' == action:
                    self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len > 0' == action:
                    eles = self.finds(step['by'], step['locator'])
                    return len(eles) > 0
