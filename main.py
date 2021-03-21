import tkinter as tk
from tkinter import Frame

dark_color = "midnight blue"
light_color = "white"

#---------------HELPER CLASSES---------------------------


# TO DO LIST

class listItem:
    #The class for each individual list object, containing text and a little checkbox thingy.
    #Contains a method to make the checkbox work.

    #Takes parameters for the item name and the length of time in minutes, plus some other gui stuff. 

    def __init__(self, itemname, timelength, parentWidget, r, c):
        self.itemString = itemname.capitalize() + " (" +str(timelength)+" Minutes)"

        self.bullet = Frame(parentWidget, padx= 20, pady = 5, bg = dark_color)
        self.bullet.grid(row = r, column = c)

        self.bulletLabel = tk.Label(self.bullet, text = self.itemString, padx = 20, bg = dark_color, fg = light_color).grid(row = 0, column = 0)
        self.checkbox = tk.Button(self.bullet, text = "  ", bg = "white", command = self.switchButton, padx = 5)
        self.checkbox.grid(row = 0, column = 1)

        self.buttonStatus = "white"
        
    def switchButton(self):
        if self.buttonStatus == "white":
            self.checkbox.config(bg = "black")
            self.buttonStatus = "black"
        else:
            self.checkbox.config(bg = "white")
            self.buttonStatus = "white"
        
    def __str__(self):
        return self.itemString


#CALENDAR

class calendarDay:
    #This class contains the individual day buttons. Need to expand the onClick function to alter the todo list. These objects are automatically made by calenderGrid.

    def __init__(self, dayNum, tasksToDo, parentgrid, row, col):
        
        self.button = tk.Button(parentgrid, text = str(dayNum)+"\n\nTasks: "+str(tasksToDo), command = self.onClick)
        self.button.grid(row = row, column = col)
        self.currentlyPressed = False
        
    def onClick(self):
        #switch from light to dark when pressed. 
        if not self.currentlyPressed:
            self.button.config(bg = "black", fg = "white")
            self.currentlyPressed = True
        else:
            self.button.config(bg = "white", fg = "black")
            self.currentlyPressed = False

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

        dayCounter = 0
        
        for r in range(5):
            self.dayGrid.append([])
            for c in range(7):

                if r == 0 and c < self.startcol:
                    self.dayGrid[r].append(calendarDay("/", "/", self.calendar, r, c)) 
                elif dayCounter <= days:
                    self.dayGrid[r].append(calendarDay(dayCounter, 3, self.calendar, r, c)) #The three is a placeholder.
                dayCounter += 1
                
    
#------------------THE ACTUAL CODE THAT MAKES THE WINDOW EXIST----------------------


#These lines create the window itself, and title it.
root = tk.Tk()
root.title("GUI prototype")
root.configure(bg = dark_color)

#Creates two "frames," one for the to-do list and one for the calendar. This allows me to align their internal widgeths more easily.
calendarFrame = Frame(root, bg = dark_color)
todoFrame = Frame(root, bg = dark_color)
calendarFrame.grid(row = 0, column = 0)
todoFrame.grid(row = 0, column = 1)

#These are hardcoded listItem objects for demonstration purposes. THIS IS NOT THE FINAL PRODUCT. Currently unsure how clicking on the day will update the toDoList. 
arr = []
for i in range(1, 8):
    arr.append(listItem("Item "+str(i), i * 10, todoFrame, i, 0))

#This creates the calendar.
#Placeholders:  'March' - will have to be replaced with a string of the current month
#               '31' - will be replaced with integer of days in the current month
#               '1' - Will have to be replaced with the integer of the first weekday of the month. 0 = Sunday, 1 = Monday, 2 = Tuesday, etc.
#don't touch calenderFrame
calendarDemo = calendarGrid("March", 31, 1, calendarFrame)


#These are the add/remove assignment buttons. Edit the "command" parameters with the appropriate function. If the function has its own parameters, use this... command = lambda: functionName(param)
addAssignmentButton = tk.Button(root, text = "Add Assignment", width = 25, command = lambda: print("hello world!"))
addAssignmentButton.grid(row = 2, column = 0)

delAssignmentButton = tk.Button(root, text = "Remove Assignment", width = 25, command = lambda: print("goodbye world!"))
delAssignmentButton.grid(row = 2, column = 1)


#makes the actual thing work
root.mainloop()
