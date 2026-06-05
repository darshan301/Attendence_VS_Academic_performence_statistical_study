import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# =====================================
# STEP 1: Create Random Sample
# =====================================
sample_random = df.sample(n=100, random_state=42)

# Save sample
sample_random.to_csv("random_sample.csv", index=False)

print("Random sample created successfully.")
print(sample_random.shape)


# =====================================
# STEP 2: Compare Population vs Sample
# =====================================
population_mean = df[["Attendance", "Total_Marks", "CGPA", "Study_Hours"]].mean()

sample_mean = sample_random[
    ["Attendance", "Total_Marks", "CGPA", "Study_Hours"]
].mean()

comparison = pd.DataFrame({
    "Population Mean": population_mean,
    "Random Sample Mean": sample_mean
})

print("\nPopulation vs Random Sample Comparison:")
print(comparison)


# =====================================
# STEP 3: Attendance vs Marks Scatter
# =====================================
plt.figure(figsize=(8,5))

plt.scatter(
    sample_random["Attendance"],
    sample_random["Total_Marks"]
)

plt.title("Attendance vs Total Marks (Random Sample)")
plt.xlabel("Attendance (%)")
plt.ylabel("Total Marks")

plt.show()


# =====================================
# STEP 4: Mode Comparison
# =====================================
mode_avg = sample_random.groupby("Mode")["Total_Marks"].mean()

plt.figure(figsize=(6,4))

mode_avg.plot(kind="bar")

plt.title("Average Marks by Mode (Random Sample)")
plt.xlabel("Mode")
plt.ylabel("Average Total Marks")

plt.show()


# =====================================
# STEP 5: Correlation
# =====================================
corr = sample_random[
    ["Attendance", "Total_Marks", "CGPA", "Study_Hours"]
].corr()

print("\nCorrelation Matrix:")
print(corr)

corr.to_csv("random_sample_correlation.csv")


print("\nRandom Sampling Analysis Complete.")