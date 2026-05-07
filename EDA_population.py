# loading dataset
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset.csv")
print(df.shape)
print(df.columns)
print(df.info())

# all statistics of dataset
print(df.describe())

# Attendence vs Number of students
plt.hist(df["Attendance"], bins=10)
plt.xlabel("Attendance")
plt.ylabel("Number of Students")
plt.title("Attendance Distribution")
plt.show()

# marks vs Number of students
plt.hist(df["Total_Marks"], bins=10)
plt.xlabel("Total Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")
plt.show()


# Attendence vs Total marks
plt.scatter(df["Attendance"], df["Total_Marks"])
plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.title("Attendance vs Total Marks")
plt.show()

# study hours vs total marks 
plt.scatter(df["Study_Hours"], df["Total_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Total Marks")
plt.title("Study Hours vs Total Marks")
plt.show()

# Average marks 
mode_avg = df.groupby("Mode")["Total_Marks"].mean()

mode_avg.plot(kind="bar")
plt.ylabel("Average Marks")
plt.title("Average Marks by Mode")
plt.show()


plt.boxplot(df["Attendance"])
plt.title("Attendance Boxplot")
plt.show()

# correaltion matrix
print("/n/n Correlation Matrix",df.corr(numeric_only=True))