import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


X = ['Group A', 'Group B', 'Group C', 'Group D']
Ygirls = [10, 20, 20, 40]
Zboys = [20, 30, 25, 30]

X_axis = np.arange(len(X))

plt.bar(X_axis - 0.2, Ygirls, 0.4, label='Girls')
plt.bar(X_axis + 0.2, Zboys, 0.4, label='Boys')

plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.savefig('wykres1.png')
plt.show()
