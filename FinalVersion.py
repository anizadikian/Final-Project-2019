import json
import datetime


class Task:

    def __init__(self, name, deadline, timetospend):
        self.name = name
        self.deadline = deadline
        self.timetospend = timetospend

    def NewTask(self):

        with open('data.json') as f:
            dicts_old = json.load(f)
        dicts = {}
        while True:
            self.name = input("What is the task you need to accomplish?   ")
            if self.name.isalpha():
                dicts[self.name] = {}
                break
            print("Please enter characters A-Z only")

        while True:
            self.deadline = input(
                "What is the deadline for the task mentioned? Please insert in the format MM/DD/YYYY:   ")
            try:
                user_deadline_converted = datetime.datetime.strptime(self.deadline, '%m/%d/%Y')
                dicts[self.name]['Deadline'] = self.deadline
                break
            except ValueError:

                print("Date format should be MM/DD/YYYY")
        while True:
            self.timetospend = input("What is the period of time you need to accomplish it?    ")
            dicts[self.name]['Time'] = self.timetospend
            if self.timetospend.isdigit():
                break
            print("You must enter a number (i.e. 0,1,2...")

        dicts_old['tasks'].append(dicts)
        dicts_new = dicts_old
        with open('data.json', 'w') as f:
            json.dump(dicts_new, f)

    def modifytask(self):

        with open('data.json') as f:
            dicts_old = json.load(f)

        for i in dicts_old['tasks']:
            self.name = next(iter(i.keys()))
            self.deadline = i[self.name]['Deadline']
            self.times = i[self.name]['Time']
            print('Task is ', self.name, ', Deadline is ', self.deadline,
                  ', The period of time you need to accomplish is', self.times)

        self.question = input("Please insert the name of the task you want to modify:      ")

        print("The task is   ", self.question)

        while True:
            self.answer = input("Please insert the new name of the task?")
            if self.answer.isalpha():
                break
            print("Please enter characters A-Z only")

        self.deadline = input("please input the new deadlinein the format MM/DD/YYYY:    ")
        self.times = input("Please input the new time you need to accomplish the task:     ")

        for i in range(len(dicts_old['tasks'])):
            if next(iter(dicts_old['tasks'][i].keys())) == self.question:
                dicts_old['tasks'][i] = {
                    self.answer: {'Deadline': self.deadline, 'Time': self.timetospend}}

        with open('data.json', 'w') as f:
            json.dump(dicts_old, f)

    @classmethod
    def getAllTasks(cls):

        with open('data.json') as f:
            dicts_old = json.load(f)
        sorted_data = {}
        for i in dicts_old['tasks']:
            name = next(iter(i.keys()))
            deadline = i[name]['Deadline']
            times = i[name]['Time']
            sorted_data[deadline] = name + " " + times

        ordered_data = sorted(sorted_data.items(), key=lambda x: datetime.datetime.strptime(x[0], '%m/%d/%Y'),
                              reverse=False)
        print(ordered_data)
        for i in ordered_data:
            print(i[0], " -------", i[1])


def main():

    mytask = Task("Programming", "12/12/1222", "4")

    while True:
        print("Please choose number from the following:")
        print("1 : Insert new task")
        print("2 : See previously added tasks")
        print("3 : Modify task")
        print("4 : Exit the application")

        user_input = int(input())

        if user_input == 1:

            mytask.NewTask()



        elif user_input == 2:

            Task.getAllTasks()


        elif user_input == 3:

            mytask.modifytask()

        elif user_input == 4:
            print("Thank you for using the ToDo list helper, which helps you organize tasks")
            exit()
 
        else:
            print("Please type as required, inserting the number 1, 2, 3 or 4")


main()
