from time import sleep

from Web.Base import Base


class TestWindows(Base):
    def test_windows(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="s-top-loginbtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        '''切换页面'''
        print(self.driver.current_window_handle)  # 打印当前得窗口
        print(self.driver.window_handles)  # 打印所以得窗口
        windows = self.driver.window_handles

        self.driver.switch_to_window(windows[-1])

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys('12345678911')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__password"]').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__isAgree"]').click()

        self.driver.switch_to_window(windows[0])

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys('123456')

        sleep(5)