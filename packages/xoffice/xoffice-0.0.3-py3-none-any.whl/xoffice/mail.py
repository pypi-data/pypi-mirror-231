import os.path
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Union, Sequence


class EMail(object):
    """
    用于发送邮件
    """

    def __init__(self, user: str, password: str, host: str = None, port: int = 465, ssl: bool = True):
        """
        初始化
        :param user: 邮箱账号
        :param password: 邮箱授权码
        :param host: 服务器地址
        :param port: 服务器端口
        :param ssl: 是否 ssl 加密传输
        """
        self.user = user
        self.password = password
        if host is None:
            self.host = "smtp." + self.user.split("@")[-1]
        self.port = port
        if ssl:
            self._smtp = smtplib.SMTP_SSL(self.host, self.port)
        else:
            self._smtp = smtplib.SMTP(self.host, self.port)  # self._smtp.set_debuglevel(1)

    def connect(self):
        """
        连接邮箱服务器
        :return:
        """
        self._smtp.login(self.user, self.password)

    def close(self):
        """
        断开邮箱服务器
        :return:
        """
        self._smtp.quit()

    def easy_send(self, to: Union[str, Sequence[str]], title: str, content: str, attachments: Sequence[str] = None):
        """
        简易版发送邮件，将连接和断开服务器整合在了一起，发送单份邮件时使用
        :param to:
        :param title:
        :param content:
        :param attachments:
        :return:
        """
        self.connect()
        self.send(to, title, content, attachments)
        self.close()

    def send(self, to: Union[str, Sequence[str]], title: str, content: str, attachments: Sequence[str] = None):
        """
        普通版发送邮件，使用时需要结合 connect 和 close 方法
        :param to: 收件人，可以多人
        :param title: 邮件主题
        :param content: 邮件内容
        :param attachments: 邮件附件，给出附件地址即可
        :return:
        """
        if attachments is None:
            attachments = []
        body = MIMEMultipart()
        # 设置邮件主题
        body['Subject'] = Header(title, 'utf-8').encode()
        # 设置邮件发送者
        body['From'] = self.user
        # 设置邮件接受者
        if isinstance(to, str):
            body['To'] = to
        else:
            body["To"] = ",".join(to)
        # 添加文本内容
        text = MIMEText(content, 'html', 'utf-8')
        body.attach(text)
        # 添加附件
        for path in attachments:
            if os.path.isfile(path):
                filename = os.path.split(path)[-1]
                with open(path, "rb") as f:
                    attach = MIMEApplication(f.read())
                attach["Content-Type"] = 'application/octet-stream'
                attach.add_header('Content-Disposition', 'attachment', filename=filename)
                body.attach(attach)
            else:
                print(path + ":wrong path")
        self._smtp.sendmail(self.user, to, body.as_string())
