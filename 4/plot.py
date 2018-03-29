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

x = np.linspace(0,4,1000)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel('t')
plt.ylabel('f(t)')
plt.xlim(0, 4.1)
plt.ylim(-3.2, 3.2)
plt.grid()
plt.legend()
plt.tight_layout(pad=0)

plt.plot(x, x**3-6*x**2+8*x, 'b-', label='f(t)')

plt.savefig('build/plot.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel('t')
plt.ylabel('f(t)')
plt.xlim(0, 4.1)
#plt.ylim(-4, 4)
plt.grid()
plt.legend()
plt.tight_layout(pad=0)

plt.plot(x, -x**4+8*x**3-20*x**2+15*x+2, 'b-', label='f(t)')

plt.savefig('build/plot2.pdf', bbox_inches='tight', pad_inches=0)
plt.clf()

