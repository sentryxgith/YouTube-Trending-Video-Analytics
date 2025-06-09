import pandas as pd

trending_videos = pd.read_csv('trending_videos.csv')
print(trending_videos.head())

# check for missing values
missing_values =  trending_videos.isnull().sum()

# display data types
data_types = trending_videos.dtypes 

missing_values, data_types

# fill missing description with "No description"
trending_videos['description'] = trending_videos['description'].fillna("No description")

# convert 'published_at' to datetime
trending_videos['published_at'] = pd.to_datetime(trending_videos['published_at'])

# convert tags from string representation of list to actual list
trending_videos['tags'] = trending_videos['tags'].apply(lambda x: eval(x) if isinstance(x, str) else x)

# descriptive statistics
descriptive_stats = trending_videos[['view_count', 'like_count', 'dislike_count', 'comment_count']].describe()

descriptive_stats