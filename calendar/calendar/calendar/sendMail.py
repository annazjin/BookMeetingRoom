#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-
#in 

import getpass, email, sys
import imaplib
import smtplib

from email.mime.text import MIMEText

import psycopg2

import datetime

from time import *

class responseEmail:
    def __init__(self,sender,):
mail_host= "smtp.gmail.com" 
mail_user= "anna.z.jin@gmail.com"   
mail_pass=  "Pwcwelcome2" 
mail_port="587"

def send_mail(to_list,sub,content):  
    me= mail_user
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')  
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] = ";".join(to_list)  
    try:  
        server = smtplib.SMTP(mail_host,mail_port) 
        server.ehlo()
        server.starttls()
        server.login(mail_user,mail_pass)  
        server.sendmail(me, to_list, msg.as_string())  
        server.quit()  
        return True  
    except Exception, e:  
        print str(e)  
        return False

