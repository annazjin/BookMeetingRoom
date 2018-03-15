#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-


import getpass, email, sys
import re
from email.message import Message 
from email.header import Header
from imapclient import IMAPClient

global List
global value
class getList:
    def getl(self):
        hostname = 'imap.gmail.com' 
        username = 'anna.z.jin@gmail.com'
        passwd = 'Pwcwelcome2'
        List=[]
        c = IMAPClient(hostname, ssl= True) 
        try:
            c.login(username, passwd) 
        except c.Error:
            print('Could not log in')
            sys.exit(1)
        else:
            c.select_folder('INBOX', readonly = False) 
            result = c.search('UNSEEN')
            msgdict = c.fetch(result, ['BODY.PEEK[]'] )
            c.set_flags(msgdict,'\Seen')
            
            for message_id, message in msgdict.items():
                e = email.message_from_string(message['BODY[]'])
                subject = email.header.make_header(email.header.decode_header(e['SUBJECT']))
                sender = email.header.make_header(email.header.decode_header(e['From']))
                step1 = str(sender).split('<')[1:]
                step2 = step1[0].split('>')[0:]
                mail_from=step2[0]
                maintype = e.get_content_maintype()
                if maintype == 'multipart':
                    for part in e.get_payload():
                        if part.get_content_maintype() == 'text':
                            mail_content = part.get_payload(decode=True).strip()
                elif maintype == 'text':
                    mail_content = e.get_payload(decode=True).strip()
            
                try:
                    mail_content = mail_content.decode('gbk')
                except UnicodeDecodeError:
                    print('decode error')
                    sys.exit(1)
                else:
                    dic={}
                    dic['From']=str(mail_from)
                    dic['Subject']=str(subject)

                    mailcontent=mail_content.replace('<br>', '\n')
                    p=re.compile('<[^>]+>')
                    content=p.sub('',mailcontent)

                    dic['Content']=str(content)
                    List.append(dic) 
        finally:
            c.logout()
        return List
def getvalue():
    getl= getList()
    value=getl.getl()
    return value
