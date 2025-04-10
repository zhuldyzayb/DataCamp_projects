# Perform exploratory data analysis on the netflix_data.csv data
# to understand more about movies from the 1990s decade.

# 1. What was the most frequent movie duration in the 1990s? Save an approximate
#    answer as an integer called duration.

# 2. A movie is considered short if it is less than 90 minutes.
#    Count the number of short action movies released in the 1990s and save
#    this integer as short_movie_count.

# Feel free to experiment after submitting the project!

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('netflix_data.csv')

# 1.
# print(df.describe())
movies_90s = df[(df['release_year']>=1990) & (df['release_year']<2000)]
#print(movies_90s.describe())
#plt.hist(movies_90s['duration'], bins = 10)
#plt.show()
duration = movies_90s['duration'].mode().iloc[0]

# 2.
short_action_movies = movies_90s[(movies_90s['genre']=="Action") & (movies_90s['duration']<=90)]
short_movie_count = short_action_movies.shape[0]
