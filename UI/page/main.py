from selenium.webdriver.common.by import By

from UI.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'com.baidu.searchbox:id/baidu_searchbox').click()
        self.steps('../page/main.yaml')
    def goto_windows(self):
        self._driver.find_element_by_android_uiautomator('new UiSelector().resourceId("android.widget.FrameLayout").index[2]').click()
        self.find(By.ID, 'com.baidu.searchbox:id/baidu_searchbox').click()
