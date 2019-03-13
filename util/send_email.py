import smtplib
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from log.user_log import UserLog
from util.read_ini import ReadIni

class Sendmail:
    def __init__(self,runningtime):
        self.user_log = UserLog().get_log()
        self.read_ini = ReadIni(node='email')
        self.run_time = runningtime

    def send_mail(self):
        sender = self.read_ini.get_value('sender')
        passwd = self.read_ini.get_value('passwd')
        receiver = self.read_ini.get_value('receivers')
        mail_host = self.read_ini.get_value('mail_host')
        print (sender,passwd,receiver,mail_host)
        tm = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        msg = MIMEMultipart()
        msg['Subject'] = Header(self.read_ini.get_value('header') + tm, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver

        #发送邮件正文
        msg.attach(MIMEText(self.read_ini.get_value('content')+str(self.run_time),'plain','utf-8'))
        #构造附件
        lists = []
        print(self.read_ini.get_value('path'))
        for root, dirs, files in os.walk(self.read_ini.get_value('path')):
            for file in files:
                if file.endswith(".html"):
                    lists.append(os.path.join(root, file))
        lists.sort(key=lambda f: os.stat(f).st_mtime)
        print(lists)
        lastmodified = lists[-1]
        att = MIMEText(open(lastmodified,'rb').read(),'base64','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename='+self.read_ini.get_value('filename')
        msg.attach(att)

        #发送
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host,25)
            smtpObj.login(sender,passwd)
            smtpObj.sendmail(sender,receiver,msg.as_string())
        except Exception as e:
            print(e)
            print('发送失败')
            self.user_log.warn("邮件发送失败:"+tm)
        else:
            print('发送成功')
            self.user_log.info('邮件发送成功')
        finally:
            smtpObj.close()

if __name__=="__main__":
    Sendmail().send_mail()