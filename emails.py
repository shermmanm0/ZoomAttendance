import csv
import shelve
shelfFile = shelve.open('data')
class_meetings = shelfFile['class_meetings']
emailfile = open('studenttoemail.csv')
reader = csv.reader(emailfile)
data = list(reader)
name_to_email_dict = {}
for x in data:
  name_to_email_dict[x[0]]=x[1]
#print(name_to_email_dict)


for meeting in class_meetings:
  meeting["students"]=[]
  for participant in meeting["participants"]:
    if participant["name"] in name_to_email_dict:
      participant["user_email"]=name_to_email_dict[participant["name"]]
      meeting["students"].append(participant)
shelfFile["class_meetings"] = class_meetings
shelfFile.close()

