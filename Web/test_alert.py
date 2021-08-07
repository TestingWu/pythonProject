from time import sleep
from selenium.webdriver import ActionChains
from Web.Base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')

        drag = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        drop = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        sleep(3)
        print('点击alert确认')
        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()
        sleep(3)