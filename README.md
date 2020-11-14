# EDA_Strava
In this project I want to explore my own data in Strava. Strava is one of the most known social networks for athletes and I use it to track my progress and shape when running or cycling, at the same time I can see activities of my friends. Is a kind of Facebook for athletes. 

# RESULTS
## Activity over time
I can clearly see how my level of activity reached a peak on May 2019, when I run the copenhaguen marathon, followed by rest period on summer. 
After that I started trail running an mtb, as I was living in my local town back in Alicante, plenty of mountains to run and bike (Sep 2019 - Dec 2019)
In the last period, you can clearly see how starting a job reduced highly my level of activity, followed by 2 months of lockdown in Spain when it was not allowed to do sport outdoors

![alt text](https://github.com/carcligu/EDA_Strava/blob/main/Figures/activities_over_time_by_activity.png =150x)
<img src="https://github.com/carcligu/EDA_Strava/blob/main/Figures/activities_over_time_by_activity.png" width="48">

# Data Source
For pulling data with the STRAVA API I used this post as a baseline: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86 .However, I did some modifications on how to convert the data into a df. 

Data is gathered with the files: 
* retrieve_access_tokens.py: generates strava_tokens.json
* strava_tokens.json: contains security data (I did not include personal data, however you can have the structure of this json file)
* get_data.py: takes the strava_tokens.json and access strava to pull data and save it as a .csv file

