import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(0, 5, 0.1)
plt.plot([0, 1, 2, 3, 4, 5, 6, 7], [2, 1, -2, -3, 2, -3, 2, -2], color='steelblue', label='33')
plt.plot([-2, -1, 0, 1, 3, 5], [3, -3, 3, 1, 3, 1], color='orange', label='333')
plt.grid()
plt.legend(loc='center left')
plt.ylabel('oś y')
plt.xlabel('oś x')
plt.title('Tytuł1')
plt.text(2.34, 0.5, 'ABCD')
plt.show()
plt.savefig("wykres11.png")