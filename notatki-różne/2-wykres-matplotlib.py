import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(15, 30, 50)

y = np.sqrt(x) + (np.cos(x)) / (np.sin(x))
plt.plot(x, y, label="sqrt(x)+(cos(x))/(sin(x))")
plt.legend()
plt.xlim([15, 30])
plt.ylabel("Oś Y")
plt.xlabel("Oś X")
plt.title("Wykres funckji")
plt.show()
