import platform

"""
# 判断当前操作系统环境；以此来自动选择不同浏览器环境的驱动
"""


def osSystem(path=''):
    os_system = platform.system()
    if os_system == 'Windows':
        print('当前操作系统：Windows')
        pathWin = path + r'Browser_Driver/chromedriver84(win32).exe'
        return pathWin
    if os_system == 'Darwin' or 'darwin' or 'Mac' or 'mac' or 'OS X':
        print('当前操作系统：Mac OS')
        pathMac = path + r'Browser_Driver/chromedriver84(Mac64)'
        return pathMac


if __name__ == '__main__':
    osSystem()
