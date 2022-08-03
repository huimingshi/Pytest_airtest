# _*_ coding: utf-8 _*_ #
# @Time     :8/3/2022 11:21 AM
# @Author   :Huiming Shi

import pytest
from libs.keyeventLib import KeyeventLib

@pytest.fixture(scope='function',autouse=False)
def back_to_home():
    """
    返回到主页
    :return:
    """
    yield
    keyeventLib = KeyeventLib()
    for i in range(4):
        keyeventLib.keycode_back()
        keyeventLib.base_sleep(1)
    keyeventLib.keycode_home()