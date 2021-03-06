#coding=utf-8
import time

class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver

    def exist_loading(self):
        """等待全局loading消失"""
        while True:
            result = self.dr.element_exist('css->.loading-mask')
            if result:
                time.sleep(1.5)
            else:
                break

    def get_error_text(self):
        """获取错误弹窗内容"""
        text = self.dr.get_text("css->.el-message.el-message--error>p")

        return text


