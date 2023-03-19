
# Part 3 : company clustering customers

For this exercise we use the the following clustrenig methods :
- K-Means
- Agglomerative
And for the following heuristic to choose a relevant number of cluster :
- Elbow
- Silhouette

You will find in the images folder all the plot we generate to choose the most relevant number of cluster for each heuritics and clustering methods.

We determined that for the K-Means methods and the Elbow heuritics the optimal number of cluster is 4, and for the Silhouette heuristic is 6.

We determined that for the Agglomerative methods and the Elbow heuritics the optimal number of cluster is 4, and for the Silhouette heuristic is 6.

We find that the K-Means clustering method and the Silhouette heuristic are a better choice in this situation because K-Means uses both inter- and intra-group distances in its scoring function, whereas the elbow method only uses intra-group distances.