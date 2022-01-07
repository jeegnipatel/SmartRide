import inline as inline
import matplotlib
import pandas as pd
import time
import random
import re
import numpy as np
import _pickle as pickle
import matplotlib.pyplot as plt
from driver.views import driverAnswer
from driver.views import searchRider

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import sqlite3

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()
request = driverAnswer()
cur.execute("Select * from rider_question where userid = %s", request.user.username)

df = pd.DataFrame.from_records(cur.fetchall(),
                               columns = [desc[0] for desc in cur.description])

# df.to_csv("temp.csv", index=False)
df = pd.read_csv("temp.csv", index_col=False)
print(df['talkative'])

# Loading in the cleaned DF
# with open("profiles.pkl",'rb') as fp:
#     data = pickle.load(fp)

# Scaler to scale the data
scaler = StandardScaler()

# Scaling the categories then replacing the old values
#df['talkative'] = dict([(y,x+1) for x,y in enumerate(sorted(set(df['talkative'][0:])))])

variety_num = {'Yes': 1, 'No': 0, 'Any': 2, 'NewUser1': 3}

df['talkative'] = df['talkative'].map(variety_num)
df['timedriving'] = df['timedriving'].map(variety_num)
df['music'] = df['music'].map(variety_num)
df['workstudent'] = df['workstudent'].map(variety_num)
df['male'] = df['male'].map(variety_num)
df['female'] = df['female'].map(variety_num)
df['userid'] = df['userid'].map(variety_num)
df['driverid'] = df['driverid'].map(variety_num)

df.drop_duplicates(inplace=True)

final_df = df[['talkative','timedriving','music','male','female','workstudent']].join(pd.DataFrame(scaler.fit_transform(
            df.drop(['talkative','timedriving','music','male','female','workstudent'], axis=1)), columns=df.columns[5:], index=df.index))

# defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters=2, init='k-means++')

# fitting the k means algorithm on scaled data
kmeans.fit(final_df)

# fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_clusters = cluster, init='k-means++')
    kmeans.fit(final_df)
    SSE.append(kmeans.inertia_)

# converting the results into a dataframe and plotting them
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

# k means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_clusters = 7, init='k-means++')
kmeans.fit(final_df)
pred = kmeans.predict(final_df)

frame = pd.DataFrame(final_df)
frame['cluster'] = pred
frame['cluster'].value_counts()

Cluster_assignments = kmeans.labels_

## Running the model on a new user
arr = np.array([0,1,-1.9872,-0.5821,1.4447,-0.53097])

newarr = arr.reshape(1, 6)

print(kmeans.predict(newarr))

searchRider(frame)

