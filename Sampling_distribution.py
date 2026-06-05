import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

# -------------------------------
# STEP 1: Population Mean
# -------------------------------
population_mean_attendance = df["Attendance"].mean()
population_mean_marks = df["Total_Marks"].mean()

print("Population Mean Attendance:", population_mean_attendance)
print("Population Mean Total Marks:", population_mean_marks)


# -------------------------------
# STEP 2: Generate Multiple Samples
# -------------------------------
sample_means_attendance = []
sample_means_marks = []

num_samples = 30
sample_size = 50

for i in range(num_samples):

    sample = df.sample(n=sample_size)

    sample_means_attendance.append(sample["Attendance"].mean())
    sample_means_marks.append(sample["Total_Marks"].mean())


# -------------------------------
# STEP 3: Mean of Sample Means
# -------------------------------
mean_of_sample_means_attendance = np.mean(sample_means_attendance)
mean_of_sample_means_marks = np.mean(sample_means_marks)

print("\nMean of Sample Means (Attendance):", mean_of_sample_means_attendance)
print("Mean of Sample Means (Marks):", mean_of_sample_means_marks)


# -------------------------------
# STEP 4: Comparison
# -------------------------------
comparison = pd.DataFrame({
    "Metric": ["Attendance", "Total Marks"],
    "Population Mean": [
        population_mean_attendance,
        population_mean_marks
    ],
    "Mean of Sample Means": [
        mean_of_sample_means_attendance,
        mean_of_sample_means_marks
    ]
})

print("\nComparison Table:")
print(comparison)


# -------------------------------
# STEP 5: Histogram - Attendance
# -------------------------------
plt.figure(figsize=(8,5))

plt.hist(sample_means_attendance, bins=10)

plt.axvline(
    population_mean_attendance,
    linestyle='dashed',
    linewidth=2,
    label='Population Mean'
)

plt.title("Sampling Distribution of Attendance Means")
plt.xlabel("Sample Mean Attendance")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# -------------------------------
# STEP 6: Histogram - Marks
# -------------------------------
plt.figure(figsize=(8,5))

plt.hist(sample_means_marks, bins=10)

plt.axvline(
    population_mean_marks,
    linestyle='dashed',
    linewidth=2,
    label='Population Mean'
)

plt.title("Sampling Distribution of Total Marks Means")
plt.xlabel("Sample Mean Total Marks")
plt.ylabel("Frequency")
plt.legend()

plt.show()


# -------------------------------
# STEP 7: Save Results
# -------------------------------
results = pd.DataFrame({
    "Attendance Sample Means": sample_means_attendance,
    "Marks Sample Means": sample_means_marks
})

results.to_csv("sampling_distribution_results.csv", index=False)

print("\nSampling distribution analysis complete.")