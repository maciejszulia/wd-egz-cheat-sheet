import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(6)
w1 = (20, 10, 30, 10, 50, 0)
w2 = (85, 67, 50, 12, 0, 0)
k1 = ['darkslateblue', 'deepskyblue', 'olive', 'royalblue', 'limegreen', 'w']
k2 = ['seagreen', 'darkgreen', 'darkkhaki','lightpink', 'limegreen', 'w']
plt.bar(x, w1, color=k1)
plt.bar(x, w2, bottom=w1, color=k2)
plt.plot([0, 1 , 2, 3, 4, 5],[120, 120, 120, 120, 120, 120], color='g')
plt.title('Tytuł')
plt.xlim(-0.65, 5.2)
plt.ylim(0, 150)
plt.tight_layout()
plt.show()
plt.savefig("wykres8.png")