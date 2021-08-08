from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class Register():
    def __init__(self, driver: WebDriver):  # ：后面的内容是方便后面进行语法提示
        self._driver = driver

    def register(self):
        # send content
        # click element
        sleep(3)
        self._driver.find_element_by_xpath('//*[@id="corp_name"]').send_keys('大表哥')
        sleep(4)
        self._driver.quit()
        return True
