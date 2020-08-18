"""
说明：
# 调用的到的 第三方模块：seldom、sys、time
# from seldom import Seldom
# import seldom
# 调用的到的 私有化模块：model/page_object/

# 运行时需要配置：
# 1、在pycharm运行时需要将'pageObject'配置环境变量，路径：Project-UIautoDemo-ProjectStructure
"""
import seldom
from seldom import Seldom
from pageObject.loginPage import *


class test01_login(seldom.TestCase):
    def start(self):
        self.dr = login(Seldom.driver)
        self.dr.get(login.url)
        self.max_window()
    def down(self):
        self.quit()

    @classmethod
    def setUpClass(cls):
        cls().start()

    @classmethod
    def tearDownClass(cls):
        cls().down()

    def test01(self):
        """测试示例1"""
        self.dr.search_input(key='百度一下')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test01')

    def test02(self):
        """测试示例2"""
        self.dr.search_input_loc.clear()
        self.dr.search_input_loc.send_keys('百度一下')
        self.dr.search_button_loc.click()
        self.assertText("百度一下")
        print('用例说明：test02')

    def test03(self):
        """测试示例3"""
        self.dr.search_input(key='百度一下')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test03')

    def test04(self):
        """测试示例4"""
        self.dr.search_input(key='百度一下')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test04')

    def test05(self):
        """测试示例5"""
        self.dr.search_input(key='百度一下')
        self.dr.search_button()
        self.assertText("百度一下")
        print('用例说明：test05')


if __name__ == '__main__':
    seldom.main(
        path='../test_case/test01_login.py',
        browser='chrome',
        driver_path='../Browser_Driver/chromedriver84(Mac64)',
        debug=False,
        rerun=0,
        timeout=10,
        save_last_run=True,
        title='自动化测试报告',
        description='测试环境：Chrome'
    )