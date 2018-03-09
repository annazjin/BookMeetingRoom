#!/usr/bin/python
#
# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import httplib2
import sys

from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
import socket             


# import smtp

client_id = "799671597294-q0m9n9f70nccch4d54e24oed587alm8n.apps.googleusercontent.com"
client_secret = "TgmU49zRsCaWq2Y3QkywEnJs"
scope = 'https://www.googleapis.com/auth/calendar'
flow = OAuth2WebServerFlow(client_id, client_secret, scope)

# smtp.py 
global organizer
# banana
global starttime,endtime
global meetingRoomAccount

s = socket.socket()         
# host = socket.gethostname() 
port = 12345                
s.bind(('127.0.0.1', port))       

s.listen(5)                
while True:
    c, addr = s.accept()    
    storage=Storage('anna.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = build('calendar', 'v3', http=http)

    try:
        
        event = {
        'summary': 'Google I/O 2018',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2018-05-28T09:00:00-07:00',
            # 'datetime':'%s',starttime
            # 'timeZone': 'Asia/Beijing',
        },
        'end': {
            'dateTime': '2018-05-28T17:00:00-07:00',
            # 'datetime':'%s',endtime
            # 'timeZone': 'Asia/Beijing',
        },
        'attendees': [
            {'email': '%s' %('anna.z.jin@pwc.com')}
        ],
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print 'Event created: %s' % (event.get('htmlLink'))

    except AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run'
            'the application to re-authorize')
    c.close()                
