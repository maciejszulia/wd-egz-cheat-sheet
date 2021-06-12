import numpy as np
import matplotlib.pyplot as plt


x = np.arange(15, 30, 0.07)
y = (np.sqrt(x)+(np.cos(x)/np.sin(x)))
plt.plot(x, np.sqrt(x)+(np.cos(x)/np.sin(x)), label="y = np.sqrt(x)+ (np.cos(x) / np.sin(x))")
plt.axis([15, 30, 0, 100])
plt.legend(loc="best")
plt.ylabel('wartości')
plt.xlabel('argumenty')
plt.title("wykres_zad2")
plt.grid()

plt.tight_layout()
plt.show()