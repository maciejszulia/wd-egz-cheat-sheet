import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(5)
w1 = (20, 0, 30, 10, 60)
w2 = (30, 50, 40, 70, 20)
k1 = ['darkslateblue', 'deepskyblue', 'olive', 'royalblue', 'limegreen']
k2 = ['seagreen', 'darkgreen', 'darkkhaki','lightpink', 'limegreen']
plt.bar(x, w1, color=k1)
plt.bar(x, w2, bottom=w1, color=k2)
plt.plot([0, 1 , 2, 3, 4],[130, 130, 130, 130, 130])
plt.title('Tytuł')
plt.xlim(-0.6, 4.6)
plt.ylim(0, 130)
plt.tight_layout()
plt.savefig("wykres10.png")
plt.show()

