from seldom.mail import SMTP
import time

# 配置e-mail信息
# user = 'you@126.com'  # 发送者邮件账号
# password = 'DINODMVPZVSBPYKA'  # 发送者邮件授权码
# host = 'smtp.126.com'  # host路径
# to = 'to@mail.com'  # 邮件接收者，如有多个','英文逗号分割
# subject = None


def sendMail(user, password, host, to, subject=None):
    smtp = SMTP(user=user, password=password, host=host)
    time.sleep(3)
    try:
        smtp.sender(to=to, subject=subject)
        smtp.sender(to=to)
        return print('📮 Email sent successfull！')
    except Exception as error:
        return error, print('❌ Email failed to send！\n', error)
