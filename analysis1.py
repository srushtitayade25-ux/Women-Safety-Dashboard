import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("crime.csv")
# Clean state names
df["state"] = df["state"].str.title()

# Create total crimes column
df["Total_Crimes"] = (
    df["Rape"] +
    df["Kidnapping and Abduction"] +
    df["Dowry Deaths"] +
    df["Assault on women with intent to outrage her modesty"] +
    df["Insult to modesty of Women"] +
    df["Cruelty by Husband or his Relatives"] +
    df["Importation of Girls"]
)

# Group state-wise
state_crimes = df.groupby("state")["Total_Crimes"].sum()

# Sort and plot top 10 states
top_states = state_crimes.sort_values(
    ascending=False
).head(10)

ax = top_states.plot(
    kind="bar",
   color="#AE0951",
   figsize=(12,7)
)

# Add value labels
for i, value in enumerate(top_states):
    ax.text(
        i,
        value + 10000,
       f"{value:,}",
        ha="center"
    )

# Chart labels
plt.title(
    "Top 10 States with Highest Crimes Against Women",
    fontsize=18,
    fontweight="bold",
    pad=20,
)
plt.xlabel("State", fontsize=12)
plt.ylabel("Crime Count", fontsize=12)

plt.xticks(rotation=45)
plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    "top_states.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
