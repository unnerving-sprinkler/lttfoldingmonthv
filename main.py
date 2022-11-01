#Import Info
import json
import requests

#Bring in spreadsheet with usernames
usernames = open("usernames.txt").read().splitlines()

#For each user pull the current information from the FAH servers
for each in usernames:
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


