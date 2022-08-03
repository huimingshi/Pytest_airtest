# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 3:40 PM
# @Author   :Huiming Shi
from common.basePage import BasePage

class SearchResult(BasePage):
    def checkSearchResult(self):
        # 断言查询结果
        self.base_assert_exists('LOL',(-0.305, -0.979),"断言查询结果")