import json
import datetime


class Task:

    def __init__(self, name="", deadline="", timetospend=""):
        self.name = name
        self.deadline = deadline
        self.timetospend = timetospend

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def loadTasksFromJSON(self):
        with open('data.json') as f:
            self.tasks = json.load(f)["tasks"]

    def saveTasks(self):
        saveObj = {}
        saveObj["tasks"] = self.tasks
        with open('data.json', 'w') as f:
            json.dump(saveObj, f)

    def addTask(self):

        newTask = {}
        while True:
            name = input("What is the task you need to accomplish?   ")
            if name.isalpha():
                newTask[name] = {}
                break
            print("Please enter characters A-Z only")

        while True:
            deadline = input(
                "What is the deadline for the task mentioned? Please insert in the format MM/DD/YYYY:   ")
            try:
                user_deadline_converted = datetime.datetime.strptime(deadline, '%m/%d/%Y')
                newTask[name]['Deadline'] = deadline
                break
            except ValueError:

                print("Date format should be MM/DD/YYYY")
        while True:
            timetospend = input("What is the period of time you need to accomplish it?    ")
            newTask[name]['Time'] = timetospend
            if timetospend.isdigit():
                break
            print("You must enter a number (i.e. 0,1,2...")

        self.tasks[name] = newTask[name]

    def modifyTask(self):

        dicts_old = self.tasks
        for i in dicts_old:
            name = i
            deadline = dicts_old[i]['Deadline']
            timetospend = dicts_old[i]['Time']
            print('Task is ', name, ', Deadline is ', deadline,
                  ', The period of time you need to accomplish is', timetospend)

        question = input("Please insert the name of the task you want to modify:      ")

        if question in dicts_old.keys():
            print("The task is   ", question)

            while True:
                answer = input("Please insert the new name of the task?")
                if answer.isalpha():
                    break
                print("Please enter characters A-Z only")

            deadline = input("please input the new deadline in the format MM/DD/YYYY:    ")
            timetospend = input("Please input the new time you need to accomplish the task:     ")
            del dicts_old[question]
            dicts_old[answer] = {'Deadline': deadline, 'Time': timetospend}
        else:
            print("Task doesnt exist")
            return


    def getAllTasks(self):

        with open('data.json') as f:
            dicts_old = json.load(f)["tasks"]
        sorted_data = {}
        for i in dicts_old:
            name = i
            deadline = dicts_old[i]['Deadline']
            times = dicts_old[i]['Time']
            sorted_data[deadline] = name + " " + times

        ordered_data = sorted(sorted_data.items(), key=lambda x: datetime.datetime.strptime(x[0], '%m/%d/%Y'),
                              reverse=False)
        print(ordered_data)
        for i in ordered_data:
            print(i[0], " -------", i[1])

def main():

    taskManager = TaskManager()
    taskManager.loadTasksFromJSON()

    while True:
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")
        print("4 : Exit the application")

        user_input = int(input())

        if user_input == 1:
            taskManager.addTask()
            taskManager.saveTasks()
        elif user_input == 2:
            taskManager.getAllTasks()
        elif user_input == 3:
            taskManager.modifyTask()
            taskManager.saveTasks()
        elif user_input == 4:
            print("Thank you for using the ToDo list helper, which helps you organize tasks")
            exit()
        else:
            taskManager.saveTasks()
            print("Please type as required, inserting the number 1, 2, 3 or 4")


main()
