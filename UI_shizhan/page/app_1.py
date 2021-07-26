from appium import webdriver

from UI_shizhan.page.base_page import BasePage
from UI_shizhan.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = dict()
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0.1'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = 'com.xueqiu.android.main.view.MainActivity'
            # caps['dontStopAppOnReset'] = 'true'  # 页面停留在那个页面
            caps['noReset'] = 'true'  # 启动app时不要清除app里的原有的数据
            caps['skipDeviceInitialization'] = True  # Appium启动时跳过初始化设置
            caps['skipServerInstallation'] = True
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
