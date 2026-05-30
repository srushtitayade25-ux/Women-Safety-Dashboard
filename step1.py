# ---------------------------------------------------------
# WOMEN SAFETY DATA ANALYSIS PROJECT
# ---------------------------------------------------------
# This project analyzes crimes against women in India
# using Python and Pandas.
#
# Steps performed in this analysis:
# 1. Loaded the dataset using Pandas
# 2. Explored dataset structure and columns
# 3. Checked dataset shape and missing values
# 4. Removed duplicate records
# 5. Standardized column names for consistency
# 6. Created a new feature: total_crimes
# 7. Performed yearly crime trend analysis
# 8. Grouped and summarized crime statistics
#
# Tools & Libraries Used:
# - Python
# - Pandas
#
# Project Goal:
# To identify crime trends, patterns, and insights
# related to crimes against women from 2001–2014.
# ---------------------------------------------------------
import pandas as pd
# Load dataset
df = pd.read_csv("crime.csv")

# Show first 5 rows
print(df.head())

# Show column names
print("\nColumns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower()

print(df.head())

# Create total crimes column
df["total_crimes"] = (
    df["rape"] +
    df["kidnapping and abduction"] +
    df["dowry deaths"] +
    df["assault on women with intent to outrage her modesty"] +
    df["insult to modesty of women"] +
    df["cruelty by husband or his relatives"] +
    df["importation of girls"]
)

# Group by state
yearly_crimes = df.groupby("year")[
    "total_crimes"
].sum()

# Sort descending
yearly_crimes = yearly_crimes.sort_values(ascending=False)

# Print result
print(yearly_crimes)
