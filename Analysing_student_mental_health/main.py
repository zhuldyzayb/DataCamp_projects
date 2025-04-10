# Explore and analyze the students data to see how the length of stay
# (stay) impacts the average mental health diagnostic scores of the
# international students present in the study.

# Return a table with nine rows and five columns.
# - The five columns should be aliased as: stay, count_int, average_phq,
#   average_scs, and average_as, in that order.
# - The average columns should contain the average of the todep (PHQ-9 test),
#   tosc (SCS test), and toas (ASISS test) columns for each length of stay,
#   rounded to two decimal places.
# - The count_int column should be the number of international students for each length of stay.
#   Sort the results by the length of stay in descending order.

import pandas as pd

# Load the data from the CSV file
data = pd.read_csv("students.csv")

# Drop missing values
data = data.dropna()

# Create a new DataFrame with the required columns
newdata = pd.DataFrame({
    "stay": data['stay'].value_counts().sort_index().index,
    "count_int": data['stay'].value_counts().sort_index().values,
    "average_phq": data.groupby('stay')['todep'].mean().values,
    "average_scs": data.groupby('stay')['tosc'].mean().values,
    "average_as": data.groupby('stay')['toas'].mean().values
})