# Initialize
import numpy as np
import matplotlib.pyplot as plt

# Prepare
X = np.linspace(0, 4 * np.pi, 1000)
Y = np.sin(X)

# Render
fig, ax = plt.subplots()
ax.plot(X, Y)
plt.show()
