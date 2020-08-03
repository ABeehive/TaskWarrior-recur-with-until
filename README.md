# The Problem
TaskWarrior doesn't support the combination of recurring tasks with an until date. 
A recurring task, in my case a reminder to congratulate someone on their birthday yearly would look something like this : 

> task add Wish FIRSTNAME LASTNAME a happy birthday due:BIRTHDAYDATE scheduled:due-2d wait:due-7d until:due+1d project:priv.bday +buy

I've added the wait and scheduled if I want to send them a card, hence also the the tag +buy

Problem is, that when you enter their birthday and let's say it's 1985-01-01 then the task will never show up, because it's well past that day. 

# The solution
To solve this problem I've created a small pythonscript using the [TaskLib](https://github.com/robgolding/tasklib) library to check for tasks which have a due date before yesterday in the project:priv.bday. 
The script then deletes the tasks that match this. 

Add a simple cronjob for a check every 30minutes. This is overkill, but at least then it's out of the way.. for example : 
> *30 * * * * python3 /PATH/TO/bday-until.py

# Dependencies
- [Taskwarrior](www.taskwarrior.org)
- Python libraries : 
  - [TaskLib](https://github.com/robgolding/tasklib)
  - datetime
  
  Which can be installed using pip3 if you have it: 
  
  >pip3 install tasklib
  >pip3 install datetime

# !! Warning !!
Make sure to restrict the filter to a specific project or tag, otherwise all your old tasks are deleted. 
You can check whether it works by first writing to a file. To do that uncomment the section shown.

