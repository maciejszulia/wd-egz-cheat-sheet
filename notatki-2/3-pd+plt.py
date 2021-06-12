import pandas as pd
import matplotlib.pyplot as plt


dataf = pd.read_csv('automobile.csv', header=0, sep=';')

dataf_2 = dataf.groupby(['Car model']).agg({'Car model': ['count']})


wykres_zad3 = dataf_2.plot.bar(orientation='horizontal')
plt.axis([0, 25, 0, 50])
plt.grid()
plt.legend("ilosc")
plt.xlabel("samochod")
plt.ylabel("wystapiena")
plt.title("samochody")
plt.tight_layout()

plt.show()