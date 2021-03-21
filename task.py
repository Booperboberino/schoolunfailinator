import datetime as dt

# Classes

class Task():

    '''
    Input: name, due_date, topic
    stores: name, due_date_time, topic

    defineWorkdays(): will be used to pick which days the user wants to work on the taks, and for how long

    '''

    def __init__(self, name='blank', due_date='1/1/2021', id=0):
        self.id = id
        self.name = name
        self.due_date = datetodatetime(due_date)
        self.is_complete = False

        # ended up putting workdays with the task becasue it didn't make much sense to have a separate object for them
        self.work_days = []
        self.work_time = 0

    def __str__(self):
        return self.name + ' is due on ' + str(self.due_date)
    
    def setDay(self, date):
        self.due_date = date

    def addWorkDays(self, date: list):
        self.work_days.extend(date)

    def setWorkTime(self, time):
        self.work_time = time


class TodaysTasks():
    '''
    input: a date, list of all tasks
    stores: list of all tasks on that day
    '''
    
    def __init__(self, date, tasks):
        self.task_list = []
        for task in tasks: # change to tasks.value for dictionary
            if task.due_date == date:
                self.task_list.append(task)
            else:
                for work_task_day in task.work_days:
                    if work_task_day == date:
                        self.task_list.append(task)
    

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

def daysToWork(task):
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

    #Having user select dates (please change to GUI)
    # Basically use the stuff from above to make a (pop up?) list where users can click a check mark from, then return a list full of the users check marks once they click submit
    selected_dates = []
    need_input = True
    while need_input:
        try:
            new_number = input("Please select a number for a date above: (or type 'q' to finish): ")
            int_number = int(new_number)
            if int_number > delta_date.days+1:
                raise EnvironmentError('Error not included')
        except EnvironmentError:
            print("You entered an invalid value, please try again.")
        except ValueError:
            if new_number == 'q':
                break
            else:
                print("ERROROROROROR")
        else:
            selected_dates.append(potential_dates[int(new_number)])
            print(selected_dates)

    # finish up by creating a work on task object for each one per day
    task.addWorkDays(selected_dates)

my_task = Task('Hello', '4/21/2021')
print(my_task)
daysToWork(my_task)