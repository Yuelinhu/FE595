import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6.28,0.01)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y)
plt.plot(x,z)