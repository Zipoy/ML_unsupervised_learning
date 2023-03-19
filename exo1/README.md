# Part 1 : Data distribution and the law of large numbers

Our 2-dimensional variable Z = (X, Y) represent the height `X` and weight `Y` of individuals in a population.

X is a continuous random variable representing height with a normal distribution of mean 170 cm and standard deviation of 10 cm.
Y is a continuous random variable representing weight with a normal distribution of mean 70kg and standard deviation of 10kg.

The mean and standard deviation correspond to :
```python
mean_x, stdDerivation_x
mean_y, stdDerivation_y
```
We sample n = 1000 points and we also save this sample has a plot in the images folder.
File name is `samples_*.png`.

We calculate the empirical average using numpy, plot the result and save it in the images folder.
The name of the file is `empirical_average_*.png`.