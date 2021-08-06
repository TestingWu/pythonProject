from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_actionchains(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        element_doubleclick = self.driver.find_element(By.XPATH, '/html/body/form/input[2]')  # 双击
        element_rightclick = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')  # 右键
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        sleep(3)
        action.perform()
        sleep(4)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)  # 移动到某个元素
        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        drop_element = self.driver.find_element(By.XPATH, '/html/body/div[3]')
        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element, drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()  # 把元素拖拽另一个元素上
        sleep(5)

    def test_keys(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        self.driver.find_element(By.XPATH, '/html/body/label[1]/input').click()
        action = ActionChains(self.driver)  # 模拟键盘操作
        action.send_keys('wunongyun').pause(2)
        action.send_keys(Keys.SPACE).pause(2)
        action.send_keys('666').pause(2)
        action.send_keys(Keys.BACK_SPACE).pause(2).perform()
        sleep(5)