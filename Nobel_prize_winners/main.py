# Analyze Nobel Prize winner data and identify patterns by answering the
# following questions:

# 1. What is the most commonly awarded gender and birth country?
# Store your answers as string variables top_gender and top_country.

# 2. Which decade had the highest ratio of US-born Nobel Prize winners to
#    total winners in all categories?
#Store this as an integer called max_decade_usa.

# 3. Which decade and Nobel Prize category combination had the highest
#    proportion of female laureates?
#Store this as a dictionary called max_female_dict where the decade is the key and the category is the value. There should only be one key:value pair.

# 4. Who was the first woman to receive a Nobel Prize, and in what category?
#Save your string answers as first_woman_name and first_woman_category.

# 5. Which individuals or organizations have won more than one Nobel Prize
#    throughout the years?
#Store the full names in a list named repeat_list.


import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv('nobel.csv')
# ['year', 'category', 'prize', 'motivation', 'prize_share', 'laureate_id',
#  'laureate_type', 'full_name', 'birth_date', 'birth_city', 'birth_country',
#  'sex', 'organization_name', 'organization_city', 'organization_country',
#  'death_date', 'death_city', 'death_country'],

# 1.
#d1 = df['year'].groupby(df['sex']).count()
#top_gender = d1.idxmax()

#d2 = df['year'].groupby(df['birth_country']).count()
#top_country = d2.idxmax()

# 2.
df['year'] = pd.to_numeric(df['year'])
decade = []
for year in df['year']:
    val = (year//10)*10
    decade.append(val)
df['decade'] = decade

#us_born_winners = df[df['birth_country'] == "United States of America"]
#us_rat = (us_born_winners['year'].groupby(us_born_winners['decade']).count()) / (df['year'].groupby(df['decade']).count())
#max_decade_usa = us_rat.idxmax()


# 3.
is_female=[]
for val in df['sex']:
    if val=='Female': is_female.append(True)
    else: is_female.append(False)
df['Female'] = is_female

dnew = df['Female'].groupby([df['decade'], df['category']]).mean()
ans = dnew.idxmax()

max_female_dict = {str(ans[0]): [ans[1]]}

# 4.
female_winners = df[df['sex']=='Female']
first_woman = female_winners[female_winners['year']==female_winners['year'].min()]
first_woman_name = first_woman['full_name'].values[0]
first_woman_category = first_woman['category']
print(first_woman_name)
# 5.
drep = df['full_name'].groupby(df['full_name']).count()
repeat_winners = drep[drep>1]
repeat_list = repeat_winners.index.tolist()


dd = df[['year', 'birth_country']]