import matplotlib.pyplot as plt

# ceny od 14 do 24 marca wg www.worldforexrates.com
eur = [4.58, 4.58, 4.59, 4.60, 4.60, 4.62, 4.63, 4.63, 4.62, 4.60, 4.62]
chf = [4.12, 4.12, 4.15, 4.17, 4.17, 4.18, 4.17, 4.17, 4.18, 4.17, 4.18]
usd = [3.83, 3.85, 3.86, 3.85, 3.88, 3.88, 3.88, 3.89, 3.85, 3.90, 3.91]

labels = ['USD', 'CHF', 'EUR']

plt.stackplot(range(14, 25), eur, chf, usd, colors=['blue', 'r', 'g'], labels=labels)

plt.ylabel("Cena wyrazona w PLN")
plt.xlabel("Marzec 2021")
plt.title("Ceny walut")

plt.legend()

plt.show()