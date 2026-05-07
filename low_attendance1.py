import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# LOAD POPULATION DATASET
# -----------------------------------

df = pd.read_csv("cleaned_dataset.csv")

# -----------------------------------
# CREATE SAMPLES
# -----------------------------------

# Low Attendance + High Marks
low_att_high_marks = df[
    (df["Attendance"] < 75) &
    (df["Total_Marks"] >= 70)
]

# Low Attendance + Low Marks
low_att_low_marks = df[
    (df["Attendance"] < 75) &
    (df["Total_Marks"] < 70)
]

# -----------------------------------
# SAVE SAMPLE DATASETS
# -----------------------------------



# -----------------------------------
# DISPLAY SAMPLE INFORMATION
# -----------------------------------

print("Low Attendance + High Marks Sample Shape:")
print(low_att_high_marks.shape)

print("\nLow Attendance + Low Marks Sample Shape:")
print(low_att_low_marks.shape)

# -----------------------------------
# GRAPH 1
# LOW ATTENDANCE + HIGH MARKS
# -----------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    low_att_high_marks["Attendance"],
    low_att_high_marks["Total_Marks"]
)

plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.title("Low Attendance + High Marks")

plt.grid(True)

plt.show()

# -----------------------------------
# GRAPH 2
# LOW ATTENDANCE + LOW MARKS
# -----------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    low_att_low_marks["Attendance"],
    low_att_low_marks["Total_Marks"]
)

plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.title("Low Attendance + Low Marks")

plt.grid(True)

plt.show()

# -----------------------------------
# COMPARISON BAR CHART
# -----------------------------------

categories = [
    "Low Attendance + High Marks",
    "Low Attendance + Low Marks"
]

average_marks = [
    low_att_high_marks["Total_Marks"].mean(),
    low_att_low_marks["Total_Marks"].mean()
]

plt.figure(figsize=(8, 6))

plt.bar(categories, average_marks)

plt.xlabel("Student Groups")
plt.ylabel("Average Total Marks")
plt.title("Comparison of Student Groups")

plt.grid(axis='y')

plt.show()