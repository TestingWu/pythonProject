from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.register import Register


class Login():
    def __init__(self, driver: WebDriver):
        self._driver = driver
    def scanf(self):
        pass
    def goto_register(self):
        #click register
        self._driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self._driver)