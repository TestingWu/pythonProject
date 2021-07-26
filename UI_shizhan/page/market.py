from selenium.webdriver.common.by import By

from UI_shizhan.page.base_page import BasePage
from UI_shizhan.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]').click()
        self.steps('../page/search.yaml')
        return Search(self._driver)