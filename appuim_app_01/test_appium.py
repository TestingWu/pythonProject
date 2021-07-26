from appium import webdriver
from time import sleep
desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.baidu.searchbox'
desired_caps['appActivity'] = 'com.baidu.searchbox.MainActivity'
desired_caps['dontStopAppOnReset'] = 'true'  # 页面停留在那个页面
desired_caps['noReset'] = 'true'  # 启动app时不要清除app里的原有的数据
desired_caps['skipDeviceInitialization'] = 'true'  # Appium启动时跳过初始化设置
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.baidu.searchbox:id/tab_indi_title').click()
sleep(6)
driver.back()  # 返回到上一个页面
driver.quit()