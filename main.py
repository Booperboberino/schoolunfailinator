from loader import Loader as ld
import tkinter as tk
from tkinter import Frame, simpledialog
import datetime
import taskHandler
Loader = ld()

arr = []
temp = str(datetime.date.today())
temp = temp.split("-")
selectedDate = {"year":0,"month":0,"day":0}
jeff = 0
for i in selectedDate:
    selectedDate[i] = temp[jeff]
    jeff += 1
#print(selectedDate)

squareRow = 0
squareColumn = 0
dark_color = "midnight blue"
light_color = "white"
#---------------HELPER CLASSES---------------------------


# TO DO LIST

class listItem:
    #The class for each individual list object, containing text and a little checkbox thingy.
    #Contains a method to make the checkbox work.

    #Takes parameters for the item name and the length of time in minutes, plus some other gui stuff. 

    def __init__(self, itemname, timelength, parentWidget, r, c, checked = False):
        self.itemname = itemname
        self.itemString = itemname.capitalize() + " (" +str(timelength)+" Minutes)"

        self.bullet = Frame(parentWidget, padx= 20, pady = 5, bg = dark_color)
        self.bullet.grid(row = r, column = c)

        self.bulletLabel = tk.Label(self.bullet, text = self.itemString, padx = 20, bg = dark_color, fg = light_color)
        self.bulletLabel.grid(row = 0, column = 0)
        self.checkbox = tk.Button(self.bullet, text = "  ", bg = "white", command = self.switchButton, padx = 5)
        self.checkbox.grid(row = 0, column = 1)
        self.checked = checked
        self.buttonStatus = "white"
        if checked: self.switchButton() #allows task to start completed (useful for getting one from memory)
        
    def switchButton(self): #switches button color and changes if a task is done or not
        global calendarDemo
        global squareRow
        global squareColumn
        if self.buttonStatus == "white":
            self.checkbox.config(bg = "black")
            self.buttonStatus = "black"
            self.checked = True
        else:
            self.checkbox.config(bg = "white")
            self.buttonStatus = "white"
            self.checked = False
        self.updateComplete()
        calendarDemo.dayGrid[squareRow][squareColumn].updateTasksLeft()

        
    def __str__(self):
        return self.itemString

    def clear(self): #some of Brian's sorcery that helps to do list update
        self.bullet.destroy()
        self.bulletLabel.destroy()
        self.checkbox.destroy()

    def updateComplete(self): #changes boolean value of task in .json file to match check box
        global selectedDate
        global update
        Loader.editToDo(selectedDate["year"],selectedDate["month"],selectedDate["day"],self.itemname,self.checked)




#CALENDAR

class calendarDay:
    #This class contains the individual day buttons. Need to expand the onClick function to alter the todo list. These objects are automatically made by calenderGrid.

    def __init__(self, dayNum, tasksDone, tasksToDo, parentgrid, row, col):
        self.parentgrid = parentgrid
        self.row = row
        self.column = col
        self.dayNum = dayNum
        self.button = tk.Button(parentgrid, text = str(dayNum)+"\nDone: "+str(tasksDone)+"\nTasks: "+str(tasksToDo), command = self.onClick,height = 5, width = 10)
        self.button.grid(row = row, column = col)
        self.currentlyPressed = False
        
    def onClick(self):
        global squareColumn
        global squareRow
        global selectedDate
        global calendarDemo

        #switch from light to dark when pressed. 
        if not self.currentlyPressed:
            squareColumn = self.column
            squareRow = self.row
            calendarDemo.clearClicked()
            self.button.config(bg = "black", fg = "white")
            self.currentlyPressed = True
            temp = ""
            if self.dayNum < 10: temp = "0"
            selectedDate["day"] = temp + str(self.dayNum) #changes day of date to calendar day
            updateToDo() #updates toDo list for that day
        else:
            self.button.config(bg = "white", fg = "black")
            self.currentlyPressed = False
            selectedDate["day"] = "0" #changes day to day 0, supposed to be some blank day so that declicking a day removes its todo list
            updateToDo()
        print(selectedDate)

    def unClick(self): #unclicks a button
            self.button.config(bg = "white", fg = "black")
            self.currentlyPressed = False

    def updateTasksLeft(self):
        global selectedDate
        data = Loader.getDayInfo(selectedDate["year"],selectedDate["month"],selectedDate["day"])
        if data != {}:
            self.button['text'] = str(selectedDate["day"])+"\nDone: "+str(data["completed"])+"\nTasks: "+str(data["remaining"]) 


class calendarGrid:
    
    #Container for a grid of calenderDay objects. Takes parameters to set up a calendar for a given month. See the end of the file for what each param means. 

    def __init__(self, month, days, startcol, parentgrid):

        self.month = month
        self.dayGrid = []
        self.startcol = startcol
        self.monthTitle = tk.Label(parentgrid, text = month, bg = dark_color, fg = light_color).grid(row = 0, column = 0)
        self.calendar = Frame(parentgrid, bg = dark_color)
        self.calendar.grid(row = 1, column = 0)
        
        self.addDays(days)

    #Method that creates the actual calendar. May need to be modifed to give each day a list of tasks that can be displayed, or at the very minium a way of determing the tasks for each day. 
    
    def addDays(self, days):
        global selectedDate
        print(selectedDate)

        dayCounter = 0
        
        for r in range(5):
            self.dayGrid.append([])
            for c in range(7):

                if r == 0 and c < self.startcol:
                    self.dayGrid[r].append(calendarDay("/", "/", "/", self.calendar, r, c)) 
                elif dayCounter <= days:
                    alteredDays = ""
                    if dayCounter < 10: alteredDays = "0"
                    temp = Loader.getDayInfo(selectedDate["year"],selectedDate["month"],alteredDays+str(dayCounter))
                    if temp == {}:
                        completed = ""
                        remaining = ""
                    else:
                        completed = str(temp["completed"])
                        remaining = str(temp["remaining"])
                    self.dayGrid[r].append(calendarDay(dayCounter, completed, remaining, self.calendar, r, c)) #The three is a placeholder.
                dayCounter += 1
    
    def clearClicked(self): #unclicks all tiles to prevent creation of smiley faces and other images on the calendar
        for r in range(len(self.dayGrid)):
            for c in range(len(self.dayGrid[r])):
                self.dayGrid[r][c].unClick()     

#----------------------ADD / DEL ASSIGNMENT FUNCTIONS-----------

def isValidDate(date):
    try:
        if len(date) != 10 or int(date[0:2]) > 12 or int(date[0:2]) <= 0 or date[2] != "/" or int(date[3:5]) > 31 or int(date[3:5]) <= 0 or date[5] != "/":
            return False
        return True
    except:
        return False

def onAddEventClick():
    #get information from user via popup: name, due date [MM/DD/YYYY]
    eventName = simpledialog.askstring("Input","What is the assignment name? ",parent=root)
    eventDate = "not a correct date"

    
    while not isValidDate(eventDate):
        eventDate = simpledialog.askstring("Input","When is the assignment due? [mm/dd/yyyy]",parent=root)

    try:
        taskHandler.addTask(eventName, eventDate)

        #get list of potential dates using daystowork, maybe have to assume all days / no weekends? 
    except:
        pass
    
    #get list of potential dates using daystowork, maybe have to assume all days / no weekends? 


def onDelEventClick():
    eventName = simpledialog.askstring("Input","What is the assignment name? ",parent=root)

    Loader.removeToDoItem(selectedDate["year"], selectedDate["month"], selectedDate["day"], eventName.lower())

def updateToDo(): #updates the todo list on the screen
    global selectedDate
    global arr
    for i in arr:
        i.clear()
    arr = []
    dayTasks = Loader.getToDo(selectedDate["year"],selectedDate["month"],selectedDate["day"]) #gets selected day's tasks
    jeff = 1 #count variable
    for i in dayTasks:#sets up todolist
        arr.append(listItem(i,0,todoFrame,jeff,0,dayTasks[i]))
        jeff +=1

      
#------------------THE ACTUAL CODE THAT MAKES THE WINDOW EXIST----------------------


#These lines create the window itself, and title it.
root = tk.Tk()
root.title("Calendar")
root.configure(bg = dark_color)

#Creates two "frames," one for the to-do list and one for the calendar. This allows me to align their internal widgeths more easily.
calendarFrame = Frame(root, bg = dark_color)
todoFrame = Frame(root, bg = dark_color)
calendarFrame.grid(row = 0, column = 0)
todoFrame.grid(row = 0, column = 1)

"""
#These are hardcoded listItem objects for demonstration purposes. THIS IS NOT THE FINAL PRODUCT. Currently unsure how clicking on the day will update the toDoList. 

for i in range(1, 8):
    arr.append(listItem("Item "+str(i), i * 10, todoFrame, i, 0))
"""
updateToDo()


#This creates the calendar.
#Placeholders:  'March' - will have to be replaced with a string of the current month
#               '31' - will be replaced with integer of days in the current month
#               '1' - Will have to be replaced with the integer of the first weekday of the month. 0 = Sunday, 1 = Monday, 2 = Tuesday, etc.
#don't touch calenderFrame
calendarDemo = calendarGrid("March", 31, 1, calendarFrame)


#These are the add/remove assignment buttons. Edit the "command" parameters with the appropriate function. If the function has its own parameters, use this... command = lambda: functionName(param)
addAssignmentButton = tk.Button(root, text = "Add Assignment", width = 25, command = onAddEventClick)
addAssignmentButton.grid(row = 2, column = 0)

delAssignmentButton = tk.Button(root, text = "Remove Assignment", width = 25, command = onDelEventClick)
delAssignmentButton.grid(row = 2, column = 1)


#makes the actual thing work
root.mainloop()
