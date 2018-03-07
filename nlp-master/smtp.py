#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-


import getpass, email, sys
import imaplib
import smtplib

from email.mime.text import MIMEText

import psycopg2

import datetime

from time import *

mail_host= "smtp.gmail.com" 
mail_user= "anna.z.jin@gmail.com"   
mail_pass=  "Pwcwelcome2" 
mail_port="587"

def send_mail(to_list,sub,content):  
    
    if type(content)==str:
        mail_msg='''
        <html>
        <head>
        <style>
        body{
        background: lightgray;
        }
        table{
        width: 100%%;
        font: "Times New Roman";
        font-size: 20px;
        }
        th{
        height: 50px;
        background-color: rgb(233, 116, 6);
        }
        </style>
        </head>
        <body >
        <img class="gb_Xa" src="https://www.google.com/a/pwc.com/images/logo.gif?alpha=1&amp;service=google_default" style="max-width:144px;max-height:60px">

        <p>%s</p>

        </body>
        '''%(content)
    else:
        
        #数据库查询结果回复内容变成html格式
        
        rowhtmlist=[]

        for row in content:
            rowhtml='<tr><td align="center"> %s</td><td align="center"> %s</td><td align="center"> %s</td><td align="center"> %s</td><td align="center"> %s</td></tr>'%(row['roomid'],row['roomname'],row['building'],row['floor'],row['maxpeople'])
            rowhtmlist.append(rowhtml)

        #生成表格部分的html
        htmlreply="".join(rowhtmlist)
        
        
        mail_msg = '''
        <html>
        <head>
        <style>
        body{
        background: lightgray;
        }
        table{
        width: 100%%;
        font: "Times New Roman";
        font-size: 20px;
        }
        th{
        height: 50px;
        background-color: rgb(233, 116, 6);
        }
        </style>
        </head>
        <body >
        <img class="gb_Xa" src="https://www.google.com/a/pwc.com/images/logo.gif?alpha=1&amp;service=google_default" style="max-width:144px;max-height:60px">
        <table style="height:auto;position:relative;">
            <thead style="background-color:lightgray">
            

                <tr>
                    <th style="width:10%%;">Room ID</th>
                    <th style="width:10%%;">Room Name</th>
                    <th style="width:10%%;">Building</th>
                    <th style="width:10%%;">Floor</th>
                    <th style="width:10%%;">Maxpeople</th>
                    
                </tr>
            </thead>

            <tbody style="background-color:rgb(236, 176, 135)">
                
            %s
                
            </tbody>
        </table>

        '''%(htmlreply)
    
    #邮件其他相关量
    me= mail_user
    msg = MIMEText(
    mail_msg, 'html', 'utf-8'
    )
    msg['Subject'] = sub  
    msg['From'] = me  
    msg['To'] =to_list
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

