import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})


# 1. Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
# 2. Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)?
#    Save as a string variable called peak_night_crime_location.
# 3. Identify the number of crimes committed against victims of different age groups.
#    Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44",
#    "45-54", "55-64", and "65+" as the index and the frequency of crimes as the values.


crimes['hour'] = crimes['TIME OCC'].astype(str).str[:2].astype(int)
peak_crime_hour = crimes['hour'].value_counts().idxmax()

night_crimes = [22, 23, 0, 1, 2, 3]
crimes['night_crime'] = crimes['hour'].isin(night_crimes)
res = crimes.groupby("AREA NAME")['night_crime'].sum().sort_values(ascending=False)
peak_night_crime_location = res[res==res.max()].index[0]

age_dict = {"0-17":17, "18-25":25, "26-34":34, "35-44":44, "45-54":54, "55-64":64,"65+":65}
def find_age_group(value):
    for key, values in age_dict.items():
        if value <= values:
            return key
    return '65+'
crimes['age_cat'] = crimes['Vict Age'].map(find_age_group)
victim_ages = crimes['age_cat'].value_counts().sort_index()
print(victim_ages)
