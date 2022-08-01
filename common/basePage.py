# _*_ coding: utf-8 _*_ #
# @Time     :8/1/2022 1:39 PM
# @Author   :Huiming Shi

import allure
from airtest.core.api import *
from airtest.report.report import *
from config.projectConf import RESOLUTION, SYSTEM_TYPE, DEVICE_ID, ADBHOST, ADBPOST
from utils.get_absolute_path import pictures_path, screenShots_path


class BasePage(object):
    def __init__(self):
        """
        Auto setup running env and try connect android device if not device connected.
        """
        auto_setup(__file__, devices=[f"{SYSTEM_TYPE}://{ADBHOST}:{ADBPOST}/{DEVICE_ID}"])

    def base_sleep(self,sleepTime):
        """
        等待
        :param sleepTime:   等待时长，单位：s
        :return:
        """
        sleep(sleepTime)

    def base_keyevent(self,witchKeyevent,action=None):
        """
        keyevent 控制按键输入
        :param witchKeyevent:  keyevent
        :param action:  按键描述
        :return:
        """
        try:
            keyevent(witchKeyevent)
        except Exception:
            self.base_snapshot(reason=action)

    def base_touch(self,witchPicture=None,position=None,action=None):
        """
        touch功能
        :param witchPicture:  哪张图片
        :param position:  中心位置
        :param action:  行为描述
        :return:
        """
        try:
            touch(Template(os.path.join(pictures_path, f'{witchPicture}.png'), record_pos=position, resolution=RESOLUTION))
        except Exception:
            self.base_snapshot(reason=action)

    def base_wait(self,witchPicture=None,position=None,action=None):
        """
        等待元素可见功能
        :param witchPicture:  哪张图片
        :param position:  中心位置
        :param action:  行为描述
        :return:
        """
        try:
            wait(Template(os.path.join(pictures_path,  f'{witchPicture}.png'), record_pos=position,resolution=RESOLUTION))
        except Exception:
            self.base_snapshot(reason=action)

    def wait_and_touch(self,witchPicture=None,position=None,action=None):
        """
        等待元素可见后进行touch功能
        :param witchPicture:  哪张图片
        :param position:  中心位置
        :param action:  行为描述
        :return:
        """
        try:
            touch(wait(Template(os.path.join(pictures_path, f'{witchPicture}.png'), record_pos=position, resolution=RESOLUTION)))
        except Exception:
            self.base_snapshot(reason=action)

    def base_text(self,content=None):
        """
        输入text功能
        :param content:  输入的文本内容
        :return:
        """
        try:
            text(content)
        except Exception:
            self.base_snapshot(reason='输入文本')

    def base_snapshot(self,reason=None):
        """
        截图功能
        :param reason: 理由
        :return:
        """
        current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        snapshot(f'{screenShots_path}{reason}{current_time}.png')
        file_png = open(f'{screenShots_path}{reason}{current_time}.png', mode='rb').read()
        allure.attach(file_png, f'{screenShots_path}{reason}{current_time}.png', allure.attachment_type.PNG)
        raise Exception(f'{reason}')

    def base_assert_equal(self,witchPicture=None,position=None,action=None):
        """
        断言是否相等
        :param witchPicture:  哪张图片
        :param position:  中心位置
        :param action:  行为描述
        :return:
        """
        try:
            assert_equal(False, exists(Template(os.path.join(pictures_path,  f'{witchPicture}.png'), record_pos=position,resolution=RESOLUTION)), action)
        except Exception:
            self.base_snapshot(reason=action)

    def base_assert_exists(self,witchPicture=None,position=None,action=None):
        """
        断言元素是否存在
        :param witchPicture:  哪张图片
        :param position:  中心位置
        :param action:  行为描述
        :return:
        """
        try:
            assert_exists(Template(os.path.join(pictures_path,  f'{witchPicture}.png'), record_pos=position,resolution=RESOLUTION), action)
        except Exception:
            self.base_snapshot(reason=action)