import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([2.0, 4.0, 1.0])
xpoint = np.array([1,2,3])

plt.plot(xpoint, ypoints)

plt.title("Sample graph")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.show()