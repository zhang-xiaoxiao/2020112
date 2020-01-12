#coding=utf-8
import time
import unittest

from public.common import mytest
from public.pages import LoginPage
from ddt import ddt,data,unpack
from loguru import logger
from public.common.datainfo import get_test_case_data, data_info
from public.common.get_img import screenshot_about_case
# from BeautifulReport import BeautifulReport


@ddt
class TestLogin(mytest.MyTest):
    """登录模块"""

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_01_login'))
    # @unittest.skipIf(True, "原因")
    def test_01_login(self, data):
        """正常登录"""
        test_data = data['data']
        test_assert = data['assertion']
        # login = LoginPage.Login(self.dr)
        # ele = login.login(test_data['username'],test_data['pw'])
        # login.exist_loading()
        # username = ele.get_name()
        # url = ele.get_url()
        # self.assertIn(url,test_assert['title'])
        # self.assertIn(username, test_assert['username'])
        login = LoginPage.Login(self.dr)
        # login.input_account(test_data['username'])
        # login.input_pw(test_data['pw'])
        # login.click_box()
        work = login.login(test_data['username'], test_data['pw'])
        name = work.get_name()
        url = work.get_url()
        self.assertIn(test_assert['username'], name)
        self.assertIn(test_assert['title'], url)

    @screenshot_about_case
    @data(*get_test_case_data(data_info, 'test_02_login'))
    def test_02_login(self, data):
        """错误密码登录"""
        test_data = data['data']
        test_assert = data['assertion']
        # login = LoginPage.Login(self.dr)
        # ele = login.login(test_data['username'],test_data['pw'])
        # login.exist_loading()
        # username = ele.get_name()
        # url = ele.get_url()
        # self.assertIn(url,test_assert['title'])
        # self.assertIn(username, test_assert['username'])
        login = LoginPage.Login(self.dr)
        login.input_account(test_data['username'])
        login.input_pw(test_data['pw'])
        login.click_box()
        work = login.click_login_btn()
        error_text = login.get_error_text()
        url = login.get_url()
        self.assertIn(test_assert['text'], error_text)
        self.assertIn(test_assert['url'], url)


