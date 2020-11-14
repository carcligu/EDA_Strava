# EDA_Strava
In this project I want to explore my own data in Strava. Strava is one of the most known social networks for athletes and I use it to track my progress and shape when running or cycling, at the same time I can see activities of my friends. Is the Facebook for athletes. 

# RESULTS
## Activity over time
There are different events I can identify on the graph: 
* My level of activity reached a peak on May 2019, when I run the Copenhaguen marathon, followed by a rest period on summer. 
* After that I started trail running an mtb, as I was living in my local town back in Alicante, plenty of mountains to run and bike (Sep 2019 - Dec 2019)
* In the last period, you can clearly see how starting a job reduced highly my level of activity, followed by 2 months of lockdown in Spain when it was not allowed to do sport outdoors

<img src="https://github.com/carcligu/EDA_Strava/blob/main/Figures/activities_over_time_by_activity.png" width="550">

## Hardest type of activity
Run and Trail Run are the hardest type of activity, accoring to the average heartrate and max heartrate provided by strava

<img src="https://github.com/carcligu/EDA_Strava/blob/main/Figures/boxplot_median_max_heartrate.png" width="550">


# Data Source
For pulling data with the STRAVA API I used this post as a baseline: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86 .However, I did some modifications on how to convert the data into a df. 

Data is gathered with the files: 
* retrieve_access_tokens.py: generates strava_tokens.json
* strava_tokens.json: contains security data (I did not include personal data, however you can have the structure of this json file)
* get_data.py: takes the strava_tokens.json and access strava to pull data and save it as a .csv file

# NEXT STEPS
Ideas that come to my mind for next steps: 

## Regression model to predict running times

### Hypothesis
The time of a race can be predicted given some inputs. 

### Inputs 
  * Distance
  * Elevation
  * Different metrics about the shape of the athlete
  
### Limitations/Risks
Strava only provide average and max heartrate per activity. The shape of the athlete can be tricky to calculate with the metrics we currently have. May be worth to connect with other APIs (Garmin?) to extract more data such as: weicht, steps per day, heart rate resting...

## Analysis on Social Media:
One of the features Strava has is the possibility to give kudos. Would be possible to do an analysis on what motivate athletes to give kudos.

### Hypothesis
Great achievements, long distances, fast runs (compared with your usual activities, not with other athletes), uploading images, modifying the title of an activity to make it funny...etc, all these things can increase the kudos you receive. 

### Inputs
Mainly commented in the hypothesis

### Limitations
Difficult to compare over time, probably I would need to exclude some activities, as at the beginning for each athlete, usually the number of followers is very limited. In that case, although you fulfill any of the previous hypoteshis, it will not have an impact on the kudos. 

