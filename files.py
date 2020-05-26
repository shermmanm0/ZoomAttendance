import shutil
import os
import ezsheets
import csv
import shelve
shelfFile = shelve.open('data')
class_meetings = shelfFile['allmeetings']
path = os.path.dirname(os.path.abspath(__file__))+"/meeting_csvs/"
os.chdir(path)
headers = []
for x in class_meetings[0]["participants"]:
    headers.append(x)

output_file = open("attendance_data2.csv","w",newline="")
writer = csv.writer(output_file)
writer.writerow(["course","date","host"]+headers)
for cm in class_meetings:
    for student in cm["participants"]:
        row = [cm["topic"],cm["date"],cm["user_email"]]
        for x in student:
            row.append(student[x])
        writer.writerow(row)
output_file.close()