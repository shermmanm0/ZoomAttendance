import shelve
import csv
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


shelfFile = shelve.open('data')
meetings = shelfFile['class_meetings']
student_email_dict = shelfFile["student_email_dict"]
all_meeting_data = shelfFile["all_meeting_data"]
all_meeting_data_duration_sum = unique(list(map(lambda x:{"course":x["course"],"date":x["date"],"user_email":x["user_email"]},all_meeting_data)))


for x in all_meeting_data_duration_sum:
    filtered = filter(lambda y:{y["course"],y["date"],y["user_email"]}=={x["course"],x["date"],x["user_email"]},all_meeting_data)        
    duration_sum = 0
    for z in filtered:
        duration_sum+=z["duration"]
    x["duration"] = duration_sum
    
file = open("meeting_data.csv","w",newline="")
writer = csv.DictWriter(file,["course","date","user_email","duration"])
writer.writeheader()
writer.writerows(all_meeting_data_duration_sum)
shelfFile["all_meeting_data"]=all_meeting_data            


shelfFile.close()
