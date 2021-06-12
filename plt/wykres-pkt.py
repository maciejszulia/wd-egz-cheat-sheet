import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 6, 6]
y = [5, 2, 4, 0, 11, 1, 4, 9, 3, 10, 5]

plt.scatter(x, y, label='kropki', color='orange', s=150, marker='v')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()