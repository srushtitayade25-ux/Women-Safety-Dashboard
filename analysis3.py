import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("crime.csv")

# Crime categories
crime_categories = [
    "Rape",
    "Kidnapping and Abduction",
    "Dowry Deaths",
    "Assault on women with intent to outrage her modesty",
    "Insult to modesty of Women",
    "Cruelty by Husband or his Relatives",
    "Importation of Girls"
]

# Calculate total crimes for each category
crime_totals = df[crime_categories].sum()

# Create graph
plt.figure(figsize=(14,7))

crime_totals.sort_values(ascending=False).plot(
    kind="bar",
    color="purple"
)

plt.title(
    "Most Common Crime Types Against Women",
    fontsize=16
)

plt.xlabel("Crime Type", fontsize=12)
plt.ylabel("Total Cases", fontsize=12)

plt.xticks(rotation=25, ha="right")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.show()

