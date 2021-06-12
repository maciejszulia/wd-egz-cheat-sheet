import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ramka = pd.read_csv('automobile.csv', sep=';', header=0)

ramka = ramka[(170 < ramka['Length'])]

ramka = ramka.groupby(['Car model']).agg({'Car model': ['count']})

wyk = ramka.plot.pie(autopct='%.2lf %%', subplots=True)

plt.title("WYKRES")


plt.xlabel("OŚ X")
plt.ylabel("OŚ Y")

plt.savefig("WYKRES.png")

plt.show()
