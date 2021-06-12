import matplotlib.pyplot as plt

# https://www.statista.com/chart/21017/...

names = ['python', 'java', 'javascript', 'c#', 'php', 'c/c++', 'inne']
percentages = [29.9, 19.1, 8.2, 7.3, 6.2, 5.9, 76.6]
colors = ['deepskyblue', 'orange', 'yellow', 'green', 'purple', 'blue', 'grey']
# https://matplotlib.org/2.0.2/examples...

plt.pie(percentages,
        labels=names,
        colors=colors,
        shadow=True,
        explode=(0.2, 0.1, 0, 0, 0, 0, 0),
        autopct='%.1f%%'
        )

plt.title("Najpopularniejsze jezyki programowania 2020")

plt.legend()

plt.show()