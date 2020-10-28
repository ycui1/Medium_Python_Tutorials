#%%
import matplotlib.pyplot as plt
distortions = [680, 350, 100, 90, 80, 75, 60, 55, 52, 45]

plt.plot(range(1, 11), distortions, marker='s')
plt.title("The Elbow Method")
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortion')
plt.show()
