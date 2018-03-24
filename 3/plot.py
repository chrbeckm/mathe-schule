import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat

x = np.linspace(-10,10)

plt.plot(x, -5*x+1, 'b-', label='f(x)')
plt.plot(0, 1, 'bx')
plt.plot(0.2, 0, 'bx')

plt.plot(x, -(3/5)*x+3, 'g-', label='g(x)')
plt.plot(0, 3, 'gx')
plt.plot(5, 0, 'gx')

plt.plot(x, 2*x-2, 'y-', label='h(x)')
plt.plot(0, -2, 'yx')
plt.plot(1, 0, 'yx')

plt.plot(-5/11, 36/11, 'rx', label=r'$\symup{S}_\text{f,g}$')
plt.plot(3/7,-8/7, 'kx', label=r'$\symup{S}_\text{f,h}$')
plt.plot(25/13, 24/13, 'mx', label=r'$\symup{S}_\text{g,h}$')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.legend()
plt.tight_layout(pad=0)
plt.savefig('build/plot.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()
