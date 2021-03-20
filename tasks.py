import datetime
""" class Task():

    '''
    Input: name, due_date, topic
    stores: name, due_date_time, workdays, topic

    defineWorkdays(): will be used to pick which days the user wants to work on the taks, and for how long

    '''

    def __init__(self='hi', name='blank', due_date='1/1/2021'):
        due_date = due_date.split('/')
        self.name = name

        try:
            self.due_date_time = datetime.date(int(due_date[2]), int(due_date[1]), int(due_date[0]))
        except ValueError:
            print("Invalid Date entered. Please enter as 'DD,MM,YYYY  Default Date will now be entered.")
            self.due_date_time = datetime.date.today()

        self.work_days = []
        self.work_time = 0

    def defineWorkdays(self):
        pass

    def __str__(self):
        return self.name + ' is due on ' + str(self.due_date_time)
 """
def datetodatetime(date='1/1/2021'):
    split_date = date.split('/')
    print(split_date)
    try:
        objectdate = datetime.date(int(split_date[2]),int(split_date[1]),int(split_date[0]))
    except ValueError:
        print("Incorrect formatting in date. Setting as today")
        objectdate = datetime.date.today()
    return objectdate
