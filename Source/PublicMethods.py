from Calenders.ICS.IcsService import IcsService
from Calenders.Google.GoogleEventService import EventService
from Model.Event import toJson
import sys

def isIcs(url):
    return str(url).startswith("http")

def main():
    args = sys.argv
    args.pop(0)
    eventList = []
    if (len(args) == 0):
        print("You must provide at least one Google Calender Id or Ics Calender URL!")
    else:
        for arg in args:
            if (isIcs(str(arg))):
                icsService = IcsService(str(arg))
                eventList = eventList + icsService.getEvents()
            else:
                evenService = EventService(str(arg))
                eventList = eventList + evenService.getEvents()
    print(toJson(eventList))


if __name__ == "__main__":
    main()





