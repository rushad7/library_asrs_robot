import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("dist_data.csv")
dist = data["dist"]
shelf_dist = data["shelf_dist"]

plt.xlabel("Distance Traveled by robot")
plt.ylabel("Distance between robot and shelf")
plt.plot(dist,shelf_dist)
plt.show()
