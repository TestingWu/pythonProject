from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBase:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_base(self):
        self.driver.get('https://testerhome.com/')
        self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/li[3]/a').click()
        '''显示等待'''
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')) >= 1
        #
        # WebDriverWait(self.driver, 10).until(wait)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')))
        self.driver.find_element_by_xpath('//*[@id="hot_teams"]/div[2]/div/div[1]/div/div[2]/div[1]/a').click()
