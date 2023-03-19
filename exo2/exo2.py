import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = np.load('data.npy')
labels = np.load('labels.npy')

pca = PCA()
fitdata = pca.fit_transform(data)

plt.scatter(fitdata[:,0], fitdata[:,1], c=labels)
plt.title('PCA 2D')
plt.show()

fig = plt.figure()
res = fig.add_subplot(projection='3d')
res.scatter(fitdata[:,0], fitdata[:,1], fitdata[:,2], c=labels)
res.set_title('PCA 3D')
plt.show()