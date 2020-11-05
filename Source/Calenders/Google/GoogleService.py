import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class CalenderService:

    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.CREDENTIALS_FILE = '../Ressources/credentials.json'

    def get_calendar_service(self):
       creds = None

       if os.path.exists('../Ressources/token.pickle'):
           with open('../Ressources/token.pickle', 'rb') as token:
               creds = pickle.load(token)

       if not creds or not creds.valid:
           if creds and creds.expired and creds.refresh_token:
               creds.refresh(Request())
           else:
               flow = InstalledAppFlow.from_client_secrets_file(
                   self.CREDENTIALS_FILE, self.SCOPES)
               creds = flow.run_local_server(port=0)

           with open('../Ressources/token.pickle', 'wb') as token:
               pickle.dump(creds, token)

       service = build('calendar', 'v3', credentials=creds)
       return service