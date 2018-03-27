import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams.update({
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'pgf.texsystem': 'lualatex',
    'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}'
})
from uncertainties import ufloat
import matplotlib.axes as Axes

x = np.linspace(-10,10)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.grid()
plt.legend()
plt.tight_layout(pad=0)

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

plt.savefig('build/plot.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

