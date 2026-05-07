import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("cleaned_dataset.csv")

# Calculate average attendance and average marks
avg_attendance = df['Attendance'].mean()
avg_marks = df['Total_Marks'].mean()

# Categorize students automatically using averages
high_att_high_marks = df[
    (df['Attendance'] >= avg_attendance) &
    (df['Total_Marks'] >= avg_marks)
]

high_att_low_marks = df[
    (df['Attendance'] >= avg_attendance) &
    (df['Total_Marks'] < avg_marks)
]

# Print results
print("Average Attendance:", avg_attendance)
print("Average Marks:", avg_marks)

print("\nHigh Attendance + High Marks Students:")
print(high_att_high_marks)

print("\nHigh Attendance + Low Marks Students:")
print(high_att_low_marks)

# ---------------- SCATTER PLOT ----------------

plt.figure(figsize=(10,6))

# High Attendance + High Marks
plt.scatter(
    high_att_high_marks['Attendance'],
    high_att_high_marks['Total_Marks'],
    label='High Attendance + High Marks'
)

# High Attendance + Low Marks
plt.scatter(
    high_att_low_marks['Attendance'],
    high_att_low_marks['Total_Marks'],
    label='High Attendance + Low Marks'
)

plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.title("Attendance vs Total Marks")
plt.legend()
plt.grid(True)

plt.show()

# ---------------- BAR GRAPH ----------------

categories = [
    'High Attendance + High Marks',
    'High Attendance + Low Marks'
]

counts = [
    len(high_att_high_marks),
    len(high_att_low_marks)
]

plt.figure(figsize=(8,5))
plt.bar(categories, counts)

plt.ylabel("Number of Students")
plt.title("Student Categories")

plt.show()