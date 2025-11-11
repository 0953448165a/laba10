import csv
import matplotlib.pyplot as plt
import numpy as np

file = "data.csv"
with open(file, encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    data = list(reader)
start_index = 0
for i, row in enumerate(data):
    if row and row[0] == "Country Name":
        start_index = i
        break
header = data[start_index]
rows = data[start_index + 1:]


years = [str(y) for y in range(1991, 2020)]

country1 = "Ukraine"
country2 = "Poland"

def get_country_values(country):
    """Повертає список значень для вибраної країни"""
    for row in rows:
        if row[0].strip().lower() == country.lower():
            values = []
            for y in years:
                idx = header.index(y)
                val = row[idx]
                values.append(float(val) if val else None)
            return values
    return []
values1 = get_country_values(country1)
values2 = get_country_values(country2)
plt.figure(figsize=(10, 6))
plt.plot(years, values1, label=country1, color='red', linewidth=3)
plt.plot(years, values2, label=country2, color='blue', linewidth=3)
plt.title("Динаміка показника Life expectancy at birth (1991–2019)", fontsize=14)
plt.xlabel("Рік", fontsize=12, color='blue')
plt.ylabel("Показник (років)", fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.show()

country_input = input("\nВведіть назву країни для побудови стовпчастої діаграми (наприклад, Ukraine): ")
values_input = get_country_values(country_input)

if not values_input:
    print("Країну не знайдено у файлі.")
else:
    plt.figure(figsize=(10, 6))
    plt.bar(years, values_input, color='green')
    plt.title(f"Показник Life expectancy at birth для {country_input} (1991–2019)", fontsize=14)
    plt.xlabel("Рік", fontsize=12, color='blue')
    plt.ylabel("Показник (років)", fontsize=12, color='blue')
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.show()
