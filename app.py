import http.client
import mimetypes
import json
import csv
import ezsheets
import shelve
from datetime import datetime
from dateutil import tz
import base64
import urllib.parse
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')
def get_student_email_dict():
  emailfile = open('studenttoemail.csv')
  reader = csv.reader(emailfile)
  data = list(reader)
  name_to_email_dict = []
  for x in data:
    name_to_email_dict.append({x[0]:x[1]})
  return name_to_email_dict

def zoom_request(url_start,return_key,id="",url_end=""):
  headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IkdseERhTERGUnMyMy1BZ3VjdTFWbHciLCJleHAiOjE1OTIwMjA4MDAsImlhdCI6MTU4OTM1MzYzOX0.32bYFaKf9ya2JrjXtw1PzNq743YWEb0Td8uorVNUhMM',
  'Cookie': 'cred=C0C3C2AA81636EA325387F12F9BF2679'
  }
  if id.startswith("/"):
        id = urllib.parse.quote(urllib.parse.quote(id,safe=''))
  url = url_start+str(id)+url_end
  conn = http.client.HTTPSConnection("api.zoom.us")
  payload = ''
  conn.request("GET", url, payload, headers)
  res = conn.getresponse()
  data = res.read()
  jsonData = json.loads(data.decode("utf-8"))
  return jsonData[return_key]
def get_teachers():
  return zoom_request("/v2/groups/0zXX8QXnQRSBpCgzIo9hmQ/members","members")
def get_teachers_meetings(id):
  return zoom_request("/v2/report/users/","meetings",id,"/meetings?from=2020-04-01&to=2020-05-17&page_size=300")
def get_meeting_participants(id):
  return zoom_request("/v2/report/meetings/","participants",id,"/participants?page_size=300")
def unique(list1):
  unique_list = []
  for x in list1:
    if x not in unique_list:
      unique_list.append(x)
  return unique_list
def convertTime(input):
  utc_time = input.replace('T'," ").replace("Z","")
  from_zone = tz.gettz('UTC')
  to_zone = tz.gettz('America/New_York')
  utc = datetime.strptime(utc_time,'%Y-%m-%d %H:%M:%S')
  utc = utc.replace(tzinfo=from_zone)
  local_time = utc.astimezone(to_zone)
  return local_time.strftime("%m/%d/%Y")
course_names = {"English 1 CRR":"English",
"Counseling Lesson":"Counseling",
"My Meeting":"World History",
"Biology March 31":"Biology",
"Success":"Student Success",
"CWSP Class Session":"CWSP",
"Spanish 3 class":"Spanish 3",
"HPE":"Health and PE",
"Religion Class":"Religion",
"Geometry":"Geometry",
"Algebra":"Algebra 1"}
student_to_email = get_student_email_dict()



teachers = get_teachers()
meetings = []
sheet_titles = []
text_file = open("students.txt","w")
for teacher in teachers:
  meetings=meetings+get_teachers_meetings(teacher['id'])
class_meetings = []
for meeting in meetings:
  if meeting["id"] in [705711667,725466437,989085360,466594717,741411187,912495440,281881346,92113197187,98615995297,385903335,911346592,385903335,687867634]:
    meeting["date"]=(convertTime(meeting["start_time"]))
    meeting["participants"] = get_meeting_participants(meeting["uuid"])
    class_meetings.append(meeting)
students = []
for x in class_meetings:
  for y in x['participants']:
    students.append(y)


shelfFile = shelve.open("data")
shelfFile['class_meetings'] = class_meetings
shelfFile['students']=unique(students)
shelfFile.close()