# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 2:21 PM
# @Author   :Huiming Shi
from common.basePage import BasePage

class HomePage(BasePage):
    def checkSearchFieldExists(self):
        # 断言是否存在搜索框
        self.base_assert_exists('搜索标识',(0.316, -0.869),"断言是否存在搜索框")

    def inputTextSearch(self):
        # 搜索框输入文本内容
        self.base_text('LOL')

    def clickSearchField(self):
        # 点击搜索框
        self.wait_and_touch('搜索框', (0.156, -0.869))
