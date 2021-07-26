from selenium import webdriver

class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.drivert.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

#   cleanmgr.exe  清理磁盘垃圾
#   https://www.cnblogs.com/aichixigua12/p/13236092.html 可以学习这个，减少自己封装数据，这种可以用于以后高级自动化
#   adb shell dumpspys activity top（app信息）
#   adb logcat l grep -i displayed（app入口）
#   adb shell dumpsys window windows | findstr "Current"（获取package activity信息）
#   adb shell am start -n package/launch activity（App启动方法）
#   adb devices        (获取设备的名字)：   deviceName
#   元素定位（uiautomatorviewer）在JDK中tools中uiautomatorviewer打开


# pytest +(**.py) --alluredir=./自定义包名    开启一个目录：allure serve ./自定义包名


# 自动遍历 android monkey
'''adb shell monkey -p com.xueqiu.android 100   对指定包'''
# adb shell monkey -p com.xueqiu.android -s 20 80 时间种子（跟着上一次测试步骤）
# adb shell monkey -p com.xueqiu.android -vv-s 20 80 详细日志
# adb shell monkey -p com.xueqiu.android --throttle 5000 100 时间延迟
# adb shell monkey -p com.xueqiu.android --pct-touch 10 1000  事件百分比
'''--pct-touch:触摸事件，比如点击    --pct-trackball:轨迹事件，比如移动+点击，曲线滑动
           --pct-motion:动作事件，比如滑动（直线）   --pct-majornav:只要导航事件，比如回退按键，菜单按键'''

# java -jar appcrawler-2.4.0-jar-with-dependencies.jar