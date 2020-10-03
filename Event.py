import json


class Event:
    def __init__(self, name, color, colorText, start, end):
        self.name = name
        self.color = color
        self.colorText = colorText
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.name) + ", " + str(self.color) + ", " + str(self.colorText) + ", " + str(
            self.start) + ", " + str(self.end)


def toJson(eventList):
    return json.dumps([event.__dict__ for event in eventList], indent=4)
