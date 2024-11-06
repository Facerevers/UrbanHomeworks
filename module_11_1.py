import matplotlib.pyplot as plt
import numpy as np
"""create simple line"""
x = np.linspace(0,25, 50)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sin graph')
plt.xlabel('y')
plt.ylabel('sin(x)')
plt.grid()
plt.show()

"""hystogramm"""

data = np.random.randn(1000)

plt.hist(data, bins=20, edgecolor='red')
plt.xlabel('Numb')
plt.ylabel('Freq')
plt.grid()
plt.show()

"""Scatter PLot"""
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y, color='green', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

"""few lines"""

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()

"""subplots"""

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, axs = plt.subplots(2)
fig.suptitle('Sin & Cos')

axs[0].plot(x, y1, 'tab:red')
axs[0].set_ylabel('sin(x)')
axs[0].grid()

axs[1].plot(x, y2, 'tab:blue')
axs[1].set_ylabel('cos(x)')
axs[1].set_xlabel('x')
axs[1].grid()

plt.show()

"""save graph to file"""

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sin graph')

plt.savefig('sin_graph.png')
plt.show()