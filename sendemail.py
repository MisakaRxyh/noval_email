import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

import datetime
import getnoval

smtpserver = 'smtp.office365.com,587'
username = '18956901938@163.com'
password = 'czj123456'
sender = '18956901938@163.com'
receiver = '18956901938@163.com'
#receiver = ['18956901938@163.com','2998280865@qq.com']
urls = []
nexturls = []
htmls = []
subjects = []
with open('E:/Python_Test/noval_email/noval.txt', 'r') as f:
#    url = f.read()
    for line in f.readlines():
        if line != '\n':
            urls.append(line.strip())# 把末尾的'\n'删掉
for url in urls:
    html,nexturl,subject = getnoval.Noval_Html_Code(url)
    htmls.append(html)
    print(html)
    nexturls.append(nexturl)
    subjects.append(subject)

with open('E:/Python_Test/noval_email/noval.txt', 'w') as f:
    for nexturl in nexturls:
        f.write(nexturl + '\n')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
print("connect success")
smtp.set_debuglevel(1)
smtp.login(username,password)
print("login success")
for (subject,html) in zip(subjects,htmls):
    subject = Header(subject, 'utf-8').encode()
    msg = MIMEMultipart('mixd')
    msg['Subject'] = subject
    msg['From'] = '皮皮陈<18956901938@163.com>'
    msg['To'] = '渣渣陈<18956901938@163.com>'
    msg['Data'] = datetime.datetime.now().strftime('%Y-%m-%d')

    text_html = MIMEText(html,'html','utf-8')
    msg.attach(text_html)
    smtp.sendmail(sender, receiver, msg.as_string())
    print("send success")
smtp.quit()
print("quit success")