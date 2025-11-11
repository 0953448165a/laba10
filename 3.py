import json
import matplotlib.pyplot as plt
file = "employees.json"
with open(file, "r", encoding="utf-8") as f:
    employees = json.load(f)
male_count = sum(1 for e in employees if e["gender"].lower() == "чоловік")
female_count = sum(1 for e in employees if e["gender"].lower() == "жінка")
labels = ["Чоловіки", "Жінки"]
sizes = [male_count, female_count]
colors = ["skyblue", "lightcoral"]
explode = (0.05, 0)  
plt.figure(figsize=(7, 7))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",  # показує відсотки
    startangle=90,
    explode=explode,
    shadow=True
)
plt.title("Розподіл співробітників за статтю", fontsize=14)
plt.legend(title="Стать", loc="best")
plt.show()
