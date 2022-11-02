#Import Info
import json
import requests
import pandas as pd
import time


#Bring in spreadsheet with usernames
usernames = open("usernames.txt").read().splitlines()

#Create empty lists to populate later
usr = []
scr = []

#For each user pull the current information from the FAH servers
for each in usernames:
    time.sleep(.8) #TODO: OPTO THIS
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

            #append that users info to the list (only if they have LTT folding xp
            usr.append(each)
            scr.append(ltt_score)

#Take information and export it to a csv file using Pandas
#Raw Data
usr = usr
scr = scr

#Disc for table head
dict = {'USERNAME':usr, 'SCORE':scr}

df = pd.DataFrame(dict)
df.to_csv('./export/current_user_scores.csv')
