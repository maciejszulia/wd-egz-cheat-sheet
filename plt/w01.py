import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
plt.subplot(3, 2, 1)
w1 = np.array([-30, -11, -20, -50, -70])
k1 = ['violet', 'darkmagenta', 'yellowgreen', 'lawngreen', 'beige']
plt.barh(x, w1, color=k1)
plt.title("Tytuł1")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()
plt.subplot(3, 2, 6)
w2 = w1 * (-1)
k1 = ['indigo', 'hotpink', 'crimson', 'darkred', 'mediumvioletred']
plt.barh(x, w2, color=k1)
plt.title("Tytuł2")
plt.yticks(x, [6, 10, 8, -2, 2])
plt.tight_layout()
plt.show()
