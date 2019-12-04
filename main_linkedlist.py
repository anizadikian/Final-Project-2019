import json
import os
import datetime

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        name, deadline, time = data
        new_node = Task(name, deadline, time)
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

    def replace(self, oldtask, newtask, newdeadline, newtime):
        node = self.head
        while node is not None:
            if node.name == oldtask:
                node.name = newtask
                node.deadline = newdeadline
                node.timetospend = newtime
                break
            node = node.next
        else:
            raise ValueError('Item not found: {}'.format(oldtask))

class Task:

    def __init__(self, name=None, deadline=None, timetospend=None):
        self.name = name
        self.deadline = deadline
        self.timetospend = timetospend
        self.next = None

    def toJSON(self):
        tmp = {}
        tmp["name"] = self.name
        tmp["deadline"] = self.deadline
        tmp["timetospend"] = self.timetospend
        return tmp

class TaskManager:

    def __init__(self):
        self.tasks = LinkedList()

    def loadJson(self):
        self.tasks = LinkedList()
        f = os.listdir()
        if "data.json" in f:
            with open("data.json") as file:
                tasks = json.load(file)['tasks']
                for key, value in tasks.items():
                    self.tasks.add((key, value['Deadline'], value['Time']))

    def createTask(self):

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
        print(newTask)
        return name, deadline, timetospend

    def saveTasks(self):

        task = {'tasks' : {}}
        tmp = self.tasks.head
        while tmp != None:
            taskdict = {"Deadline": tmp.deadline, "Time": tmp.timetospend}
            task['tasks'][tmp.name] = taskdict
            tmp = tmp.next
        with open('data.json', 'w') as f:
            json.dump(task, f)

    def addTask(self, newdata):
        self.tasks.add(newdata)

    def printTask(self):

        print("\nAll tasks:")
        self.tasks.display()

    def modifyTask(self):

        newTask = {}

        oldtask = input("\nPlease insert the name of the task you want to modify:     ")
        newtask = input("\nPlease insert the name of the new task:    ")
        newdeadline = input("\nPlease insert the deadline of the new task:    ")
        newtime = input("\nPlease insert the new time of the new task:    ")

        newTask[newtask] = {}
        newTask[newtask]['Deadline'] = newdeadline
        newTask[newtask]['Time'] = newtime

        if self.tasks.find(oldtask) != None:
            self.tasks.replace(oldtask, newtask, newdeadline, newtime)

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
            mytask.loadJson()
            newTask = mytask.createTask()
            mytask.addTask(newTask)
            mytask.saveTasks()
        elif user_input == 2:
            mytask.loadJson()
            mytask.printTask()
        elif user_input == 3:
            mytask.loadJson()
            mytask.printTask()
            mytask.modifyTask()
            mytask.saveTasks()
        elif user_input == 4:
            print("Thank you for using the ToDo list helper, which helps you organize tasks")
            exit()
        else:
            mytask.saveTasks()
            print("Please type as required, inserting the number 1, 2, 3 or 4")

main()
