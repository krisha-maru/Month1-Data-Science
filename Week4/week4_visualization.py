import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
np.random.seed(42)
n = 120
study_hours = np.clip(np.random.normal(5.5, 1.8, n), 1, 10)
attendance = np.clip(np.random.normal(82, 10, n), 50, 100)
sleep_hours = np.clip(np.random.normal(7, 1.0, n), 4, 10)
marks = np.clip(35 + study_hours * 6 + attendance * 0.35 + sleep_hours * 2 + np.random.normal(0, 6, n), 40, 100)

performance = pd.cut(
    marks,
    bins=[0, 60, 75, 100],
    labels=["Average", "Good", "Excellent"]
)

df = pd.DataFrame({
    "StudyHours": study_hours.round(1),
    "Attendance": attendance.round(1),
    "SleepHours": sleep_hours.round(1),
    "Marks": marks.round(1),
    "Performance": performance
})

df.to_csv("week4_sample_dataset.csv", index=False)

print("First 5 rows of dataset:")
print(df.head())

# Scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(df["StudyHours"], df["Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.tight_layout()
plt.savefig("scatter_plot.png", dpi=200)
plt.show()

# Histogram
plt.figure(figsize=(7, 5))
plt.hist(df["Marks"], bins=12)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
plt.tight_layout()
plt.savefig("histogram.png", dpi=200)
plt.show()

# Heatmap
plt.figure(figsize=(7, 5))
corr = df[["StudyHours", "Attendance", "SleepHours", "Marks"]].corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png", dpi=200)
plt.show()

# Pairplot-style dashboard
grid = sns.PairGrid(df[["StudyHours", "Attendance", "SleepHours", "Marks"]])
grid.map_upper(plt.scatter)
grid.map_lower(plt.scatter)
grid.map_diag(plt.hist)
grid.fig.suptitle("Pairplot of Student Features", y=1.02)
grid.savefig("pairplot.png", dpi=200)
plt.show()

# Basic insights
print("\nAverage marks:", df["Marks"].mean())
print("Maximum marks:", df["Marks"].max())
print("Minimum marks:", df["Marks"].min())
print("\nAverage marks by performance category:")
print(df.groupby("Performance", observed=False)["Marks"].mean())
