import tweepy
import requests
import datetime
import json



today = datetime.date.today()

formatted = today.strftime('%Y%m%d')

newFormat = int(formatted)

print(newFormat)


auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

url = "https://mlb-data.p.rapidapi.com/json/named.mlb_broadcast_info.bam"


querystring = {
    "src_comment":"'National'",
    "src_type":"'TV'",
    "tcid":"mm_mlb_schedule",
    "start_date": newFormat,
    "season":"'2021'",
    "end_date": newFormat,
    "sort_by":"'game_time_et_asc'",
    "away_team_id": "108"
    } 


# print(params)

headers = {
    'x-rapidapi-key': "7524861152msh237a3378b10e9bfp1a411ejsn270bb159b78f",
    'x-rapidapi-host': "mlb-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)


games = json.loads(response.text)

print(games)

# print(games)

# for game in games:
#         try: 
#             print(game)
#         except KeyError:
#             print("Error")


api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)



try: 
    api.verify_credentials()
    print("Authentication ok")
except:
    print("error")

# # api.update_status("Test")


