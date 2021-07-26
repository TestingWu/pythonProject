from selenium.webdriver.common.by import By
from time import sleep

from selenium_wework_main.page.base_page import BasePage


class Address(BasePage):
    def address(self):
        sleep(2)
        self.find(By.ID, 'username').send_keys('大表哥')
        self.find(By.ID, 'memberAdd_acctid').send_keys('123456')
        self.find(By.ID, 'memberAdd_phone').send_keys('15454578454')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    # def update_page(self):
    #     content: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
    #     #  对1/10 进行切割
    #     return [int(x) for x in content.split('/', 1)]

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
        list = [element.get_attribute('title') for element in elements]
        return list
        # self.wait_for(By.CSS_SELECTOR, './ww_checkbox')
        # cur_page, total_page = self.update_page()
        # while True:
        #     elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        #     for element in elements:
        #         if value == element.get_attribute('title'):
        #             return True
        #     cur_page = self.update_page()[0]
        #     if cur_page == total_page:
        #         return False
        #     self.find(By.CSS_SELECTOR, '.js_next_page').click()
            # list = [element.get_attribute('title') for element in elements]
            # list = []
            # for element in elements:
            #     list.append(element.get_attribute('title'))
            # return list
