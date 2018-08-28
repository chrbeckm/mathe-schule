import numpy as np
import matplotlib.pyplot as plt

ticks = np.linspace(-5, 5, 11)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(-5.5, 5.5)
plt.ylim(-5.5, 5.5)
plt.grid()
plt.tight_layout()
plt.savefig('build/koordleer.pdf')
plt.clf()

ticks = np.linspace(-5, 5, 11)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(-5.5, 5.5)
plt.ylim(-5.5, 5.5)
plt.grid()
x = [-5, 0, 3, -1,  4, -2,  0, -4]
y = [ 0, 4, 2,  4, -4, -3, -1,  2]
for i in range(len(x)):
    plt.plot(x[i], y[i], 'x', label = i+1)
plt.legend()
plt.tight_layout()
plt.savefig('build/koordpunkte.pdf')
plt.clf()

def linear(x,m,b):
    return m*x+b

x = np.linspace(-5.5, 5.5)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(ticks)
plt.yticks(ticks)
plt.xlim(-5.5, 5.5)
plt.ylim(-5.5, 5.5)
plt.grid()
m = [ 1, 0.8, -0.5, -1, 0]
b = [ 0,   4,  3.5, -4, 4]
for i in range(len(m)):
    plt.plot(x, linear(x, m[i], b[i]), '-', label=i+1)
plt.legend()
plt.tight_layout()
plt.savefig('build/koordgeraden.pdf')
