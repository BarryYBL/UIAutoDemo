import re
import os
import zipfile
import platform
import requests
from seldom.logging import log

"""
# 判断当前操作系统环境；以此来自动选择不同浏览器环境的驱动
"""

class automatic(object):
    def __init__(self):
        self.url = 'http://npm.taobao.org/mirrors/chromedriver/'

    # 获取线上最新版本号与版本时间
    def get_latest_version(self):
        rep = requests.get(self.url, timeout=30).text
        time_list = []
        time_version_dict = {}
        result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)
        for x in result:
            time = x[-24:-1]
            version = re.compile(r'.*?/').findall(x)[0]
            time_version_dict[time] = version
            time_list.append(time)
        latest_version = time_version_dict[max(time_list)][:-1]    # 获取浏览器版本号
        log.info('线上最新版本：'+str(latest_version))
        return latest_version

    # 下载Mac系统下的Chromedriver
    def mac_download_driver(self, path=''):
        latest_version = automatic().get_latest_version()
        mac_driver_url = self.url + latest_version + '/chromedriver_mac64.zip'
        file = requests.get(mac_driver_url, timeout=60)
        with open(path + r'Browser_Driver/chromedriver.zip', 'wb') as zip_file:
            zip_file.write(file.content)
            log.info('Mac驱动下载成功！！！')

    # 下载Windows系统下的Chromedriver
    def win_download_driver(self, path=''):
        latest_version = automatic().get_latest_version()
        win_driver_url = self.url + latest_version + '/chromedriver_win32.zip'
        file = requests.get(win_driver_url, timeout=60)
        with open(path + r'Browser_Driver/chromedriver.zip', 'wb') as zip_file:
            zip_file.write(file.content)
            log.info('Windows驱动下载成功！！！')

    # 解压缩包
    def Unpack_driver(self, path=''):
        file = zipfile.ZipFile(path + r'Browser_Driver/chromedriver.zip', 'r')
        for files in file.namelist():
            file.extract(files, path + r'Browser_Driver')
            log.info('解压成功！！！')
        file.close()
        os.remove(path + r'Browser_Driver/chromedriver.zip')
        log.info('ChromeDriver驱动压缩包删除成功！！！')

    # Mac系统下的本地与线上版本对比
    def Contrast_mac(self, path=''):
        try:
            log.info('正在检查本地ChromeDriver！！！')
            r = os.path.abspath(path + r'Browser_Driver/chromedriver')
            os.popen('chmod +x '+r)
            version = os.popen(r + r' --version').read()
            version = version.split(' ')[1]
            log.info("当前版本号："+str(version))
        except Exception as error:
            error
            log.info('❎检查不到Chromedriver，正在下载...')
            automatic().mac_download_driver(path=path)
            automatic().Unpack_driver(path=path)
            r = os.path.abspath(path + r'Browser_Driver/chromedriver')
            os.popen('chmod +x ' + r)
            version = os.popen(r + r' --version').read()
            version = version.split(' ')[1]
            log.info("当前版本号："+str(version))
        if version == automatic().get_latest_version():
            log.info('✅当前系统Chromedriver已经是最新版本')
        else:
            log.info('当前系统Chromedriver不是最新版本，需要更新！！！ 请等待！！！')
            automatic().mac_download_driver(path=path)
            automatic().Unpack_driver(path=path)

    # Windows系统下的本地与线上版本对比
    def Contrast_win(self, path=''):
        try:
            log.info('正在检查本地ChromeDriver！！！')
            r = os.path.abspath(path + r'Browser_Driver/chromedriver.exe')
            version = os.popen('"'+r+'"' + r' --version').read()
            version = version.split(' ')[1]
            log.info("当前版本号："+str(version))
        except Exception as error:
            error
            log.info('❎检查不到Chromedriver，正在下载...')
            automatic().win_download_driver(path=path)
            automatic().Unpack_driver(path=path)
            r = os.path.abspath(path + r'Browser_Driver/chromedriver.exe')
            version = os.popen('"'+r+'"' + r' --version').read()
            version = version.split(' ')[1]
            log.info("当前版本号："+str(version))

        if version == automatic().get_latest_version():
            log.info('✅当前系统Chromedriver已经是最新版本')
        else:
            log.info('当前系统Chromedriver不是最新版本，需要更新！！！ 请等待！！！')
            automatic().win_download_driver(path=path)
            automatic().Unpack_driver(path=path)

def osSystem(path=''):
    os_system = platform.system()
    driver = automatic()
    if os_system == 'Windows':
        log.info('当前操作系统：Windows')
        driver.Contrast_win(path=path)   # 检查对比Windows系统环境下的Chromedriver
        pathWin = path + r'Browser_Driver/chromedriver.exe'
        return pathWin
    elif os_system == 'Darwin' or \
            os_system == 'darwin' or \
            os_system == 'Mac' or \
            os_system == 'mac' or \
            os_system == 'OS X':
        log.info('当前操作系统：Mac OS')
        driver.Contrast_mac(path=path)  # 检查对比Mac系统环境下的Chromedriver
        pathMac = path + r'Browser_Driver/chromedriver'
        return pathMac
    else:
        log.error("当前操作系统 " + os_system)
        raise SystemExit(log.error(' ❌ The current operating system environment is not  Windows  or  Mac, '
                                   'please confirm the current environment!!'))


if __name__ == '__main__':
    result = automatic()
    osSystem('../')
