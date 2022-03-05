import copy
from dataclasses import dataclass
from glob import glob
from math import gcd

from matplotlib import pyplot as plt
import numpy as np

from RM_Exemple import estimatePriority

tasks = {}
hyperperiod = 0
dataTask = {}
task_bis = {}
y_axis  = []
from_x = []
to_x = []
nbTasks = 0

"""
This function is used by the user to enter the data of the task they 
wish to schedule. The data should be presented as: 
    * Number of tasks
    and then for each task:
        * WCET of task
        * Period of task
        * Deadline of task (usualy same as period)
"""
def EnterData():
    nbTasks = int(input("\nEnter the number of tasks you wish to schedule: "))

    dataTask = {}
    # Storing data for every task in a dictionary
    # array of start time and finish time for each task
    for i in range(nbTasks):
        dataTask["task%d"%i] = {"start":[], "finish":[]}
    
    dataTask["sleeping"] = {"start":[],"finish":[]}

    for i in range(nbTasks):
        tasks[i] = {}
        print("\nEnter WCET of task T", i, ":")
        tasks[i]["WCET"] = int(input())
        print("\nEnter the period of task T", i, ":")
        tasks[i]["Period"] = int(input())
        print("\nEnter the deadline of task D", i, ":")
        tasks[i]["Deadline"] = int(input())

"""
Function to calculate the hyperperiod needed to schedule the tasks
"""
def Hyperperiod():
    tmp = []
    for i in range(nbTasks):
        tmp.append(tasks[i]["Period"])
    hyperperiod = tmp[0]
    for i in tmp[1:]:
        hyperperiod = hyperperiod*i // gcd(hyperperiod, i)
    print("\n Hyperperiod: ", hyperperiod)
    return hyperperiod


def Priorities(task_bis):
    tempPeriod = hyperperiod
    P = -1    #Returns -1 for idle tasks
    for i in tasks.keys():
        if (task_bis[i]["WCET"] != 0):
            if (tempPeriod > task_bis[i]["Period"] or tempPeriod > tasks[i]["Period"]):
                tempPeriod = tasks[i]["Period"] #Checks the priority of each task based on period
                P = i
    return P

"""
Takes the hyperperiod in params 
"""
def Scheduling(hyperperiod):
    task_bis = copy.deepcopy(tasks)
    for i in range(hyperperiod):
        priority = Priorities(task_bis)

        if (priority != -1):
            task_bis[priority]["WCET"] -= 1
            dataTask["task%d"%priority]["start"].append(i)
            dataTask["task%d"%priority]["finish"].append(i+1)
            y_axis.append("task%d"%priority)
            from_x.append(i)
            to_x.append(i+1)
        
        else:
            dataTask["sleeping"]["start"].append(i)
            dataTask["sleeping"]["finish"].append(i+1)
			# For plotting the results
            y_axis.append("Sleeping")
            from_x.append(i)
            to_x.append(i+1)

        for j in task_bis.keys():
            task_bis[j]["Period"] -= 1
            if(task_bis[j]["Period"] == 0):
                task_bis[j] = copy.deepcopy(tasks[j])
                
def Show():
    plt.title('Rate Monotonic scheduling')
    plt.xlabel("Real-Time clock")
    plt.ylabel("Tasks")
    plt.hlines(y_axis, from_x, to_x, linewidth=20, color = 'red')
    plt.grid(True)
    plt.xticks(np.arange(min(from_x), max(to_x)+1, 1.0))
    plt.show()

if __name__ == '__main__':
	EnterData()
	hyperperiod = Hyperperiod()
	Scheduling(hyperperiod)
	Show()
