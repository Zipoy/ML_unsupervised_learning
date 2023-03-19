import numpy as np
import matplotlib.pyplot as plot
import datetime

mean_x, std_derivation_x = 170, 10
mean_y, std_derivation_y = 70, 10
n = 1000

x = np.random.normal(mean_x, std_derivation_x, n)
y = np.random.normal(mean_y, std_derivation_y, n)

filename_s = 'samples_' + str(int(datetime.datetime.now().timestamp())) + '.png'
plot.scatter(x, y, s=5)
plot.xlabel('Height (cm)')
plot.ylabel('Weight (kg)')
plot.savefig('images/' + filename_s)
plot.clf()

empirical_mean_x = np.zeros(n)
empirical_mean_y = np.zeros(n)
for i in range(n):
    empirical_mean_x[i] = np.mean(x[:i+1])
    empirical_mean_y[i] = np.mean(y[:i+1])

distance = np.sqrt((empirical_mean_x - mean_x)**2 + (empirical_mean_y - mean_y)**2)

filename_ea = 'empirical_average_' + str(int(datetime.datetime.now().timestamp())) + '.png'
plot.plot(range(1, n+1), distance)
plot.xlabel('Number of samples')
plot.ylabel('Distance to expected value')
plot.savefig('images/' + filename_ea)
