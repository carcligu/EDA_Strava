# EDA_Strava
In this project I want to explore my own data in Strava. Strava is one of the most known social networks for athletes and I use it to track my progress and shape when running or cycling, at the same time I can see activities of my friends. Is a kind of Facebook for athletes. 

# Data Source
For pulling data with the STRAVA API I used this post as a baseline: https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86 .However, I did some modifications on how to convert the data into a df. 

Data is gathered with the files: 
* retrieve_access_tokens.py: generates strava_tokens.json
* strava_tokens.json: contains security data (I did not include personal data, however you can have the structure of this json file)
* get_data.py: takes the strava_tokens.json and access strava to pull data and save it as a .csv file

# Metadata
