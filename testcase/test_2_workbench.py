#coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case
from public.pages.LoginPage import Login


@ddt
class TestWorkbench(mytest.MyAutologinTest):
    """工作台模块"""
    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_loginout'))
    def test_loginout(self, data):
        """退出登陆"""
        test_assert = data['assertion']
        self.workbench.click_center()
        loginpage = self.workbench.close()
        text = loginpage.get_title()
        url = loginpage.get_url()
        self.assertIn(test_assert['text'], text)
        self.assertIn(test_assert['url'], url)

    # @screenshot_about_case
    # def test_luandian(self):
    #     """点击左侧菜单"""
    #     menu = ['客户管理', '平台管理', '机型管理', '权限管理', '协议管理', '设备管理', '用户管理']
    #     for i in menu:
    #         self.workbench.click_menu(i)
    #         time.sleep(3)
