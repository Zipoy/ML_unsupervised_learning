import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plot
import sys

np.set_printoptions(threshold=sys.maxsize)
data = np.load('data/data.npy')

# Elbow method method to dertermine hte optimal number of cluster
filename = 'KMeans_Elbow.png'
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
plot.plot(range(1, 11), wcss)
plot.title('Elbow Method for KMeans')
plot.xlabel('Number of clusters')
plot.ylabel('WCSS')
plot.savefig('images/Kmeans/' + filename)
plot.clf()


# Silhouette method method to dertermine hte optimal number of cluster
filename = 'KMeans_Silhouette.png'
sil_scores = []
for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(data)
    score = silhouette_score(data, kmeans.labels_)
    sil_scores.append(score)
plot.plot(range(2, 11), sil_scores)
plot.title('Silhouette Method for KMeans')
plot.xlabel('Number of clusters')
plot.ylabel('Silhouette score')
plot.savefig('images/Kmeans/' + filename)
plot.clf()

# Elbow method with optimal number of cluster
n_clusters_elbow = 4
kmeans = KMeans(n_clusters=n_clusters_elbow)
kmeans.fit(data)
labels = kmeans.labels_
original_stdout = sys.stdout
with open('data/Kmeans/lables_elbow.txt', "w") as f:
    sys.stdout = f
    print(labels)
    sys.stdout = original_stdout

# Silhouette method with optimal number of cluster
n_clusters_silhouette = 6
kmeans = KMeans(n_clusters=n_clusters_silhouette, random_state=42)
labels = kmeans.fit_predict(data)
silhouette_score = silhouette_score(data, labels)
original_stdout = sys.stdout
with open('data/Kmeans/lables_silhouette.txt', "w") as f:
    sys.stdout = f
    print(labels)
    print(f"Silhouette score for KMeans with {n_clusters_silhouette} clusters: {silhouette_score}")
    sys.stdout = original_stdout
