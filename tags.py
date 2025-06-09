import matplotlib.pyplot as plt
import seaborn as sns
import isodate
import pandas as pd
from data import trending_videos
sns.set(style="whitegrid")

# calculate the number of tags for each video
trending_videos['tag_count'] = trending_videos['tags'].apply(lambda x: len(x))

# scatter plot for number of tags vs view count
plt.figure(figsize=(10,6))
sns.scatterplot(x='tag_count', y='view_count', data=trending_videos, alpha=0.6, color='orange')
plt.title('Number of Tags vs View Count')
plt.xlabel('Number of Tags')
plt.ylabel('View Count')
plt.show()