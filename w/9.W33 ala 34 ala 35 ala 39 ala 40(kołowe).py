import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.subplot(2, 2, 1)
labels2 = 'A', 'B', 'C', 'D', 'E'
sizes2 = [23, 13, 30, 3, 30]
colors2 = ['mistyrose', 'lawngreen', 'lightsteelblue', 'mediumorchid', 'peru']
plt.title('Tytuł1')
plt.pie(sizes2, labels=labels2, autopct='%1.0f%%',
        shadow=False, colors=colors2)
plt.subplot(2, 2, 2)
labels2 = 'A', 'B', 'C', 'D', 'E'
sizes2 = [10, 19, 21, 24, 26]
colors2 = ['cornflowerblue', 'blueviolet', 'mediumorchid', 'yellowgreen', 'dodgerblue']
plt.title('Tytuł2')
plt.pie(sizes2, labels=labels2, autopct='%1.0f%%',
        shadow=False, colors=colors2)
plt.subplot(2, 2, 3)
labels2 = 'A', 'B', 'C', 'D', 'E'
sizes2 = [39, 1, 44, 2, 13]
colors2 = ['blueviolet', 'g', 'orchid', 'magenta', 'mediumslateblue']
plt.title('Tytuł3')
plt.pie(sizes2, labels=labels2, autopct='%1.0f%%',
        shadow=False, colors=colors2)
plt.subplot(2, 2, 4)
labels2 = 'A', 'B', 'C', 'D', 'E'
sizes2 = [13, 4, 33, 6, 44]
colors2 = ['aquamarine', 'burlywood', 'rebeccapurple', 'goldenrod', 'yellowgreen']
plt.title('Tytuł4')
plt.pie(sizes2, labels=labels2, autopct='%1.0f%%',
        shadow=False, colors=colors2)
plt.tight_layout()
plt.show()
plt.savefig("wykres9.png")

