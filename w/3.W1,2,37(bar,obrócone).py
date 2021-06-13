import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(5)
plt.subplot(3, 2, 1)
w1 = np.array([-30, -10, -20, -50, -70])
k1 = ['maroon', 'darkorchid', 'darkmagenta', 'sienna', 'mediumseagreen']
plt.barh(x, w1, color=k1)
plt.xlim(-70, 0)
plt.xticks(np.arange(-60,1,20))
plt.title("Tytuł1")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()
plt.subplot(3, 2, 6)
w1 = np.array([30, 10, 20, 50, 70])
k1 = ['limegreen', 'darkmagenta', 'c', 'aquamarine', 'forestgreen']
plt.barh(x, w1, color=k1)
plt.xlim(0,70)
plt.xticks(np.arange(0,70,20))
plt.title("Tytuł2")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()
plt.savefig("wykres3.png")
plt.show()
