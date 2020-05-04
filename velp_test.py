import math
import matplotlib.pyplot as plt

dist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
fp = []

for t in range(len(dist)):
    # testting with a gausian velocity profile
    #SD of profle is set to 10, contros the rate of change of the velocity profile(think of it like acc)
    f = (1/(math.sqrt(2*math.pi*10)))*math.exp((-(dist[t]-(dist[-1]/2))**2)/20)
    fp.append(f/2)

plt.ylim(0,0.3)
plt.plot(dist,fp)
plt.show()
