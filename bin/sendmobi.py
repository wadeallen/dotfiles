#!/usr/bin/env python3

import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys, os

book = sys.argv[1]
exten = book.split(".")[0]
print(book, exten)

fromaddr = config.username
toaddr  = config.username

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "emailing "
 
body = "This is a scripted email to send file to kindle"
 
msg.attach(MIMEText(body, 'plain'))

body = "TEXT YOU WANT TO SEND"
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "test.txt"
attachment = open("/home/wadeallen/Desktop/test.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(config.username,config.password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("File has been emailed")
