'''
Author: fengsc
Date: 2022-04-17 17:07:26
LastEditTime: 2022-04-18 16:38:30
'''
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
print("The following input press enter to use default")
mail_host = input("Input main host(default:smtp.qq.com):") or "smtp.qq.com"  # 设置服务器
mail_user = input("Input main user(default:2471326731@qq.com):")or"2471326731@qq.com"  # 用户名
mail_pass = input("Input main pass(default:ligwcwdmkcvrecbe):")or"ligwcwdmkcvrecbe"  # 授权码
sender = mail_user
receivers =input("Input receivers(default:2170412575@qq.com,Separated by Spaces if there are more than one):")or['2170412575@qq.com', ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText(input("Input text:"), 'plain', 'utf-8')
# 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
message['From'] = Header(input("Input from :"), 'utf-8')
message['To'] = Header(input("Input to:"), 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
message['Subject'] = Header(input("Input subject :"), 'utf-8')
try:
    smtpObj = smtplib.SMTP(timeout=100)
    smtpObj.connect(mail_host, 25)  # 发件人邮箱中的SMTP服务器
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as ex:
    print("Error: 无法发送邮件",ex)
    # raise

# smtpObj.quit()
msg = '''\
From: fengsc
Subject: testin

This is a test '''
