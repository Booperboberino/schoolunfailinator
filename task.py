import datetime as dt

# Classes

class Task():

    '''
    Input: name, due_date, topic

    stores: name, due_date_time, workdays, topic

    defineWorkdays(): will be used to pick which days the user wants to work on the taks, and for how long

    '''

    def __init__(self='hi', name='blank', due_date='1/1/2021'):
        self.name = name
        self.due_date = datetodatetime(due_date)
        self.work_days = []
        self.work_time = 0
        self.is_complete = False

    def defineWorkdays(self, workdays: list):
        self.work_days.extend(workdays)

    def __str__(self):
        return self.name + ' is due on ' + str(self.due_date)

    def setDay(self, date):
        self.due_date = date

# Functions

def datetodatetime(date='1/1/2021'):
    '''
    Input: raw date as string

    Output: datetime date class 
    '''
    split_date = date.split('/')
    try:
        objectdate = dt.date(int(split_date[2]),int(split_date[1]),int(split_date[0]))
    except ValueError:
        # To prevent crashing on incorrect date being passed, if an error is raised when the date strings are converted to int, today will be passed instead
        print("Incorrect formatting in date. Setting as today")
        objectdate = dt.date.today()
    return objectdate

    def whenToWork(due_date):
        # only on edit screen, show days until due date, then uncheck the ones that you don't want
        pass


aaaaaaaaaaaaaaa = True