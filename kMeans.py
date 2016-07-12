import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv

'''
x=[1, 5, 1.5, 8, 1, 9]
y=[2, 8, 1.8, 8, 0.6, 11]
'''

data=[]
with open(r'Tomato_db_sorted_Lat_Long.csv','rb') as c:
    f=csv.reader(c)
    for row in f:
        data.append([float(row[0]),float(row[1])])
X=np.array(data)
y=X[:,0]
x=X[:,1]

plt.scatter(x,y)
plt.show()

'''X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])'''

kmeans = KMeans(n_clusters=10)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print centroids
print labels

colors = ["g.", "r.","y.","c.","m.","k."]

for i in xrange(len(X)):
    #print "Coordinate:",X[i], "label:",labels[i]
    with open(r'clustersDivision_of_Restaurants.csv','ab') as c:
        f=csv.writer(c)
        f.writerow([X[i][0],X[i][1],labels[i]])
    plt.plot(X[i][1], X[i][0], colors[labels[i]%6], markersize = 10)

plt.scatter(centroids[:, 1],centroids[:, 0], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
