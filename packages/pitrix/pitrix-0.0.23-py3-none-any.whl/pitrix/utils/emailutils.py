#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
        subject,
        sender,
        recipients,
        body,
        smtp_server,
        smtp_port,
        login_user,
        login_password,
        ssl_on=False,
        timeout=15,
        attachments=None):
    """
    向收件人发送电子邮件
    :param subject:邮件主题
    :param sender:发件人
    :param recipients:电子邮件收件人列表
    :param body:邮件正文内容
    :param smtp_server: smtp服务
    :param smtp_port: smtp端口号 25
    :param login_user: 登录邮箱的用户名
    :param login_password: 登录邮箱的密码
    :param ssl_on: 是否开启SSL
    :param timeout: 超时时间
    :param attachments: 是否发送附件, 发送的格式内容如下, [{'name': "name.txt", 'data': 'file data', 'charset': 'UTF-8'}]
    :return:
    """
    recipient_addrs = ",".join(recipients)
    header_charset = 'UTF-8'

    message = MIMEMultipart()
    message['From'] = Header(sender)
    message['To'] = recipient_addrs
    message['subject'] = Header(subject, header_charset)  # 邮件标题
    message.attach(MIMEText(body, 'html', header_charset))  # 邮件正文

    if attachments:
        if attachments:
            for attachment in attachments:
                res = open(attachment['name'], 'rb').read()
                att = MIMEText(res, 'base64', attachment['charset'])
                att["Content-Type"] = 'application/octet-stream'
                att_header = Header((attachment['name']), header_charset)
                att.add_header(
                    'Content-Disposition',
                    'attachment; filename="%s"' %
                    att_header)
                if 'content_id' in attachment:
                    att.add_header(
                        'Content-ID', '<%s>' %
                        attachment['content_id'])
                message.attach(att)

    try:
        if ssl_on:
            session = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=timeout)
        else:
            session = smtplib.SMTP(smtp_server, smtp_port, timeout=timeout)
        session.connect(smtp_server, smtp_port)
        if login_user:
            session.login(login_user, login_password)
        session.sendmail(sender, recipients, message.as_string())
        session.quit()
        print(f'邮件发送到 {recipients} 成功')
        return True
    except Exception as e:
        print(f'邮件发送到 {recipients} 失败,原因:{e}')
        return False
