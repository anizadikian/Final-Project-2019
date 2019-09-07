class Task:

    def __init__(self, name="", deadline="", timetospend=""):
        self.name = name
        self.deadline = deadline
        self.timetospend = timetospend

    def printTask(self):
        print("New Task", "\nTask: ", self.name, "\nDeadline: ", self.deadline, "\nTime: ", self.timetospend)

    def modifytask(self):
        print("Modified Task", "\nNew Task: ", self.name, "\nNew Deadline: ", self.deadline, "\nNew Time: ",
               self.timetospend)

    def seealltasks(self):
        pass

def main():

    task1 = Task("Programming", "20/07/2019", "4")
    task1.printTask()

    task2 = Task("Algebra", "21/09/2019", "5")
    task2.modifytask()

main()


