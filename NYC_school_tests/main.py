# 1. Which NYC schools have the best math results?
# The best math results are at least 80% of the *maximum possible score of 800* for math.
# Save your results in a pandas DataFrame called best_math_schools, including
# "school_name" and "average_math" columns, sorted by "average_math" in descending order.

# 2. What are the top 10 performing schools based on the combined SAT scores?
# Save your results as a pandas DataFrame called top_10_schools containing the
# "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in
# descending order.

# 3. Which single borough has the largest standard deviation in the combined SAT score?
# Save your results as a pandas DataFrame called largest_std_dev.
# The DataFrame should contain one row, with: "borough" - the name of the NYC borough
# with the largest standard deviation of "total_SAT". "num_schools" - the number of schools
# in the borough. "average_SAT" - the mean of "total_SAT".
# "std_SAT" - the standard deviation of "total_SAT".
# Round all numeric values to two decimal places.

import pandas as pd

schools = pd.read_csv(".venv/schools.csv")
# print(schools.head())
# print(schools.columns)
# 1.
# math_lim = 800*0.8
# best_math = schools[schools['average_math']>=math_lim]
# best_math_schools = best_math.drop(columns = ['borough', 'building_code',
#       'average_reading', 'average_writing', 'percent_tested'])
# best_math_schools = best_math_schools.sort_values(by = 'average_math', inplace = False)
# print(best_math_schools.head(10))

# 2. Top 10 shools
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
#top_schools = schools.filter(['school_name', 'total_SAT'])
#top_schools = top_schools.sort_values(by = 'total_SAT', ascending=False)
#top_10_schools = top_schools.head(10)
#print(top_10_schools)

# 3.

stds = schools['total_SAT'].groupby(schools['borough']).std()
borough_name = stds.idxmax()
std_score = round(stds[borough_name],2)
num_schools = schools[schools['borough']==borough_name].shape[0]
average_SAT = round(schools['total_SAT'][schools['borough']==borough_name].mean(),2)
largest_std_dev = {"borough": [borough_name],
                   "num_schools": [num_schools],
                   "average_SAT": [average_SAT],
                   "std_SAT": [std_score]}
largest_std_dev = pd.DataFrame(largest_std_dev)
print(largest_std_dev)

