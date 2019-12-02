import json
import os
import datetime

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        new_data = (data)
        new_node = Task(new_data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        val = self.head
        while val is not None:
            print(val.name, val.deadline, val.timetospend)
            val = val.next

    def find(self, node):
        tmp = self.head
        while tmp != None:
            if tmp.name == node:
                return tmp
            tmp = tmp.next
        return None

    def deleteNode(self, key):

        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

class Task:

    def __init__(self, name=None, deadline=None, timetospend=None):
        self.name = name
        self.deadline = deadline
        self.time = timetospend
        self.next = None

class TaskManager:

    def __init__(self):
        self.tasks = LinkedList()

    def loadJson(self):

        f = os.listdir()
        if "data.json" in f:
            with open("data.json") as file:
                tasks = json.load(file)
                for key in tasks:
                    self.tasks = json.load(f)["tasks"]

    def NewTask(self):

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

        self.tasks = newTask[name]

    def saveTasks(self):

        task = {}
        tmp = self.tasks.head
        while tmp != None:
            task[tmp.name, tmp.deadline, tmp.timetospend] = tmp.toJSON()
            tmp = tmp.next
            with open('data.json', 'w') as f:
                json.dump(task, f)

    def addTask(self, name, deadline, timetospend):
        data = name, deadline, timetospend
        self.tasks.add(data)

    def printTask(self):

        print("\nAll tasks:")
        self.tasks.display()

    def mofifyTask(self):

        self.tasks.display()
        oldtask = input("\nPlease insert the name of the task you want to modify:")
        if self.tasks.find(oldtask) != None:
            self.tasks.deleteNode(oldtask)
            TaskManager.addTask()

def main():

    mytask = TaskManager()

    while True:
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")
        print("4 : Exit the application")

        user_input = int(input())

        if user_input == 1:
            mytask.NewTask()
            # mytask.addTask()
            mytask.saveTasks()
        elif user_input == 2:
            mytask.printTask()
        elif user_input == 3:
            mytask.mofifyTask()
            mytask.saveTasks()
        elif user_input == 4:
            print("Thank you for using the ToDo list helper, which helps you organize tasks")
            exit()
        else:
            mytask.saveTasks()
            print("Please type as required, inserting the number 1, 2, 3 or 4")


main()
