"""
main方法说明：
    path ： 指定测试目录或文件,
    browser : 指定测试浏览器，默认Chrome,
    report : 自定义测试报告的名称，默认格式为2020_04_04_11_55_20_result.html,
    title ： 指定测试报告标题,
    description ： 指定测试报告描述,
    debug ： debug模式，设置为True不生成测试HTML测试，默认为False,
    rerun : 设置失败重新运行次数，默认为 0,
    save_last_run : 设置只保存最后一次的结果，默认为False,
    driver_path : 设置浏览器驱动的绝对路径。要和 browser 设置保持一致；默认,
    grid_url : 设置远程节点，selenium Grid doc,
    timeout : 设置超时时间，默认10秒，
    xmlrunner : 默认False，True生成xml格式的测试报告，html与xml报告二者选一


邮件发送功能：
    引入'from models.mail import sendMail'
    user = 'you@126.com'    # 发送邮件账号
    password = 'ABC123'     # 发送邮件密码
    host = 'smtp.126.com'   # host路径
    to = 'receive@mail.com'     # 邮件接受者，如有多个','英文逗号分割
    sendMail(user, password, host, to)
"""


import seldom
from seldom import ChromeConfig
from models.mail import sendMail
from Cdriver import cdriver

# 配置e-mail信息
user = 'you@126.com'    # 发送者邮件账号
password = 'DINODMVPZVSBPYKA'     # 发送者邮件授权码
host = 'smtp.126.com'   # host路径
to = 'to@mail.com'     # 邮件接收者，如有多个','英文逗号分割


if __name__ == '__main__':
    ChromeConfig.headless = False
    ChromeConfig.executable_path = cdriver()   # 默认根据操作系统自行选择Chromedriver驱动
    seldom.main(
        path='./test_case/test01_login.py',
        browser='chrome',
        debug=False,
        rerun=0,
        timeout=10,
        save_last_run=True,
        title='自动化测试报告',
        description='测试环境：Chrome'
    )
    """mail邮件发送；关闭注释启用"""
    sendMail(user, password, host, to)