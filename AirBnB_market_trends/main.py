import pandas as pd
import numpy as np


airbnb_price = pd.read_csv('airbnb_price.csv')
airbnb_review = pd.read_csv('airbnb_last_review.tsv', sep='\t')
airbnb_type = pd.read_excel("airbnb_room_type.xlsx")

#print(airbnb_price.head())
#print(airbnb_type.head())
#print(airbnb_review.head())

# 1. What are the dates of the earliest and most recent reviews?
#    Store these values as two separate variables with your preferred names.
airbnb_review['date'] = pd.to_datetime(airbnb_review['last_review'], format='%B %d %Y')
first_reviewed = airbnb_review['date'].min()
last_reviewed = airbnb_review['date'].max()


# 2. How many of the listings are private rooms? Save this into any variable.
nb_private_rooms = sum(airbnb_type['room_type'].str.lower()=='private room')

# 3. What is the average listing price? Round to the nearest two decimal places
#    and save into a variable.
airbnb_price['num_price'] = airbnb_price['price'].str.split().str[0].astype(float)
avg_price = airbnb_price['num_price'].mean().round(decimals=2)


# 4. Combine the new variables into one DataFrame called review_dates with
#    four columns in the following order: first_reviewed, last_reviewed,
#    nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.
review_dates = pd.DataFrame({'first_reviewed': [first_reviewed], 'last_reviewed': [last_reviewed], 'nb_private_rooms': [nb_private_rooms], 'avg_price': [avg_price]})
print(review_dates)

