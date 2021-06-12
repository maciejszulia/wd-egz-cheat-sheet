import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {'a': np.random.randint(124, 230, 100),
        'b': np.random.randint(50, 100, 100),
        'c': np.random.randint(1, 9, 100)}

plt.subplots(figsize=(7, 8))
sns.scatterplot(data['a'], data['b'], legend=True, label='Kropki', palette='Set2', hue=data['c'])
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.title('Losowe liczby w stosunku do losowych liczb')
plt.show()