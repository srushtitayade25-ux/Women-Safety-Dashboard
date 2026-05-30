import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("crime.csv")

# -----------------------------
# CLEAN STATE NAMES
# -----------------------------

# Convert all state names to lowercase first
df["state"] = df["state"].str.lower()

# Remove extra spaces
df["state"] = df["state"].str.strip()

# Replace inconsistent names
df["state"] = df["state"].replace({
    "delhi UT": "delhi",
    "a&n islands": "andaman & nicobar",
    "d&a haveli": "dadra & nagar haveli",
    "d & n haveli": "dadra & nagar haveli",
    "d&n haveli": "dadra & nagar haveli"
})

# Convert back to proper title format
df["state"] = df["state"].str.title()


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

# -----------------------------
# HEATMAP
# -----------------------------

# Keep only important states
state_totals = df.groupby("state")[
    "Total_Crimes"
].sum()

important_states = state_totals[
    state_totals > 5000
].index

df = df[df["state"].isin(important_states)]

pivot_table = df.pivot_table(
    values="Total_Crimes",
    index="state",
    columns="Year",
    aggfunc="sum"
)

# Sort states by total crimes
pivot_table = pivot_table.loc[
    pivot_table.sum(axis=1).sort_values(
        ascending=False
    ).index
]

plt.figure(figsize=(16,12))

sns.heatmap(
    pivot_table,
    cmap="Reds",
    linewidths=0.5,
    linecolor="white",
    cbar_kws={"shrink": 0.8}
)

plt.xticks(fontsize=10)
plt.yticks(fontsize=11)

plt.title(
    "State-wise Crime Intensity Heatmap (2001–2014)",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel(
    "Year",
    fontsize=12
)

plt.ylabel(
    "State",
    fontsize=12
)

plt.savefig(
    "final_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

highest_state = (
    df.groupby("state")["Total_Crimes"]
    .sum()
    .idxmax()
)

print(
    f"\nState with highest crimes: {highest_state}"
)
