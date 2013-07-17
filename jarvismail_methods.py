#!/usr/bin/python3.2
import sys
sys.path.append('/home/kevin/Downloads/Jarvis/JarvisMethods')
from textsender import textsender as textsender

jarvis_username = 'antonshipley@gmail.com'
jarvis_password = 'TradecraftOlympic1865'

def createjdate(gmaildatestring):
    import datetime as datetime
    string = gmaildatestring

    l = string.split(' ')
    l[0] = l[0].replace(',','')
    l[4] = l[4].split(':')

    day = int(l[1])
    year = int(l[3])
    hour = int(l[4][0])
    minute = int(l[4][1])
    second = int(l[4][2])
    
    month = l[2]
    if month == 'Jan':
        month = 1
    elif month == 'Feb':
        month = 2
    elif month == 'Mar':
        month = 3
    elif month == 'Apr':
        month = 4
    elif month == 'May':
        month = 5
    elif month == 'Jun':
        month = 6
    elif month == 'Jul':
        month = 7
    elif month == 'Aug':
        month = 8
    elif month == 'Sep':
        month = 9
    elif month == 'Oct':
        month = 10
    elif month == 'Nov':
        month = 11
    elif month == 'Dec':
        month = 12
    else:
        textsender(8173126800,'error with createjdate, find month')
    
    jdate = datetime.datetime(year,month,day,hour,minute,second)
    return(jdate)

class jarvismessage:
    import datetime as datetime
    
    def __init__(self,messageID,From,To,Date,Subject,Body):
        self.ID = messageID
        self.F = From
        self.T = To
        self.D = Date
        self.S = Subject
        self.B = Body
    def __repr__(self):
        return 'messageID: %s' % (self.ID)
    def __str__(self):
        return 'From: %s,\n\nTo: %s,\n\nDate: %s\n\nSubject: %s:\n\n%s' % (self.F,self.T,self.D,self.S,self.B)

##h = jarvismessage('1','test@test','test@test','today','test','test test')
##print(h)
    
def getgmail(username,password,SEARCH_KEY):
    global jarvis_username
    global jarvis_password
    username = jarvis_username
    password = jarvis_password
    import datetime as datetime
    from email.parser import HeaderParser
    import email, getpass, imaplib, os
    jmail = []
    M = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    M.login(username, password)
    M.select()
    typ, items = M.search(None, SEARCH_KEY)# you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)
    idlist = items[0].split()

    for num in idlist:
        Body = None
        resp, data = M.FETCH(num, '(RFC822)')
        try:
            email_body = data[0][1].decode() # getting the mail content
        except:
            email_body = data[0][1].decode('latin-1') # getting the mail content
        mail = email.message_from_string(email_body)
        for part in mail.walk():
            if part.get_content_maintype() == 'text':
                Body = part.get_payload()
                break
        Subject = mail['Subject']
        Date = createjdate(mail['Date'])
        To = mail['Delivered-To']
        From = mail['From']
        messageID = mail['Message-ID']
        jmessage = jarvismessage(messageID,From,To,Date,Subject,Body)
        jmail.append(jmessage)
                
    M.close()
    M.logout()
    return(jmail)

def send_mail(to, subject, text, attach):
    import smtplib
    import os

    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    global jarvis_username
    global jarvis_password
    gmail_user = jarvis_username
    gmail_pwd = jarvis_password
    
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject




    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.close()


