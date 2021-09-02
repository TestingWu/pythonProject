import yaml
from appium import webdriver

from UI.page.base_page import BasePage
from UI.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = 'com.xueqiu.android.common.GeneralNoticeActivity'
    def start(self):
        if self._driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0.1'
            # desired_caps['deviceName'] = yaml.safe_load(open('./configuration.yaml'))['desired_caps']['deviceName']
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在那个页面
            desired_caps['noReset'] = 'true'  # 启动app时不要清除app里的原有的数据
            desired_caps['skipDeviceInitialization'] = 'true'  # Appium启动时跳过初始化设置
            desired_caps['unicodeKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式(缺一不可)
            desired_caps['resetKeyBoard'] = 'true'  # 默认的英文模式可以设置为中文模式
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(20)
        return self
    def main(self) -> Main:
        return Main(self._driver)