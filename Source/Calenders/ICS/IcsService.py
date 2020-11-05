import requests
from ics import Calendar
from Model.Event import Event as MyEvent
import datetime

class IcsService:

    def __init__(self, url):
        self.url = url
        self.events = Calendar(requests.get(url).text).events


    def getEvents(self):
        eventList = []
        for event in self.events:
            if (event.end.datetime - event.begin.datetime) == datetime.timedelta(1,0,0,0,0,0,0):
                event.end = event.end.shift(days=-1)
                eventList.append(MyEvent(str(event.name), "#000000", "#ffffff", str(event.begin.date()),
                                         str(event.end.date())))
            else:
                eventList.append(MyEvent(str(event.name),"#000000","#ffffff",str(event.begin).split("+")[0],
                                         str(event.end).split("+")[0]))

        return eventList