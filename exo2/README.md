# Part 2 : meteorological data : dimensionality reduction and visualization
In order to implement  my dimensionality reduction method, I choose the linear method. 

To do the linear method I used the method PCA in the sklearn librairies.  

Load the data an label -> use PCA -> plot in 2D and 3D 

Which dimension, between 2 and 3, seems to allow to predict the label based on the projected components only ? 

The dimensions wich seems to allow to predict the label is the one in which we can best see the difference between the two classes so I think is the 3D version even if we can clearly see the difference between them in the 2D version.