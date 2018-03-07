#-*- encoding:utf-8 -*-
#-*- encoding:gbk -*-
#!/bin/python

import email, getpass, poplib, sys
import psycopg2
import time,datetime



def connAndInsert(eventid, eventname, roomid, starttime,endtime,bookpeople):
    conn = psycopg2.connect(database="mydb", user="postgres",password="postgres", host="localhost")
    cur = conn.cursor()
    cur.execute("INSERT INTO event (eventid, eventname, roomid, starttime,endtime,bookpeople) \
            VALUES (%s, %s, %s, %s, %s,%s)",(eventid, eventname, roomid, starttime,endtime,bookpeople))

    conn.commit()

    print ('Just Booked:')
    cur.execute("SELECT * from event where eventid=%s",(eventid,))
    rows = cur.fetchall()
    for row in rows:
        print "eventid = ", row[0]
        print "eventname = ", row[1]
        print "roomid = ", row[2]
        print 'starttime=',row[3]
        print 'endtime',row[4]
        print 'bookpeople',row[5]
    
    conn.close() 
