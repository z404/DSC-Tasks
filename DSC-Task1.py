import schedule
import time
from datetime import datetime, timedelta
import smtplib


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(mail, passwd)

def reminder(subname):
    message = 'You have '+subname+' in 5 minutes! Join the class now to avoid being late!'
    s.sendmail(mail, rec, message)

mail=input("Enter a sender's email ID: ")
passwd = input("Enter password of sender's email ID: ")
rec = input("Enter receiver's email ID")

with open('TimeTable.txt') as file:
    lines = file.readlines()
        
current_day = ''
print(lines)
for i in lines:
    line = i.rstrip('\n')
    if line.startswith('-'): current_day = line.lstrip('-')
    else:
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
        
while True:
    schedule.run_pending()
    time.sleep(1)
