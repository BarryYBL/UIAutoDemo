from seldom import SMTP
import time

# 配置e-mail信息
# user = 'you@126.com'  # 发送者邮件账号
# password = 'DINODMVPZVSBPYKA'  # 发送者邮件授权码
# host = 'smtp.126.com'  # host路径
# to = 'to@mail.com'  # 邮件接收者，如有多个','英文逗号分割
# subject = None


def sendMail(user, password, host, to, subject=None):
    try:
        smtp = SMTP(user=user, password=password, host=host)
        time.sleep(3)
        smtp.sender(to=to, subject=subject)
    except Exception as error:
        return error
