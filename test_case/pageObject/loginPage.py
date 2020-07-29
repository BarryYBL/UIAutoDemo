# -*-coding:utf-8-*-
# 用于登录页元素定位
import sys
sys.path.append('./models')
from models.url import Url
from poium import Page, PageElement, PageElements, NewPageElement, PageWait, PageSelect

class login(Page):
    """ 项目用户登录、退出定位元素"""
    # url
    url = Url.baseUrl

    # 示例
    search_input_loc = NewPageElement(id_='kw')
    search_button_loc = NewPageElement(id_='su')

    # 操作方法封装
    def search_input(self, key):
        self.search_input_loc.clear()
        self.search_input_loc.send_keys(key)

    def search_button(self):
        self.search_button_loc.click()
