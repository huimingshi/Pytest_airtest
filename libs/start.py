# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 3:05 PM
# @Author   :Huiming Shi
from common.basePage import BasePage

class Start(BasePage):
    def clickQKWD(self):
        # 点击乾坤未定
        self.base_touch('乾坤未定',(0.195, -0.546))

    def startTaobao(self):
        # 启动淘宝app
        self.wait_and_touch('淘宝图标',(0.253, -0.387))