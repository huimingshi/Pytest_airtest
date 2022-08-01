# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 3:47 PM
# @Author   :Huiming Shi
from common.basePage import BasePage

class KeyeventLib(BasePage):
    def keycode_home(self):
        # HOME键对应keyevent
        self.base_keyevent('3')

    def keycode_back(self):
        # 返回键对应keyevent
        self.base_keyevent('4')