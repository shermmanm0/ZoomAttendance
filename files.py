import shutil
import os
import ezsheets
import csv
import shelve
shelfFile = shelve.open('data')
class_meetings = shelfFile['class_meetings']
path = os.path.dirname(os.path.abspath(__file__))+"/meeting_csvs/"
os.chdir(path)
for x in class_meetings[0]['students']:
    print(x)
"""



files = os.listdir()
ss = ezsheets.Spreadsheet('1K-KFYMPQuSz5Tnns-YQJ8KD5jS57cMqvom5cg5qDxOk')




for file in files:
    file_data = open(path+file)
    file_reader = csv.reader(file_data)
    file_array = list(file_reader)
    ss.createSheet(file)
    sheet = ss[file]
    sheet.updateRows(file_array)

shelfFile["class_meetings"]=class_meetings
shelfFile.close()"""