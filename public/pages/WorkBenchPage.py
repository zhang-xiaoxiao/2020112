#coding=utf-8
import time
from public.common import basepage
from public.pages import LoginPage, CustomerPage, TaskLogPage


class WorkBench(basepage.Page):
    """课程库模块"""
    def get_name(self):
        """获取右上角名称"""
        name = self.dr.get_text("css->div.flex.flex--align-center.el-dropdown-selfdefine")
        return name

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def close(self):
        """点击退出按钮"""
        self.dr.click("xpath->//li[contains(text(), '退出')]")
        time.sleep(0.3)
        return LoginPage.Login(self.dr)

    def click_out(self):
        """确定退出"""
        self.dr.click("css->.el-message-box__btns>button:nth-child(2)")

        return LoginPage.Login(self.dr)

    def click_center(self):
        """点击右上角图标"""
        self.dr.click("css->div.flex.flex--align-center.el-dropdown-selfdefine")
        time.sleep(1)



