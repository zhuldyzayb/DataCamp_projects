import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import seaborn as sns
penguins = pd.read_csv('penguins.csv')
## convert gender into numeric
penguins['sex'] = penguins['sex'].apply(lambda x: 1 if x=='MALE' else 0)
## there are no missing values in the data
#print(penguins.describe())

## pairwise plots to take a look
sns.pairplot(penguins)
plt.show()
## based on the plots there is no significant difference between genders
penguins = penguins.drop(columns='sex')

###########  A  ############
print("Non-normalised mass, prior KMeans")
print(penguins.head())
model = KMeans(n_clusters=3,  init='random', random_state=123).fit(penguins)
stat_penguins = pd.DataFrame(model.cluster_centers_)
stat_penguins.columns = penguins.columns


###########  B  ############
def myClusteringFunc(df, n_clusters, eps):
    # The function performs clustering for the given dataframe df & number of clusters n_clusters
    # eps = chosen machine precision value, s.t. once the updates are smaller than eps we stop

    # Initialise the original
    df['cluster'] = None
    init = df.sample(n_clusters, random_state = 123).reset_index(drop=True)
    for i in range(len(df)):
        distances = ((init - df.iloc[i]) ** 2).sum(axis=1)
        df.loc[i, 'cluster'] = distances.idxmin()
        means = df.groupby('cluster').mean()

    oldmean = init
    while ((abs(oldmean - means).max()>eps).all()):
        for i in range(len(df)):
            distances = ((means - df.iloc[i]) ** 2).sum(axis=1)
            df.loc[i, 'cluster'] = distances.idxmin()
            oldmean = means
            means = df.groupby('cluster').mean()
    return means
check = myClusteringFunc(penguins, n_clusters=3, eps = 0.001)
print(check)
print(stat_penguins)
## Cluster centers are quite similar

## There is an option to normalise the mass so that it would not skew the clustering algorithm
penguins = penguins.drop(columns = 'cluster')
penguins['body_mass_g'] = (penguins['body_mass_g'] - penguins['body_mass_g'].min())/(penguins['body_mass_g'].max() - penguins['body_mass_g'].min())
sklearn_clusters = pd.DataFrame(KMeans(n_clusters=3,  init='random', random_state=123).fit(penguins).cluster_centers_)
my_clusters = myClusteringFunc(penguins, n_clusters=3, eps = 0.001)
print(sklearn_clusters)
print(my_clusters)

