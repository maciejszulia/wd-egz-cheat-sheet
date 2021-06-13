import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

fig, ax1 = plt.subplots()
x = np.arange(0.00, 15.0, 0.01)

ax1.plot(x, np.log(x), 'g')
ax1.set_xlabel('x')

ax1.set_ylabel('ln(x)', color='g')
ax1.tick_params('y', colors='g')

ax2 = ax1.twinx()
s2 = x**2+x
ax2.plot(x, s2, linestyle='--', color='red')
ax2.set_ylabel('x^2+x', color='red')
ax2.tick_params('y', colors='red')
plt.title('Dwa wykresy')

fig.tight_layout()
plt.show()

plt.savefig("wykres6.png")