import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(5)
plt.subplot(2, 1, 1)
w1 = np.array([-30, -10, -20, -50, -70])
k1 = ['maroon', 'darkorchid', 'darkmagenta', 'sienna', 'mediumseagreen']
plt.barh(x, w1, color=k1)
plt.xlim(-70, 0)
plt.title("Tytuł1")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()
plt.subplot(2, 1, 2)
x = np.arange(5)
w1 = (20, 10, 27, 7, 50)
w2 = (34, 44, 25, 45, 27)
k1 = ['darkslateblue', 'deepskyblue', 'olive', 'royalblue', 'red']
k2 = ['seagreen', 'darkgreen', 'darkkhaki','lightpink', 'limegreen']
plt.bar(x, w1, color=k1)
plt.bar(x, w2, bottom=w1, color=k2)
plt.title('Tytuł')
plt.ylim(0, 150)
plt.tight_layout()
plt.show()
plt.savefig("wykres5.png")
