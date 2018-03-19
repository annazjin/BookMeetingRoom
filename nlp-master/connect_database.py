# -*- coding: UTF-8 -*-




#参数是句子，先调用nlparser模块pasing，再根据情况查数据库，返回值是string
def select_database(sentence):
    
    
    
    try:
        import psycopg2
        import nlparser
    except ImportError:
        print "requires psycopg2 nlparser"

    conn = psycopg2.connect(database="mydb", user="postgres", password="postgres", host="localhost")
    cur = conn.cursor()    
    reply="null"
    resultdict=nlparser.parser(sentence)[0]
    
    message=nlparser.parser(sentence)[1]

    #十种时间分支的不能被读懂的分支，没有返回结果，直接回邮件说读不懂
    if resultdict['endtime']==0:
        reply=message
    
    #没有默认选项，直接返回结果，不需要再回邮件确认
    elif message=="null":
        
        if resultdict['building']=="NULL":
            
            if resultdict['people']=="NULL":
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor']))
                    rows=cur.fetchall()
                
                pass
            else:
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and maxpeople>=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['people']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and maxpeople>=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['people']))
                    rows=cur.fetchall()

            
        else:
            
            if resultdict['people']=="NULL":
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['building']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['building']))
                    rows=cur.fetchall()
                
                pass
            else:
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and maxpeople>=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['people'],resultdict['building']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and maxpeople>=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['people'],resultdict['building']))
                    rows=cur.fetchall()
        
        reply_rowdic_list=[]
        for row in rows:
            reply_rowdic={'roomid':row[0],'roomname':row[1],'building':row[2],'floor':row[3],'maxpeople':row[4]}
            reply_rowdic_list.append(reply_rowdic)
        
        reply=reply_rowdic_list
    
        
    #有默认值，又查数据库又回信（本分支实际上没有用到）    
    else:
        
        if resultdict['building']=="NULL":
            
            if resultdict['people']=="NULL":
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor']))
                    rows=cur.fetchall()
                
                pass
            else:
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and maxpeople>=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['people']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and maxpeople>=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['people']))
                    rows=cur.fetchall()

            
        else:
            
            if resultdict['people']=="NULL":
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['building']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['building']))
                    rows=cur.fetchall()
                
                pass
            else:
                
                if resultdict['floor']=="NULL":
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and maxpeople>=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['people'],resultdict['building']))
                    rows = cur.fetchall()
                else:
                    cur.execute("select * from room where roomid not in (select roomid from event where (starttime>=%s and starttime<=%s) or (endtime>=%s and endtime<=%s)) and floor=%s and maxpeople>=%s and building=%s order by maxpeople asc",(resultdict['starttime'],resultdict['endtime'],resultdict['starttime'],resultdict['endtime'],resultdict['floor'],resultdict['people'],resultdict['building']))
                    rows=cur.fetchall()
        
        
        strow_list=[]
        
        for row in rows:
            
            convert_str_row=[]
            
            for item in row:
                item=str(item)
                convert_str_row.append(item)
            
            strow=" ".join(convert_str_row)
            strow_list.append(strow)
            
        
        reply1="\n".join(strow_list)
        reply=reply1+"\n"+message
        
        
    

    
    
    
    conn.close()
    return reply,resultdict
        
        



if __name__ == '__main__':
    sentencelist=[]
    #sentencelist.append("Hi, could you help me book a meeting room with at least 6 seats ?")
    #sentencelist.append("Hi, I want to book a meeting room at 11 am for 4 people")
    #sentencelist.append("We will have an one hour meeting at 4pm for six people.")
    #sentencelist.append("I want to book a meeting room at 11am for 2 hours for 25 minutes(wrong expression)")
    #sentencelist.append("any meetingroom available this friday 4pm?")
    #sentencelist.append("I'd LIKE to book a room @ 4:30pm next monday for 20 minutes")
    #sentencelist.append("book @5pm tomorrow for 1 hour for 30 minutes(wrong expression)")
    sentencelist.append("book at 11:30 am today...tomorrow(wrong expression)")
    #sentencelist.append("I want to book a meeting room from 11am to 3pm for 5 people.")
    #sentencelist.append("I want to book a meeting room 3pm-5pm tomorrow")
    
    for sentence in sentencelist:
        print sentence
        print "#########################################"
        print "roomid roomname floor maxpeople building"
        print "#########################################"
        if type(select_database(sentence))==str:
            print 'yes'
        else:
            print 'no'


