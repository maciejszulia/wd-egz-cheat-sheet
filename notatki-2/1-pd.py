import pandas as pd
import matplotlib.pyplot as plt

dataf = pd.read_csv('automobile.csv', header=0, sep=';')
# print(dataf)

dataf_2 = dataf[(dataf['Length'] > 170)]
# print(dataf2)

dataf_3 = dataf_2.groupby(['Car model']).agg({'Car model': ['count']})
# print(dataf_3)

wykres = dataf_3.plot.pie(subplots=True, autopct='%.2f %%')
plt.title("wykres_zad1")
# plt.ylabel('y')
# plt.xlabel('x')
plt.tight_layout()
plt.savefig("wykres_zad1.png")

plt.show(