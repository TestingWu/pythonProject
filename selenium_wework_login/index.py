'''pageobject的原理：封装'''
from selenium_wework_login.login import Login
from selenium_wework_login.register import Register
from selenium import webdriver

class Index():
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)
        self._driver.get('https://work.weixin.qq.com/')
    def goto_login(self):
        #click login
        self._driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return Login(self._driver)
    def goto_register(self):
        #click register
        self._driver.find_element_by_xpath('//*[@id="tmp"]/div[1]/a').click()
        return Register(self._driver)
