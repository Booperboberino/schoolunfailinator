import loader
from task import Task

class TaskHandler:

    def __init__(self):
        self.tasks = []
        pass
    
    def findUniqueId(self):
        # (Get all ids)
        allIds = []
        cnt = 0
        while True:
            cnt += 1
            if cnt in allIds:
                pass
            else:
                return cnt

    # Does not return
    def addTask(self, name: str, date):
        id = self.findUniqueId()
        task = Task(name=name, due_date=date)
        self.tasks.append(task)
        loader.addTask(task)

        

    def addWorkTask(self, id: int, date):
        pass

    # Does not return
    def editTask(self, id:int, name: str, ):

        pass

    # Does not return
    def removeTask(self):

        pass
    
    # Get the number of tasks in one day
    # Returns int
    def numberOfTasksOnDay(self, day):
        cnt = 0
        for a in loader.getListOfTasks:   # Get list of tasks in one day
            cnt += 1
        return cnt
