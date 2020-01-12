#coding=utf-8
from public.common import basepage
from public.pages.WorkBenchPage import WorkBench


class Login(basepage.Page):
    """登录页面"""

    def input_account(self, account):
        """输入账号"""
        self.dr.clear_type("css->[placeholder='手机号']", account)

    def input_pw(self, pw):
        """输入密码"""
        self.dr.clear_type("css->[placeholder='密码']", pw)

    def click_login_btn(self):
        """点击登录按钮"""
        self.dr.click("class->el-button")

        return WorkBench(self.dr)

    def get_url(self):
        """获取url"""
        url = self.dr.get_url()
        return url

    def get_title(self):
        """获取登录框上的大标题"""
        text = self.dr.get_text("class->slogan")
        return text

    def click_box(self):
        """点击记住密码"""
        self.dr.click("class->el-checkbox__input")

    def login(self, account, pw):
        """封装登录函数"""
        self.input_account(account)
        self.input_pw(pw)
        self.click_box()
        self.click_login_btn()

        return WorkBench(self.dr)

