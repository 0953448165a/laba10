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
def get_country_values(country):
    for row in rows:
        if row[0].strip().lower() == country.lower():
            values = []
            for y in years:
                idx = header.index(y)
                val = row[idx]
                values.append(float(val) if val else None)
            return values
    return None
print("Введіть країни через кому (наприклад: Ukraine, Poland, Germany):")
user_input = input("> ")
countries = [c.strip() for c in user_input.split(",")]
plot_data = {}
for c in countries:
    vals = get_country_values(c)
    if vals:
        plot_data[c] = vals
    else:
        print(f" Дані для '{c}' не знайдені у файлі.")
if not plot_data:
    print(" Немає жодної країни для побудови графіка.")
    exit()
x = np.arange(len(years))
width = 0.8 / len(plot_data)  
plt.figure(figsize=(14, 7))
for i, (country, values) in enumerate(plot_data.items()):
    plt.bar(x + i * width, values, width, label=country)
plt.title("Порівняння показників між країнами (1991–2019)", fontsize=14)
plt.xlabel("Рік", fontsize=12)
plt.ylabel("Показник", fontsize=12)
plt.xticks(x + width, years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
