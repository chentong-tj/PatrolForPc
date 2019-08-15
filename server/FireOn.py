import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr

class FireOn():
    def __init__ (self,smtp_server,from_who,to_who,if_own_massage):
        self.smtp_server = smtp_server
        self.from_who = from_who
        self.to_who = to_who
        self.if_own_massage = if_own_massage

    def SendMail(self):
    #发送邮件用，需先行设置stmp配置，传入smtp服务器地址，发送方邮箱，接收方邮箱，邮件正文（可选）
    #return 正常为字符串sendover，不正常返回错误代码
        msg = MIMEMultipart()
        msg['From'] = formataddr('本邮件来自 %s' % self.from_who).encode()
        msg['To'] = ','.join(self.to_who)
        msg['Subject'] = Header('报警报告邮件','utf-8').encode()
        if self.if_own_massage == None:
            #构建默认msg
            msg.attach(MIMEText("这是默认邮件内容，请查看报警",'html','utf-8'))
        else:
            msg.attach(MIMEText(self.if_own_massage,'html','utf-8'))
        try:
            send = smtplib.SMTP()
            send.connect(self.smtp_server,"25")
            send.login(self.from_who,"xxx")
            send.sendmail(self.from_who,self.to_who,msg.as_string())
            send.quit()
            return 'sendover'
        except smtplib.SMTPException as e:
            return e

    def wx(self):
        #todu:开发微信报警推送
        return 0

