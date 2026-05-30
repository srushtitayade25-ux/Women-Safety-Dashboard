import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("crime.csv")

# Create Total Crimes column
df["Total_Crimes"] = (
    df["Rape"] +
    df["Kidnapping and Abduction"] +
    df["Dowry Deaths"] +
    df["Assault on women with intent to outrage her modesty"] +
    df["Insult to modesty of Women"] +
    df["Cruelty by Husband or his Relatives"] +
    df["Importation of Girls"]
)

# Year-wise crime trend
yearly_crimes = df.groupby("Year")["Total_Crimes"].sum()

# Plot graph
plt.figure(figsize=(10,6))

yearly_crimes.plot(
    kind="line",
    marker="o",
    linewidth=3,
    color="#930303"
)

plt.title(
    "Crime Trend Over Years",
    fontsize=18,
    fontweight="bold",
    pad=20
)

plt.plot(
    yearly_crimes.index,
    yearly_crimes.values,
    marker="o",
    linewidth=3,
    color="#930303"
)

plt.xlabel("Year")
plt.ylabel("Total Crimes")

plt.grid(
    linestyle="--",
    alpha=0.6
)

plt.tight_layout()

plt.savefig(
    "year_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

