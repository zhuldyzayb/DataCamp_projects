import pandas as pd
import matplotlib.pyplot as plt
import pingouin as pg
from scipy.stats import mannwhitneyu
pd.set_option('display.max_columns', None)

men_res = pd.read_csv('men_results.csv')
women_res = pd.read_csv('women_results.csv')
# ('date', 'home_team', 'away_team', 'home_score', 'away_score', 'tournament')

men_res['date'] = pd.to_datetime(men_res['date'])
women_res['date'] = pd.to_datetime(women_res['date'])
men_res = men_res[(men_res['date'] > pd.Timestamp('2002-01-01')) & (men_res['tournament'] == 'FIFA World Cup')]
women_res = women_res[(women_res['date'] > pd.Timestamp('2002-01-01')) & (women_res['tournament'] == 'FIFA World Cup')]

men_res['total_score'] = men_res['home_score'] + men_res['away_score']
women_res['total_score'] = women_res['home_score'] + women_res['away_score']
men_res['group'] = 'men'
women_res['group'] = 'women'

comb = pd.concat([men_res, women_res], axis = 0, ignore_index=True)
comb = comb[['group', 'total_score']]
temp = comb.pivot(columns='group', values='total_score')
res = pg.mwu(x=temp['women'], y=temp['men'], alternative='greater')
result_dict = {"p_val": res['p-val'].values[0], "result": "reject"}


