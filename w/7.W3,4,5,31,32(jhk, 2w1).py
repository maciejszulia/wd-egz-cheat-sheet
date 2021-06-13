import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(5)
w1 = np.array([-90, -5, -60, -55, -3])
w2 = np.array([22, 13, 40, 80, 10])
k1 = ['paleturquoise', 'chocolate', 'sandybrown', 'lightcyan', 'blue']
k2 = ['lightsteelblue', 'palevioletred', 'tab:brown','blueviolet', 'skyblue']
plt.barh(x, w1, color=k1)
plt.barh(x, w2, color=k2)
plt.xlim(-90, 90)
plt.title('Tytuł jhk')
plt.yticks(x, ['A', 'B', 'C', 'D', 'E'])
plt.tight_layout()
plt.show()
plt.savefig("wykres7.png")