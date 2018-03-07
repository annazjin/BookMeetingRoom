# -*- coding: UTF-8 -*-
#接收邮件
import imap
import schedule
import time
import connect_database
#发送邮件
import smtp
class check:
    global value

    def job():
        #value是本次刷新所获得的所有新邮件的内容字典的list
        value =imap.getvalue()
        if value:
            #item：一封新邮件
            for item in value:
                sentence=item['Subject']
                people=item['From']
                
                reply=connect_database.select_database(sentence)
                #回复邮件
                smtp.send_mail(people,'Please choose the proper meeting room',reply)
                
                
                print "Successfully sent email to: "+people
            
        
    schedule.every(0.1).minutes.do(job)
    while True:
        schedule.run_pending()  

