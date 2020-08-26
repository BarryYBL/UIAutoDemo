import platform
from seldom.logging import log

"""
# 判断当前操作系统环境；以此来自动选择不同浏览器环境的驱动
"""


def osSystem(path=''):
    os_system = platform.system()
    if os_system == 'Windows':
        log.info('当前操作系统：Windows')
        pathWin = path + r'Browser_Driver/chromedriver84(win32).exe'
        return pathWin
    elif os_system == 'Darwin' or \
            os_system == 'darwin' or \
            os_system == 'Mac' or \
            os_system == 'mac' or \
            os_system == 'OS X':
        log.info('当前操作系统：Mac OS')
        pathMac = path + r'Browser_Driver/chromedriver84(Mac64)'
        return pathMac
    else:
        log.error("当前操作系统 " + os_system)
        raise SystemExit(log.error(' ❌ The current operating system environment is not  Windows  or  Mac, '
                                   'please confirm the current environment!!'))


if __name__ == '__main__':
    osSystem()
