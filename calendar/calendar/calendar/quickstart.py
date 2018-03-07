
from __future__ import print_function
import httplib2
import os
import datetime
import time
import re
import sys

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow



import connectDB
# import sendMail

client_id = "893327939461-1jdj062qeb3qh4hsve9kag1rdqpd1hed.apps.googleusercontent.com"
client_secret = "Vt8nW7r1BVk43iIFWjYrySMH"

# The scope URL for read/write access to a user's calendar data
scope = 'https://www.googleapis.com/auth/calendar'

# Create a flow object. This object holds the client_id, client_secret, and
# scope. It assists with OAuth 2.0 steps to get user authorization and
# credentials.
flow = OAuth2WebServerFlow(client_id, client_secret, scope)

global CalendarID
global localtime
localtime=time.mktime(datetime.datetime.now().timetuple())
print (localtime)


def get_credentials(filename):
    
    storage = Storage(filename)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())

    return credentials




def main(filename):
    
    credentials = get_credentials(filename)
    http = credentials.authorize(httplib2.Http())

    service = discovery.build('calendar', 'v3', http=http)


    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    oldevents=[]
    newevents=[]
    
    page_token=None
    while True:
        calendar_list=service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            CalendarID=calendar_list_entry['id']
            CalendarName=calendar_list_entry['summary']
            print (CalendarName)
            
        page_token=calendar_list.get('nextPageToken')
        if not page_token:
            break 
    

    # get all events then put them which status is 'needsAction'  into a list named 'newevents',
    # and put event which status is 'accepted' into a list name 'oldevents'
    def getNewevent():
        print('Getting all events')
        page_token=None
        while True:
            eventsResult = service.events().list(
                calendarId=CalendarID,pageToken=page_token).execute()
            events = eventsResult.get('items', [])
            # print(events)

            if not events:
                print('No upcoming events found.')
            for event in events:
                eventIds = event['id']
                everyevent=service.events().get(calendarId=CalendarID,eventId=eventIds).execute()
                attendees=everyevent.get('attendees',[])
                for attendee in attendees:
                    email=attendee['email']
                    if email==CalendarID:
                        restatus=attendee['responseStatus']
                        if restatus =='needsAction':
                            newevents.append(event)
                            
                        elif restatus =='accepted':
                            oldevents.append(event)
                
            page_token=eventsResult.get('nextPageToken')
            if not page_token:
                break  
        return oldevents,newevents
    

    # change to starttime and endtime into stamp 
    def change_timeStamp(event):
        start=event['start'].get('dateTime',event['start'].get('date'))
        sstart=start.encode()
        nsstart=re.compile('T')
        ansstart=nsstart.sub(' ',sstart)
        astart=ansstart[0:19]
        starttime=time.mktime(time.strptime(astart,'%Y-%m-%d %H:%M:%S'))
        

        end=event['end'].get('dateTime',event['end'].get('date'))
        send=end.encode()
        nsend=re.compile('T')
        asend=nsend.sub(' ',send)
        aend=asend[0:19]
        endtime=time.mktime(time.strptime(aend,'%Y-%m-%d %H:%M:%S'))
        

        return starttime,endtime

    def insertDB(geteventid,eventname,roomid,starttime,endtime,bookpeople):
        connectDB.connAndInsert(geteventid, eventname, roomid, starttime,endtime,bookpeople)

    
    def updateNewevent():
        oldevents,newevents=getNewevent()
        # if newevents:
        #     print (newevents)
        while newevents:
            for newevent in newevents:
                # retrieve strarttime,endtime,status,eventid of each new event
                nstart,nend = change_timeStamp(newevent)
                status=newevent['status']
                neweventIds = newevent['id']
                organizer=newevent['organizer'].get('email')
                sequence=newevent['sequence']
                print(sequence)
                print('newevent is')
                print(newevent['summary'])
                # retrieve responseStatus of attendee, the current account logged in to the gmail,  according to the 'neweventIds' just retrieved
                #  and assignment it to a variable named newrestatus.
                thenewevent=service.events().get(calendarId=CalendarID,eventId=neweventIds).execute()
                newattendees=thenewevent.get('attendees',[])
                for newattendee in newattendees:
                    email=newattendee['email']
                    if not(email==CalendarID):
                        continue
                    else:
                        # newrestatus=newattendee['responseStatus']
                        # return newrestatus
                        # decline the conflict event, and accept the valid event
                        n=0
                        if oldevents:
                            for oldevent in oldevents:
                                
                                print('now this new event is comparing to ')
                                print(oldevent['summary'])
                                ostart,oend = change_timeStamp(oldevent)
                                if () or (sequence!=0) or not((nstart <= ostart and nend <= ostart) or (nstart >= oend and nend >= oend)):
                                    newattendee['responseStatus']='declined'
                                    thenewevent['status']='cancelled'
                                    updated_event=service.events().update(calendarId=CalendarID,eventId=neweventIds,body=thenewevent).execute() 
                                    newevents.remove(newevent)
                                    print('the new event conflicted to this old event or updated events are not allowed, so declined it, so declined it')
                                    # print (updated_event)
                                    # newevent['status']='cancelled'                   
                                    break
                                else:
                                    n=n+1
                                    if n == len(oldevents):
                                        insertDB(neweventIds,newevent['summary'],CalendarID,nstart,nend,organizer)
                                        newattendee['responseStatus']='accepted'
                                        newevent['status']='confirmed'
                                        updated_event=service.events().update(calendarId=CalendarID,eventId=neweventIds,body=thenewevent).execute()
                                        oldevents.append(updated_event)
                                        newevents.remove(newevent)
                                        print('the new event did not conflict to this old event, so change the responseStatus of the event below into accpeted')
                                        # print(updated_event)
                                        # print('old events became to :')
                                        # print(oldevents)
                                        # print('now new event became to :')
                                        # print (newevents)
                                        break
                                    
                        else:
                            if sequence!=0:
                                newattendee['responseStatus']='declined'
                                thenewevent['status']='cancelled'
                                updated_event=service.events().update(calendarId=CalendarID,eventId=neweventIds,body=thenewevent).execute() 
                                newevents.remove(newevent)
                                print('updated events are not allowed, so declined it')
                                # print (updated_event)
                                # newevent['status']='cancelled'                   
                                break
                            else:
                                newattendee['responseStatus']='accepted'
                                sub=thenewevent['summary']+' Accepted'
                                content=sub
                                updated_event=service.events().update(calendarId=CalendarID,eventId=neweventIds,body=thenewevent).execute()
                                oldevents.append(updated_event)
                                insertDB(neweventIds,newevent['summary'],CalendarID,nstart,nend,organizer)
                                # sendMail.send_mail(to_list,sub,content)
                                print('there is no old events, then change the responseStatus of it ')
                                # print(updated_event)
                                # print('old events became to :')
                                # print(oldevents)
                                # print('now new evenupdated_event)
                                newevents.remove(newevent)
                                # print (newevents)
                                # print(oldevents)
                                # print (updated_event)
                                #######
        else:
            print ('have no events')

    updateNewevent()

      
    
         
if __name__ == '__main__':
    # main('PWCcredentials.dat')
    main('credentialsPWC.dat')
 