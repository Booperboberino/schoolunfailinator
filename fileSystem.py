import json
from task import Task
import taskHandler
#I haven't tested some of this stuff in a while so no guarantee it all works
def editToDo(year,month,day,task,done = False): #either changes or adds a value to the to do list
    global fileName
    createDay(year,month,day)
    f = open(fileName)
    data = json.load(f)
    f.close()

        if data[str(year)][str(month)][str(day)] == {}:
            initDay(year,month,day)
        dayInfo = getDayInfo(year,month,day)

        if task in dayInfo["toDo"]: #code to change value and update completed and remaining, to be used with check box
            old = dayInfo["toDo"][task]
            dayInfo["toDo"][task] = done
            if done != old:
                if done == True:
                    dayInfo["completed"]+=1
                    dayInfo["remaining"]-=1
                else:
                    dayInfo["completed"]-=1
                    dayInfo["remaining"]+=1
        else: #adds new item to toDo and updates completed or remaining depending on if said new item is completed
            dayInfo["toDo"][task] = done
            if done == True:
                dayInfo["completed"]+=1
            else:
                dayInfo["remaining"]+=1
        data[str(year)][str(month)][str(day)] = dayInfo
        f = open(fileName,'w')
        json.dump(data,f,indent = 2)
        f.close()    
    

    def createDay(year,month,day): #creates blank day if not in .json and also creates year and month if necessary
        global fileName
        listyBoi = [str(year), str(month), str(day)]
        f = open(fileName)
        data = json.load(f)
        a = data
        for i in listyBoi:
            if i not in a:
                a[i]={}
            a = a[i]
        f.close()
        f = open(fileName,'w')
        json.dump(data,f,indent = 2)
        f.close()

    def getDayInfo(year,month,day): #returns dictionary for a day
        global fileName
        createDay(year,month,day)
        
        f = open(fileName)
        data = json.load(f)
        f.close() 
        return data[str(year)][str(month)][str(day)]

    def getToDo(year,month,day): #kinda redundant since get day info, but it exists cause yeah
        dayInfo = getDayInfo(year,month,day)
        if dayInfo == {}:
            return dayInfo
        return dayInfo["toDo"]

    def initDay(year,month,day): #initializes/resets a day
        global fileName
        createDay(year,month,day)
        f = open(fileName)
        data = json.load(f)
        initValues = {"completed":0,"remaining":0,"toDo":{}}
        data[str(year)][str(month)][str(day)] = initValues
        f.close()
        f = open(fileName,'w')
        json.dump(data,f,indent = 2)
        f.close()

    def removeDay(year,month,day): #removes a day and its month and/or year if made empty
        global fileName
        createDay(year,month,day)
        f = open(fileName)
        data = json.load(f)    
        del data[str(year)][str(month)][str(day)]
        if data[str(year)][str(month)] == {}:
            del data[str(year)][str(month)]
        if data[str(year)]== {}:
            del data[str(year)]
        f.close()
        f = open(fileName,'w')
        json.dump(data,f,indent = 2)
        f.close()

    def removeToDoItem(year,month,day,task): #removes an item from the to do list and updates the completed or remaining values
        global fileName
        createDay(year,month,day)
        f = open(fileName)
        data = json.load(f)
        f.close()
        dayInfo = getDayInfo(year,month,day)
        if dayInfo == {} or "toDo" not in dayInfo:
            return
        elif task not in dayInfo["toDo"]:
            return
        if dayInfo["toDo"][task] == False:
            dayInfo["remaining"] -= 1
        else:
            dayInfo["completed"] -=1
        del dayInfo["toDo"][task]
        data[str(year)][str(month)][str(day)] = dayInfo
        f = open(fileName,'w')
        json.dump(data,f,indent = 2)
        f.close()  
        
    def resetJSON(): #completey resest the .json file, pog for testing
        global fileName
        f = open(fileName,'w')
        json.dump({},f,indent = 2)
        f.close()

    def jsonToTask(task, year="2020",month="03",day="21"):
        dueDate = month + "/" + day + "/" + year
        return Task(name=task, due_date=dueDate)


fileName = "files.json"