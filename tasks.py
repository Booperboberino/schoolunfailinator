
class Task():

    '''
    Input:

    '''

    def __init__(self, name, time, date, rangee, topic):
        self.name = name
        self.time = time # probably should do something with datetime here to make this better
        self.date = date # again datetime
        self.range = rangee
        self.topic = topic