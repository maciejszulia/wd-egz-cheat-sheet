import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.arange(5)
plt.subplot(2, 2, 1)
w1 = np.array([-30, -10, -20, -50, -70])
k1 = ['maroon', 'darkorchid', 'darkmagenta', 'sienna', 'mediumseagreen']
plt.barh(x, w1, color=k1)
plt.xlim(-70, 0)
plt.xticks(np.arange(-60,1,20))
plt.title("Tytuł1")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()

plt.subplot(2, 2, 4)
x2 = np.array([-2,-1,0,1,2,3])
y2 = np.array([5,4,3,2,1,0])
x1 = np.array([-2,-1,0,1,2,3])
y1 = np.array([-2,-1,0,1,2,3])
plt.plot(x1,y1, 'r^', label="opcja 1")
plt.plot(x2,y2, 'bs', label="opcja 2")
plt.title("tytuł")
plt.yticks(np.arange(-2,4.1,2))
plt.legend(loc='center right')
plt.savefig("wykres4.png")
plt.show()

