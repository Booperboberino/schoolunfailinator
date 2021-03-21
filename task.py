import datetime as dt

# Classes

class Task():

    '''
    Input: name, due_date, topic
    stores: name, due_date_time, topic

    defineWorkdays(): will be used to pick which days the user wants to work on the taks, and for how long

    '''

    def __init__(self, id: int, name: str, due_date: str):
        #self.id = findUniqueId()
        self.name = name
        self.due_date = datetodatetime(due_date)
        self.is_complete = False

    def __str__(self):
        return self.name + ' is due on ' + str(self.due_date)
    
    def setDay(self, date):
        self.due_date = date

class WorkOnTask():
     '''
     Input: respective task, date to work on, time

     '''

    #def __init__(self):
    #    pass


class TodaysTasks():
    #export list of each days task
    pass

# Functions

def datetodatetime(date='1/1/2021'):
    '''
    Input: raw date as string

    Output: datetime date class 
    '''
    int_dates = []
    try:
        for date in date.split('/'):
            int_dates.append(int(date))
    except ValueError:
        # To prevent crashing on incorrect date being passed, if an error is raised when the date strings are converted to int, today will be passed instead
        print("Incorrect formatting in date. Setting as today")
        objectdate = dt.date.today()
    else:
        objectdate = dt.date(int_dates[2],int_dates[0],int_dates[1])
    return objectdate

def whenToWork(task):
    # only on edit screen, show days until due date, then uncheck the ones that you don't want

    #variables to make things easier
    today = dt.date.today()
    due_date = task.due_date
    delta_date = due_date - today

    # Creating a list of dates to chose from
    potential_dates = []
    for i in range(0, delta_date.days+1):
        date = today + dt.timedelta(days=i)
        potential_dates.append(date)
        print(str(i) + ' ' + date.isoformat()) #CHANGE TO UI!!

    #Having user select dates (please change to UI)
    selected_dates = []
    need_input = True
    while need_input:
        try:
            new_number = input("Please select a number for a date above: (or type 'q' to finish)")
            if int(new_number) > delta_date.days+1 or new_number != 'q':
                raise EnvironmentError('Error not included')
        except EnvironmentError:
            print("You entered an invalid value, please try again.")
        else:
            if new_number == 'q':
                break
            else:
                selected_dates.append(int(new_number))
                
    # finish up by creating a work on task object for each one per day


my_task = Task('Hello', '4/21/2021')
print(my_task)
whenToWork(my_task)