import shelve
import csv
import os

shelfFile = shelve.open('data')
ids = shelfFile['ids']
class_meetings = shelfFile['class_meetings']
headers = []
for x in class_meetings[0]['students'][0]:
    headers.append(x)
print(headers)
#class_meeting = class_meetings[0]
path = os.path.dirname(os.path.abspath(__file__))+"/meeting_csvs/"
#filename = path+"/"+class_meeting['file_name']+".csv"


for class_meeting in class_meetings:
    output_file = open(path+class_meeting['file_name']+'.csv','w',newline='')
    writer = csv.DictWriter(output_file,headers)
    writer.writeheader()
    for x in class_meeting['students']:
        writer.writerow(x)
    output_file.close()


shelfFile['class_meetings']=class_meetings
shelfFile.close()
