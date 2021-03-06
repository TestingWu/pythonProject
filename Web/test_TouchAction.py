from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get('http://www.baidu.com')
        el = self.driver.find_element(By.XPATH, '//*[@id="kw"]')
        el.send_keys('selenium测试')
        send_sou = self.driver.find_element(By.XPATH, '//*[@id="su"]')
        action = TouchActions(self.driver)
        action.tap(send_sou).perform()
        action.scroll_from_element(el, 0, 10000).perform()  # 滑动
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(3)