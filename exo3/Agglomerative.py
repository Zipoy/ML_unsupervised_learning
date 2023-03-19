import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plot
import sys

np.set_printoptions(threshold=sys.maxsize)
data = np.load('data/data.npy')

# Elbow method to dertermine hte optimal number of cluster
filename = 'Agglomerative_Elbow.png'
icss = []
for i in range(1, 11):
    agg_clustering = AgglomerativeClustering(n_clusters=i, linkage='ward')
    agg_clustering.fit(data)
    icss.append(np.sum((data - np.mean(data[agg_clustering.labels_], axis=0))**2))
plot.plot(range(1, 11), icss)
plot.title('Elbow Method for Agglomerative Clustering')
plot.xlabel('Number of clusters')
plot.ylabel('ICSS')
plot.savefig('images/Agglomerative/' + filename)
plot.clf()

# Silhouette method to dertermine hte optimal number of cluster
filename = 'Agglomerative_Silhouette.png'
sil_scores = []
for i in range(2, 11):
    agg_clustering = AgglomerativeClustering(n_clusters=i, linkage='ward')
    agg_clustering.fit(data)
    score = silhouette_score(data, agg_clustering.labels_)
    sil_scores.append(score)
plot.plot(range(2, 11), sil_scores)
plot.title('Silhouette Method for Agglomerative Clustering')
plot.xlabel('Number of clusters')
plot.ylabel('Silhouette score')
plot.savefig('images/Agglomerative/' + filename)
plot.clf()

# Elbow method with optimal number of cluster
n_clusters_elbow = 5
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters_elbow, linkage='ward')
agg_clustering.fit(data)
labels = agg_clustering.labels_
original_stdout = sys.stdout
with open('data/Agglomerative/lables_elbow.txt', "w") as f:
    sys.stdout = f
    print(labels)
    sys.stdout = original_stdout

# Silhouette method with optimal number of cluster
n_clusters_silhouette = 6
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters_silhouette, linkage='ward')
agg_clustering.fit(data)
labels = agg_clustering.labels_
silhouette_score = silhouette_score(data, labels)
original_stdout = sys.stdout
with open('data/Agglomerative/lables_silhouette.txt', "w") as f:
    sys.stdout = f
    print(labels)
    print(f"Silhouette score for Agglomerative with {n_clusters_silhouette} clusters: {silhouette_score}")
    sys.stdout = original_stdout
