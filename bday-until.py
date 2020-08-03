import os
from tasklib import TaskWarrior
import datetime
from datetime import date
from datetime import timedelta 

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

# This is so you can use YYYY-MM-DD in TaskWarrior
year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day	

today = date(year, month, day)
# Here you can choose when you want to delete tasks. If due was -1 or -2, 4, 20 days whatever you want)
yesterday = today - timedelta(days = 1) 
with open(todo, 'w'): pass

# Fill in your path to your Taskwarrior database

tw = TaskWarrior('/PATH/TO/.task')

# This filters tasks which are pending and due before yesterday and in the project: priv.bday which is the subproject 'bday' of the main project 'priv' for me. 
tasks = tw.tasks.pending().filter(due__before=yesterday, project='priv.bday')

# WARNING this deletes the tasks If you want to check whether the script works I suggest you comment out the following and replace it with what's below
for task in tasks:
    task.delete()

# If you want to check before allowing tasks to be deleted use the below and check your CHECK.txt file after running the script.
# CHECK = = "/PATH/TO/CHECK.txt"
# for task in tasks:
#   begin = "[ ] "
#   end = "\n"
#   f = open(CHECK, "a+")
#   f.write(begin + str(task) + end)
#   f.close()


