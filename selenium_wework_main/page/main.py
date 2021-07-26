from selenium.webdriver.common.by import By
from selenium_wework_main.page.address import Address
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    def goto_add_member(self):
        self.find(By.ID, 'menu_contacts').click()
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        self.wait_for(locator)
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        return Address(self._driver)