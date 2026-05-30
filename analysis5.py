import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATASET
# -----------------------------

df = pd.read_csv("crime.csv")

# -----------------------------
# CLEAN DISTRICT NAMES
# -----------------------------

# Convert district names to lowercase for filtering
df["district"] = df["district"].str.lower()

# Remove invalid summary rows
invalid_districts = [
    "total",
    "zz total",
    "total district(s)",
    "delhi ut total"
]

df = df[~df["district"].isin(invalid_districts)]

# Convert back to title case
df["district"] = df["district"].str.title()

# -----------------------------
# CREATE TOTAL CRIMES COLUMN
# -----------------------------

df["Total_Crimes"] = (
    df["Rape"] +
    df["Kidnapping and Abduction"] +
    df["Dowry Deaths"] +
    df["Assault on women with intent to outrage her modesty"] +
    df["Insult to modesty of Women"] +
    df["Cruelty by Husband or his Relatives"] +
    df["Importation of Girls"]
)

# -----------------------------
# TOP 10 DANGEROUS DISTRICTS
# -----------------------------

district_crimes = df.groupby("district")["Total_Crimes"].sum()

# Sort values
top_districts = district_crimes.sort_values(
    ascending=False
).head(10)

# -----------------------------
# PLOT GRAPH
# -----------------------------

plt.figure(figsize=(14,7))

top_districts.plot(
    kind="bar",
    color="darkred"
)

plt.title(
    "Top 10 Dangerous Districts",
    fontsize=16
)

plt.xlabel(
    "District",
    fontsize=12
)

plt.ylabel(
    "Total Crimes",
    fontsize=12
)

plt.xticks(
    rotation=30,
    ha="right"
)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.7
)

plt.tight_layout()

plt.show()

# -----------------------------
# PRINT TOP DISTRICTS
# -----------------------------

print("\nTop 10 Dangerous Districts:\n")
print(top_districts)

# Export cleaned dataset
df.to_csv(
    "cleaned_crime_data.csv",
    index=False
)

print(
    "\nCleaned dataset exported successfully."
)