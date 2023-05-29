import numpy as np
import matplotlib.pyplot as plt

years = np.array([2000, 2002, 2005, 2007, 2010])
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

coefficients = np.polyfit(years, percentages, 1)


# zad 1
year = 2023
predicted_percentage = coefficients[0]*year + coefficients[1]
print("Przewidywany procent bezrobotnych w roku {}: {:.3f}%".format(year, predicted_percentage))

# zad 2
year = (12 - coefficients[1]) / coefficients[0]
print("Procent bezrobotnych przekroczy 12% w roku: {:.0f}".format(year))

# zad 3

slope, intercept = np.polyfit(years, percentages, 1)
line = slope * years + intercept

fig, ax = plt.subplots()
ax.plot(years, percentages, 'o', label='Dane')
ax.plot(years, line, label='Regresja liniowa')
ax.legend()

# Dodanie etykiet i tytułu
ax.set_xlabel('Rok')
ax.set_ylabel('Procent bezrobotnych')
ax.set_title('Regresja liniowa procentu bezrobotnych')

# Wyświetlenie wykresu
plt.show()