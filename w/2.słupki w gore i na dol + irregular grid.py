import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
data1 = [0,85, 72, 43, 52]
data2 = [-42, -35, 0, -16, -9]
plt.bar(range(len(data1)), data1)
plt.bar(range(len(data2)), data2)
plt.savefig("wykres2-1.png")
plt.show()



# =========================

data = [23, 45, 56, 78, 213]

plt.bar(range(len(data)), data, color='royalblue', alpha=0.7)
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.yticks([4,7,28,56,122,136,189])
plt.savefig("wykres2-2.png")
plt.show()
