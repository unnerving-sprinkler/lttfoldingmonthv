#Import Info
import json
import requests
import pandas as pd
import time
from datetime import datetime

user_directory = {}

#Bring in spreadsheet with usernames
usernames = open("usernames.txt").read().splitlines()

#For each user pull the current information from the FAH servers
for each in usernames:
    time.sleep(.8)
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

            userid = userid
            ltt_score = ltt_score

            user_directory[userid] = {'id:': userid, 'username' : each, 'ltt_start_score': ltt_score}

            print(user_directory)


with open('userdict.json', 'w') as outfile:
        json.dump(user_directory, outfile)