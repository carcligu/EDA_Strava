import requests
from pandas.io.json import json_normalize
import json
import pandas as pd

# Get the tokens from file to connect to Strava
with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)
# Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']


# Loop through all activities
page = 1
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']


# Create the dataframe ready for the API call to store your activity data
columns_to_keep=[
        "id",
        "name",
        "distance",
        "moving_time",
        "elapsed_time",
        "total_elevation_gain",
        "type",
        "start_date_local",
        "location_country",
        "achievement_count",
        "kudos_count",
        "comment_count",
        "athlete_count",
        "photo_count",
        "average_speed",
        "max_speed",
        "average_cadence",
        "has_heartrate",
        "average_heartrate",
        "max_heartrate",
        "elev_high",
        "elev_low",
        "pr_count",
        "total_photo_count",
        "suffer_score"
]

while True:
    # get page of activities from Strava
    r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
    r = r.json()

    # if no results then exit loop
    if (not r):
        break


    if page==1:
        activities = pd.json_normalize(r)
    else:
        activities = pd.concat([activities, pd.json_normalize(r)])

    # increment page
    page += 1

activities[columns_to_keep].to_csv('strava_activities_selected_fields.csv')