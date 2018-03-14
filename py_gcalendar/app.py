from flask import Flask,redirect
import httplib2
import webbrowser
import os
from apiclient.discovery import build
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import OAuth2WebServerFlow
from flask import request

app = Flask(__name__)

client_id = "799671597294-q0m9n9f70nccch4d54e24oed587alm8n.apps.googleusercontent.com"
client_secret = "TgmU49zRsCaWq2Y3QkywEnJs"
scope = 'https://www.googleapis.com/auth/calendar'
flow = OAuth2WebServerFlow(client_id, client_secret, scope)




@app.route("/",methods=["GET","POST"])
def index():
  organizer=request.args.get("organizer")
  starttime=request.args.get("starttime")
  endtime=request.args.get("endtime")
  meetingRoomAccount=request.args.get("meetingRoomAccount")

  home_dir = os.getcwd()
  credential_dir = os.path.join(home_dir, 'credentials')
  if not os.path.exists(credential_dir):
      os.makedirs(credential_dir)
  credential_path = os.path.join(credential_dir,
                                  '%s.dat' % (organizer))


  storage = Storage(credential_path)
  # storage=Storage('anna.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
      credentials = tools.run_flow(flow, storage, tools.argparser.parse_args())
  http = httplib2.Http()
  http = credentials.authorize(http)
  service = build('calendar', 'v3', http=http)

  # page_token=None
  # while True:
  #     calendar_list=service.calendarList().list(pageToken=page_token).execute()
  #     for calendar_list_entry in calendar_list['items']:
  #         CalendarID=calendar_list_entry['id']
  #         CalendarName=calendar_list_entry['summary']
  #         print (CalendarID)
          
          
  #     page_token=calendar_list.get('nextPageToken')
  #     if not page_token:
  #         break 
  try:
      
      event = {
      'summary': 'Google I/O 2018',
      'description': 'A chance to hear more about Google\'s developer products.',
      'start': {
          # 'dateTime': '2018-05-29T09:00:00-07:00',
          'dateTime':'%s'%(starttime)
          # 'timeZone': "America/Los_Angeles",
      },
      'end': {
          # 'dateTime': '2018-05-29T18:00:00-07:00',
          'dateTime':'%s'%(endtime)
          # 'timeZone': "America/Los_Angeles",
      },
      'attendees': [
          {'email': '%s'%(meetingRoomAccount)}
      ],
      }
      even = service.events().insert(calendarId=organizer, body=event).execute()
      url=even.get('htmlLink')
      # print 'Event created: %s' % (even.get('htmlLink'))
    #   webbrowser.open(url)
      return redirect(url)

  except AccessTokenRefreshError:
      print ('The credentials have been revoked or expired, please re-run'
          'the application to re-authorize')

if __name__ == "__main__":
  app.run()

