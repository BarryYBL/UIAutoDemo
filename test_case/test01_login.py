"""
说明：
# 调用的到的 第三方模块：seldom、sys、time
# 调用的到的 私有化模块：model/url、page_object/ invoiceOpenPage 下的 invoiceOpen\invoiceOpen_Validation
#                     page_object\ loginPage 下的 login
# 运行时需要配置：
# 1、setUpClass方法需要设定 启动的浏览器，默认为chrome; 设定该项目账号与密码
# 2、单元测试不能生成测试报告，需要在run.py运行配置
"""
import seldom
from seldom import Seldom
from pageObject.loginPage import login

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
        self.dr.search_input(key='百度一下')
        self.dr.search_button()
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
        driver_path='../Browser_Driver/chromedriver84',
        debug=False,
        rerun=0,
        timeout=10,
        save_last_run=True,
        title='自动化测试报告',
        description='测试环境：Chrome'
    )