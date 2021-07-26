from time import sleep

from appium import webdriver


class TestAppiumWeb:
    '''测试手机自带的浏览器中的网页'''
    def setup(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',
            'browserName': 'Browser',
            'noReset': True,
            'deviceName': '127.0.0.1:7555',
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()
    def test_web(self):
        self.driver.get('http://m.baidu.com')
        sleep(5)