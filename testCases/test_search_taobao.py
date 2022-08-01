# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 3:02 PM
# @Author   :Huiming Shi
import os
import allure
import pytest
from libs.homePage import HomePage
from libs.keyeventLib import KeyeventLib
from libs.searchResult import SearchResult
from libs.start import Start
from utils.get_absolute_path import reports_path

@allure.epic('淘宝项目')
@allure.feature('淘宝app测试')
class Test_search_taobao(object):
    @allure.story('淘宝查询功能')
    @allure.title('查询结果正确')
    def test_search_taobao(self):
        with allure.step('1-打开淘宝'):
            start = Start()
            start.clickQKWD()
            start.base_sleep(2)
            start.startTaobao()
        with allure.step('2-进行搜索'):
            homePage = HomePage()
            homePage.checkSearchFieldExists()
            homePage.clickSearchField()
            homePage.inputTextSearch()
        with allure.step('3-断言'):
            searchResult = SearchResult()
            searchResult.checkSearchResult()
        with allure.step('4-环境恢复'):
            keyeventLib = KeyeventLib()
            for i in range(4):
                keyeventLib.keycode_back()
                keyeventLib.base_sleep(1)
            keyeventLib.keycode_home()

if __name__ == '__main__':
    pytest.main(['-sv',__file__,'--alluredir', reports_path,'--clean-alluredir'])
    os.system(f'allure serve  {reports_path}')