import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
'''第一步：首先先进入cmd输入chrome --remote-debugging-port=9222，进行企业微信登录，然后对登录后的微信进行cookies的储存，
方便下次登录是可以处于免登录状态'''
class TestBai():
    def setup(self):
        '''设置自动化登录浏览器（调试端口）  chrome --remote-debugging-port=9222
        在已有的页面进行继续操作'''
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    def test_bai(self):
        # print(self.driver.get_cookies())#获取到cookies的值
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open('cookies')
        db['cookie'] = self.driver.get_cookies()#类似于一个数据库的功能，把信息缓存到cookies文件中
        # cookies = db['cookie']
        # for cookie in cookies:
        #     if 'expiry' in cookie.keys():
        #         cookie.pop('expiry')
        #     self.driver.add_cookie(cookie)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # sleep(3)
        # db.close()
'''第二步，如下图所示进行操作，就可以免登录：使用cookies登录企业微信'''
class TestBai():
    def setup(self):
        '''设置自动化登录浏览器（调试端口）  chrome --remote-debugging-port=9222
        在已有的页面进行继续操作'''
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    def test_bai(self):
        # print(self.driver.get_cookies())#获取到cookies的值
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        db = shelve.open('cookies')
        # db['cookie'] = self.driver.get_cookies()#类似于一个数据库的功能，把信息缓存到cookies文件中
        cookies = db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        db.close()