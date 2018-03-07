# -*- coding: utf-8 -*-


try:
    import sys
    import re
    import string
    import os
    import mx.DateTime as DateTime
    import time
except ImportError:
    print "requires sys re string os mx.DateTime time"


#------------------------------------------预处理定义与函数-------------------------------------------
reload(sys)
sys.setdefaultencoding('utf-8')
###predefination and functions for get_regular_precise_time###
hm = "\d+:\d+"
apm="[ap]m"

#get 8:00 am/9:00 pm
def get_precise_time_p1(sentence,precise_time_list):
    
    regxp1="(" + hm + " (" + "am" + "))"
    regxp12="(" + hm + " (" + "pm" + "))"
    regxp2="(" + hm +"("+ "am" + "))"
    regxp22="(" + hm +"("+ "pm" + "))"    
    
    reg1 = re.compile(regxp1)
    reg12 = re.compile(regxp12)
    reg2=re.compile(regxp2)
    reg22=re.compile(regxp22)



    precise_time=precise_time_list
    
    new_sentence=sentence
    
    found = reg1.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)

    found = reg12.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)
    

    found = reg2.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)  
    
    found = reg22.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)
    
    
    for item in precise_time:
        new_sentence=re.sub(item,"",new_sentence)
    
    return new_sentence,precise_time
    pass

#get 1 am /9 pm
def get_precise_time_p2(sentence,precise_time_list):
    regxp3="(" +"\d+"+" ("+"am" + "))"
    regxp32="(" +"\d+"+" ("+"pm" + "))"
    regxp4="(" +"\d+"+"("+"am" + "))"
    regxp42="(" +"\d+"+"("+"pm" + "))"


    reg3=re.compile(regxp3)
    reg32=re.compile(regxp32)
    reg4=re.compile(regxp4)
    reg42=re.compile(regxp42)
    
    precise_time=precise_time_list
    new_sentence=sentence

    found = reg3.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)
    
    found = reg4.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:

        precise_time.append(item)
    
    
    
    found = reg32.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)
    
    found = reg42.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        precise_time.append(item)
    
    for item in precise_time:
        new_sentence=re.sub(item,"",new_sentence)
    
    return new_sentence,precise_time

#get 15:00
def get_precise_time_p3(sentence,precise_time_list):
    
    new_sentence=sentence
    precise_time=precise_time_list
    
    reg=re.compile(hm)
    found=reg.findall(sentence)
    for item in found:
        precise_time.append(item)

    for item in precise_time:
        new_sentence=re.sub(item,"",new_sentence)
    
    return new_sentence,precise_time

    pass


###predefination and functions for get_regular_precise_date###
day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
rel_day = "(today|tomorrow|the day after tomorrow)"
prep = "(this|next)"
hashweekdays = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6}


###predefination and functions for get_regular_continued_time###
contime = "(minute|hour|day|week)"
numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
        eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
        eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
        ninety|hundred|thousand)"

def hashnum(number):
    if re.match(r'one|^a\b', number, re.IGNORECASE):
        return 1
    if re.match(r'two', number, re.IGNORECASE):
        return 2
    if re.match(r'three', number, re.IGNORECASE):
        return 3
    if re.match(r'four', number, re.IGNORECASE):
        return 4
    if re.match(r'five', number, re.IGNORECASE):
        return 5
    if re.match(r'six', number, re.IGNORECASE):
        return 6
    if re.match(r'seven', number, re.IGNORECASE):
        return 7
    if re.match(r'eight', number, re.IGNORECASE):
        return 8
    if re.match(r'nine', number, re.IGNORECASE):
        return 9
    if re.match(r'ten', number, re.IGNORECASE):
        return 10
    if re.match(r'eleven', number, re.IGNORECASE):
        return 11
    if re.match(r'twelve', number, re.IGNORECASE):
        return 12
    if re.match(r'thirteen', number, re.IGNORECASE):
        return 13
    if re.match(r'fourteen', number, re.IGNORECASE):
        return 14
    if re.match(r'fifteen', number, re.IGNORECASE):
        return 15
    if re.match(r'sixteen', number, re.IGNORECASE):
        return 16
    if re.match(r'seventeen', number, re.IGNORECASE):
        return 17
    if re.match(r'eighteen', number, re.IGNORECASE):
        return 18
    if re.match(r'nineteen', number, re.IGNORECASE):
        return 19
    if re.match(r'twenty', number, re.IGNORECASE):
        return 20
    if re.match(r'thirty', number, re.IGNORECASE):
        return 30
    if re.match(r'forty', number, re.IGNORECASE):
        return 40
    if re.match(r'fifty', number, re.IGNORECASE):
        return 50
    if re.match(r'sixty', number, re.IGNORECASE):
        return 60
    if re.match(r'seventy', number, re.IGNORECASE):
        return 70
    if re.match(r'eighty', number, re.IGNORECASE):
        return 80
    if re.match(r'ninety', number, re.IGNORECASE):
        return 90
    if re.match(r'hundred', number, re.IGNORECASE):
        return 100
    if re.match(r'thousand', number, re.IGNORECASE):
        return 1000
###predefination for get_people###
peoplexp = "(people|seat)"
#------------------------------------------------预处理定义与函数-----------------------------------------------------





#-------------------------------------------------功能函数-----------------------------------------------------
#预处理：转小写、去多余空格
def preproccess(sentence):
    lowersentence=sentence.lower()
    text=re.sub(r"\s{2,}", " ", lowersentence)
    return text

#得到24小时制%H:%M（str）的“准确时间”list
def get_regular_precise_time(sentence):
    #由于正则匹配的重复，将准确时间的抓取分为三部分，每抓取一种准确时间后，在句子中删掉
    #初始化抓到的准确时间列表
    precise_time=[]
    get_precise_time_1=get_precise_time_p1(preproccess(sentence),precise_time)
    get_precise_time_2=get_precise_time_p2(get_precise_time_1[0],get_precise_time_1[1])
    get_precise_time_3=get_precise_time_p3(get_precise_time_2[0],get_precise_time_2[1])
    
    #未经格式化的所有抓出来的准确时间
    timelist= get_precise_time_3[1]
    
    
    #初始化标准格式准确时间列表
    rtimelist=[]
    for item in timelist:

        if ("pm" in item):
            
            minute=""
            if re.search("(\:)(\d+)",item):

                minute=re.search("(\:)(\d+)",item).group(2)
            else:
                minute="00" 
            
            hour=""
            for i in item:
                p1=re.compile('[0-9]')
                if p1.match(i):
                    hour=hour+i

                else:
                    break
            
            inthour=int(hour)
            if inthour>=1 and inthour<=11:
                inthour=inthour+12
                hour=str(inthour)
            else:
                hour=hour #出现不符合1-12a/pm的输入时，默认是24小时制
        
            item=hour+":"+minute
            rtimelist.append(item)        
        
        
        
        elif ("am" in item):
            
            minute=""
            if re.search("(\:)(\d+)",item):

                minute=re.search("(\:)(\d+)",item).group(2)
            else:
                minute="00" 
            
            hour=""
            for i in item:
                p1=re.compile('[0-9]')
                if p1.match(i):
                    hour=hour+i

                else:
                    break
            inthour=int(hour)
            
            if inthour==12:
                hour="00"
            elif inthour<12 and inthour>=1:
                hour=hour
                pass
            else:
                hour=hour #出现不符合1-12a/pm的输入时，默认是24小时制

            item=hour+":"+minute
            rtimelist.append(item)

        else:
            item=item
            rtimelist.append(item)
                
                

    return rtimelist

#得到YYYY-MM-DD（str）的“日期”list   
def get_regular_date(sentence):
    
    datelist=[]
    rdatelist=[]
    
    base_date=DateTime.today()
    
    regxp1 = "(" + prep + " (" + day + "))"

    reg1=re.compile(regxp1)
    reg2=re.compile(rel_day)

    found = reg1.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        datelist.append(item)

    found = reg2.findall(sentence)
    for item in found:
        datelist.append(item)

    
    #日期->YYYY-MM-DD
    for item in datelist:
        
        if re.match(r'today', item):
            item = str(base_date)
            
            item = re.sub(r'\s.*', '', item)
            rdatelist.append(item)
        elif re.match(r'tomorrow',item):
        
            item=str(base_date + DateTime.RelativeDateTime(days=+1))
            
            item = re.sub(r'\s.*', '', item)
            rdatelist.append(item)
        elif re.match(r'the day after tomorrow',item):
            item=str(base_date+DateTime.RelativeDateTime(days=+2))
            item = re.sub(r'\s.*', '', item)
            rdatelist.append(item)
        
        # Weekday in the current week.
        elif re.match(r'this ' + day, item):
            days = hashweekdays[item.split()[1]]
            item = str(base_date + DateTime.RelativeDateTime(weeks=0, \
                            weekday=(days,0)))
            item = re.sub(r'\s.*', '', item)
            rdatelist.append(item)
            
        # Weekday in the following week.
        elif re.match(r'next ' + day, item):
            days = hashweekdays[item.split()[1]]
            item = str(base_date + DateTime.RelativeDateTime(weeks=+1, \
                            weekday=(days,0)))
            item = re.sub(r'\s.*', '', item)
            rdatelist.append(item)
        else:
            continue
            
        
            
        
        
    return rdatelist

#得到秒数（int）的“持续时间”list
def get_regular_continued_time(sentence):
    
    continued_time=[]
    all_int_time=[]
    rcontinuelist=[]
    
    regxp1 = "((\d+|(" + numbers + "[-\s]?)+) " + contime + "s?" + ")"
    
    reg1 = re.compile(regxp1)

    found = reg1.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        continued_time.append(item)

    #文字表达转数字表达：eg. twenty five days ago --> 25 days ago
    for item in continued_time:
        
        
        if re.search(numbers, item, re.IGNORECASE):
            split_item = re.split(r'\s(?=days?|hours?|minutes?|weeks?)', \
                                                            item, re.IGNORECASE)
            value = split_item[0]
            unit = split_item[1]
            num_list = map(lambda s:hashnum(s),re.findall(numbers + '+', \
                                        value, re.IGNORECASE))
            item = `sum(num_list)` + ' ' + unit
            all_int_time.append(item)
        else:
            all_int_time.append(item)


    for item in all_int_time:
        
        if re.match(r'\d+ days?', item, re.IGNORECASE):
            offset = int(re.split(r'\s', item)[0])
            second=offset*24*60*60   #offset天有多少秒？
            rcontinuelist.append(second)
            pass
        elif re.match(r'\d+ hours?', item, re.IGNORECASE):
            
            offset = int(re.split(r'\s', item)[0])
            second=offset*60*60   #offset小时有多少秒？
            rcontinuelist.append(second)
            pass
        elif re.match(r'\d+ weeks?', item, re.IGNORECASE):
            offset = int(re.split(r'\s', item)[0])
            second=offset*7*24*60*60   #offset周有多少秒？
            rcontinuelist.append(second)
            pass
        elif re.match(r'\d+ minutes?', item, re.IGNORECASE):
            offset = int(re.split(r'\s', item)[0])
            second=offset*60   #offset分钟有多少秒？
            rcontinuelist.append(second)
            pass
        else:
            continue
        

    
    
    #rcontinuelist是一个int的list，返回值为秒数（int）
    return rcontinuelist

#得到int的人数list
def get_people(sentence):

    people=[]
    int_people=[]
    rpeoplelist=[]
    
    #5/five seats/people
    regxp1 = "((\d+|(" + numbers + "[-\s]?)+) " + peoplexp + "s?" + ")"
    #5-17ish people/seats
    regxp2="((\d+\-\d+ish("+  "[-\s]?)+) "+peoplexp+ "s?" + ")"
    
    reg1 = re.compile(regxp1)
    reg2=re.compile(regxp2)
    
    
    found = reg1.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        people.append(item)
    
    found = reg2.findall(sentence)
    found = [a[0] for a in found if len(a) > 1]
    for item in found:
        people.append(item)

    
    # five seats-->5 seats
    for item in people:
        
        
        if re.search(numbers, item, re.IGNORECASE):
            split_item = re.split(r'\s(?=peoples?|seats?)', \
                                                            item, re.IGNORECASE)
            value = split_item[0]
            unit = split_item[1]
            num_list = map(lambda s:hashnum(s),re.findall(numbers + '+', \
                                        value, re.IGNORECASE))
            item = `sum(num_list)` + ' ' + unit
            int_people.append(item)
        else:
            int_people.append(item)
    
    

    for item in int_people:
        
        if re.match(r'\d+ peoples?', item, re.IGNORECASE):
            peoplenumber = int(re.split(r'\s', item)[0])   
            rpeoplelist.append(peoplenumber)
            pass
        
        elif re.match(r'\d+ seats?', item, re.IGNORECASE):
            peoplenumber = int(re.split(r'\s', item)[0])   
            rpeoplelist.append(peoplenumber)
            pass

        elif re.match(r'\d+-\d+ish '+peoplexp+r's?',item):
            peoplenumber=int(re.split('\-|ish',item)[1])
            rpeoplelist.append(peoplenumber)
            pass
        else:
            continue
    
    
    return rpeoplelist

#得到string的楼号list
def get_building(sentence):
    buildinglist=[]
    rbuildinglist=[]
    
    exp1="(building [a-z])"
    reg1=re.compile(exp1)

    found = reg1.findall(sentence)
    for item in found:
        buildinglist.append(item)

    
    for item in buildinglist:
        number=re.split(r'\s',item)[1]
        rbuildinglist.append(number)
    
    return rbuildinglist

#得到int的楼层list
def get_floor(sentence):
    floorlist=[]
    rfloorlist=[]
    
    floor="\d+f"
    floor2="\d+st floor|\d+nd floor|\d+rd floor|\d+th floor"
    
    reg1=re.compile(floor)
    reg2=re.compile(floor2)

    found = reg1.findall(sentence)
    for item in found:
        floorlist.append(item)

    found = reg2.findall(sentence)
    for item in found:
        floorlist.append(item)

    
    for item in floorlist:
        if re.match(r'\d+f',item):
            rfloor=int(re.split('f',item)[0])
            rfloorlist.append(rfloor)
        elif re.match(r'\d+st floor|\d+nd floor|\d+rd floor|\d+th floor',item):
            rfloor=int(re.split('st|nd|rd|th',item)[0])
            rfloorlist.append(rfloor)
        else:
            continue

        
    
    return rfloorlist
#----------------------------------------------- 功能函数--------------------------------------------------------------



#------------------------------------------------主函数----------------------------------------------------------------
def parser(sentence):

    resultdict={'starttime':0,'endtime':0,'people':0,'building':0,'floor':0}
    message="null"
    
    starttime=0
    endtime=0
    people=0
    building=0
    floor=0
    
    rsentence=preproccess(sentence)

    precise_time_list=get_regular_precise_time(sentence)

    
    if len(precise_time_list)==0:
        message= "Can not find 'specific time', nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."
    elif len(precise_time_list)==1:
        
        
        date_list=get_regular_date(rsentence)
        
        if len(date_list)==0:
            
            date=str(DateTime.today())#未提供日期时默认是今天
            date=re.sub(r'\s.*', '', date)

            starttime=date+" "+precise_time_list[0]
            
            #print starttime
            starttime=time.mktime(time.strptime(starttime,"%Y-%m-%d %H:%M"))
            
            continue_time_list=get_regular_continued_time(sentence)
            
            if len(continue_time_list)==0:
                #message= "No duration found, how long the meeting lasts? I Booked an hour for you as default, please send me email if it is not correct."
                endtime=starttime+3600
            elif len(continue_time_list)==1:
                endtime=starttime+continue_time_list[0]
            else:
                message= "More than one duration found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."

            resultdict['starttime']=starttime
            resultdict['endtime']=endtime

            
                
            
        elif len(date_list)==1:
            
            date=date_list[0]
            
            starttime=date+" "+precise_time_list[0]
            
            starttime=time.mktime(time.strptime(starttime,"%Y-%m-%d %H:%M"))
            
            continue_time_list=get_regular_continued_time(sentence)
            
            if len(continue_time_list)==0:
                #message= "No duration found, how long the meeting lasts? I Booked an hour for you as default, please send me email if it is not correct."
                endtime=starttime+3600
            elif len(continue_time_list)==1:
                endtime=starttime+continue_time_list[0]
            else:
                message= "More than one duration found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."

            resultdict['starttime']=starttime
            resultdict['endtime']=endtime
        
        else:
            message= "More than one 'date' found, is there a cross-day query? Nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."
        
    elif len(precise_time_list)==2:
        
        date_list=get_regular_date(rsentence)
        if len(date_list)==0:
            
            date=str(DateTime.today())#未提供日期时默认是今天
            date=re.sub(r'\s.*', '', date)
            time1=date+" "+precise_time_list[0]
            time2=date+" "+precise_time_list[1]
            time1=time.mktime(time.strptime(time1,"%Y-%m-%d %H:%M"))
            time2=time.mktime(time.strptime(time2,"%Y-%m-%d %H:%M"))
            
            if time1>=time2:
                endtime=time1
                starttime=time2
            else:
                endtime=time2
                starttime=time1

            resultdict['starttime']=starttime
            resultdict['endtime']=endtime    
        
        elif len(date_list)==1:
            
            date=date_list[0]
            
            time1=date+" "+precise_time_list[0]
            time2=date+" "+precise_time_list[1]
            time1=time.mktime(time.strptime(time1,"%Y-%m-%d %H:%M"))
            time2=time.mktime(time.strptime(time2,"%Y-%m-%d %H:%M"))
            
            if time1>=time2:
                endtime=time1
                starttime=time2
            else:
                endtime=time2
                starttime=time1

            resultdict['starttime']=starttime
            resultdict['endtime']=endtime 
        
        else:
            message= "More than one 'date' found, is there a cross-day query? Nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."
        
    else:
        message= "More than one 'specific time' found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people."
        
    
    #找楼号
    building_list=get_building(sentence)
    if len(building_list)==0:
        building='NULL'
    elif len(building_list)==1:
        building=building_list[0]
    else:
        message= "More than one 'building number' found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people in building A on 7F."

    resultdict['building']=building
    
    #找人数
    people_list=get_people(sentence)
    if len(people_list)==0:
        people='NULL'
    elif len(people_list)==1:
        people=people_list[0]
    else:
        message= "More than one 'number of participants' found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people in building A on 7F."
    resultdict['people']=people
    
    #找楼层
    floor_list=get_floor(sentence)
    if len(floor_list)==0:
        floor='NULL'
    elif len(floor_list)==1:
        floor=floor_list[0]
    else:
        message= "More than one 'floor' found, nlp process can not be carried out, please try to follow the example sentence."+"\n"+"example sentence: I want to book a meeting room from 11am to 3pm for 5 people in building A on 7F."
    
    resultdict['floor']=floor
    
    return resultdict,message
    


#------------------------------------------------主函数---------------------------------------------------------