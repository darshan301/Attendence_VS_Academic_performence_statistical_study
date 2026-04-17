import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# data loading
df = pd.read_csv("attendance_performance_updated.csv")
print(df.head())
print(df.info())

# data cleaning

print(df.isnull().sum())
    # Remove rows where Student_ID is missing
df = df.dropna(subset=["Student_ID"])
    # Optional: reset index after dropping rows
df.reset_index(drop=True, inplace=True)
print('\n Null values in Student_id Column is ',df["Attendance"].isnull().sum())

# handling attendence missing values
df["Attendance"] = df.groupby("Mode")["Attendance"].transform(
    lambda x: x.fillna(x.mean()))
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
print('\n Null values in Attendence Column is ',df["Attendance"].isnull().sum())

# Handling Internal marks,Final marks and Total Marks columns 
# Step 1: Count missing values in the 3 columns
cols = ["Internal_Marks", "Final_Marks", "Total_Marks"]
df["missing_count"] = df[cols].isnull().sum(axis=1)

# Step 2: Drop rows where 2 or more values are missing
df = df[df["missing_count"] < 2]

# Step 3: Fill missing values using logic
# Internal = Total - Final
mask_internal = df["Internal_Marks"].isnull()
df.loc[mask_internal, "Internal_Marks"] = (
    df.loc[mask_internal, "Total_Marks"] - df.loc[mask_internal, "Final_Marks"]
)
# Final = Total - Internal
mask_final = df["Final_Marks"].isnull()
df.loc[mask_final, "Final_Marks"] = (
    df.loc[mask_final, "Total_Marks"] - df.loc[mask_final, "Internal_Marks"]
)
# Total = Internal + Final
mask_total = df["Total_Marks"].isnull()
df.loc[mask_total, "Total_Marks"] = (
    df.loc[mask_total, "Internal_Marks"] + df.loc[mask_total, "Final_Marks"]

)
# Step 4: Drop helper column
df.drop(columns=["missing_count"], inplace=True)

print('\n Null values in Internal_Marks Column is ',df["Internal_Marks"].isnull().sum())
print('\n Null values in Final_Marks Column is ',df["Final_Marks"].isnull().sum())
print('\n Null values in Total_Marks Column is ',df["Total_Marks"].isnull().sum())

# Handling CGPA values

df["CGPA"]=df["Total_Marks"]/10
print('\n Null values in CGPA Column is ',df["CGPA"].isnull().sum())


# Handling study hours missing values
# Step 1: Performance-based
df["Study_Hours"] = df.groupby(pd.cut(df["Total_Marks"], bins=4),observed=True)["Study_Hours"].transform(
    lambda x: x.fillna(x.mean()))
# Step 2: Fallback
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
print('\n Null values in Study_hours Column is ',df["Study_Hours"].isnull().sum())

# handling mode column

df["Mode"] = df["Mode"].fillna(df["Mode"].mode()[0])
print('\n Null values in Mode Column is ',df["Mode"].isnull().sum())

print('\n',df.isnull().sum())
