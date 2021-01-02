'''
PROGRAM TO SCHEDULE EMAILS 5 MINUTES BEFORE A CLASS
'''
#importing required modules
import schedule
import time
from datetime import datetime, timedelta
import smtplib

#Getting required information
mail = input("Enter a sender's email ID: ")
passwd = input("Enter password of sender's email ID: ")
rec = input("Enter receiver's email ID")

#readying smtp module to send emails
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(mail, passwd)

#reminder funtion that is called by the scheduler when the time comes
def reminder(subname):
    message = 'You have '+subname+' in 5 minutes! Join the class now to avoid being late!'
    s.sendmail(mail, rec, message)

#reading the time table file to get class timings and class name
with open('TimeTable.txt') as file:
    lines = file.readlines()

#schedule each task on the correct day and time  
current_day = ''
print(lines)
for i in lines:
    line = i.rstrip('\n')
    if line.startswith('-'):
        #chaning the current day to the appropriate day
        current_day = line.lstrip('-')
    else:
        #schedule the task appropriatly
        timegiven = datetime.strftime(datetime.strptime(line.split()[0],'%H:%M')-timedelta(minutes=5),'%H:%M')
        subjectname = line.split()[1]
        print('Sceduled',subjectname,'at',timegiven,'on',current_day)
        if current_day == 'Monday': schedule.every().monday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Tuesday': schedule.every().tuesday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Wednesday': schedule.every().wednesday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Thursday': schedule.every().thursday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Friday': schedule.every().friday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Saturday': schedule.every().saturday.at(timegiven).do(reminder,subname=subjectname)
        if current_day == 'Sunday': schedule.every().sunday.at(timegiven).do(reminder,subname=subjectname)

#keep main loop busy while the scheduler waits for the right time
while True:
    schedule.run_pending()
    time.sleep(1)
