import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'a': np.random.randint(124, 230, 100, dtype='int'),
        'b': np.random.randint(50, 100, 100, dtype='int'),
        'c': np.random.randint(1, 9, 100, dtype='int')
        }

# print(data['a'])
# print(data['b'])
# print(data['c'])

dataf = pd.DataFrame(data)

wykres_seaborn = sns.relplot(data=dataf, x='a', y='b', palette='Set2', hue='c')
plt.title("wykres_zad4")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='best')
plt.tight_layout()
plt.show()