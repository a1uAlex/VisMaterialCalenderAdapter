from Calenders.Google.GoogleService import CalenderService
from Model.Event import Event

class EventService:

    def __init__(self, calenderId):
        self.calenderId = calenderId
        self.calenderService = CalenderService()

    def getEvents(self):
        service = self.calenderService.get_calendar_service()
        page_token = None
        eventList = []
        while True:
            events = service.events().list(calendarId=self.calenderId, pageToken=page_token, showDeleted=False,
                                           singleEvents=False).execute()
            colors = colors = service.colors().get().execute()
            background = service.calendarList().get(calendarId=self.calenderId).execute()['backgroundColor']
            foreground = service.calendarList().get(calendarId=self.calenderId).execute()['foregroundColor']
            for event in events['items']:
                eventBackground = background
                eventForeground = foreground
                if not event['status'] == 'cancelled':

                    if "colorId" in event:
                        eventBackground = str(colors['event'][event['colorId']]['background'])
                        eventForeground = str(colors['event'][event['colorId']]['foreground'])

                    eventList.append(
                        Event(event['summary'], eventBackground, eventForeground, str(next(iter(event['start'].values()))).split("+")[0],
                              str(next(iter(event['start'].values()))).split("+")[0]))

            page_token = events.get('nextPageToken')
            if not page_token:
                break

        return eventList