#Import Info
import json
import requests
import pandas as pd
import time
from datetime import datetime


#Bring in spreadsheet with usernames
usernames = open("usernames.txt").read().splitlines()
userdictionary = open('userdict.json')
userdictionary = json.load(userdictionary)


#Create empty lists to populate later
usr = []
scr = []
tot_scr = []

#For each user pull the current information from the FAH servers
for each in usernames:
    time.sleep(1.2) #TODO: OPTO THIS
    url = 'https://api.foldingathome.org/user/' + str(each)
    print(url)
    #Clean up the responce
    user_info = requests.get(url).json()

    #This is this persons USERID
    userid = str((user_info['id']))
    print(userid)

    #BLOCK FOR TROUBSHOOTING
    # print(user_info['teams'])
    # for team in user_info['teams']:
    #     print(team['team'])

    for team in user_info['teams']:
        if team['team'] == 223518:
            ltt_score = team['score']
            print(each + " current score is: " + str(ltt_score))
            StartScore = userdictionary[userid]['ltt_start_score']
            print(each + " orgin score was " + str(StartScore))

            earned_score = ltt_score - StartScore

            #append that users info to the list (only if they have LTT folding xp
            usr.append(each)
            scr.append(earned_score)
            tot_scr.append (ltt_score)

#Take information and export it to a csv file using Pandas
#Raw Data
usr = usr
scr = scr
tot_scr = tot_scr

#Disc for table head
dict = {'USERNAME':usr, 'SCORE':scr, 'TOTAL SCORE':tot_scr}

#MAKE THE DATAFRAME
df = pd.DataFrame(dict)

#NAME AND SAVE DATAFRAME
now = datetime.utcnow()
datestring = now.strftime("%m_%d %H_%M_%S")
csvname = ("./export/FAHSTATS " + datestring + ".csv")
df.to_csv(csvname)
