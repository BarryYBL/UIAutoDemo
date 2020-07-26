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
    driver_path : 设置浏览器驱动的绝对路径。要和 browser 设置保持一致,
    grid_url : 设置远程节点，selenium Grid doc,
    timeout : 设置超时时间，默认10秒

邮件发送功能：
    引入'from seldom.mail import SMTP'
    smtp = SMTP(user="you@126.com", password="abc123", host="smtp.126.com")
    time.sleep(3)
    smtp.sender(to="receive@mail.com")
"""

import seldom
import time
from seldom.mail import SMTP

if __name__ == '__main__':
    seldom.main(
        path='../test_case',
        browser='chrome',
        driver_path='../Browser_Driver/chromedriver84',
        debug=False,
        rerun=0,
        timeout='10',
        save_last_run=True,
        title='自动化测试报告',
        description='测试环境：Chrome'
    )