# ==========================================
# MULTIPLE REGRESSION MODEL
# Attendance vs Academic Performance
# ==========================================

import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ------------------------------------------
# STEP 1: Load Dataset
# ------------------------------------------

df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)

# ------------------------------------------
# STEP 2: Encode Mode
# ------------------------------------------

df["Mode"] = df["Mode"].map({
    "Online": 0,
    "Offline": 1
})

# ------------------------------------------
# STEP 3: Features and Target
# ------------------------------------------

X = df[
    [
        "Attendance",
        "Study_Hours",
        "Mode"
    ]
]

y = df["Total_Marks"]

# ------------------------------------------
# STEP 4: Train-Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ------------------------------------------
# STEP 5: Train Model
# ------------------------------------------

model = LinearRegression()

model.fit(X_train, y_train)

# ------------------------------------------
# STEP 6: Predictions
# ------------------------------------------

y_pred = model.predict(X_test)

# ------------------------------------------
# STEP 7: Regression Equation
# ------------------------------------------

intercept = model.intercept_

attendance_coef = model.coef_[0]
study_coef = model.coef_[1]
mode_coef = model.coef_[2]

print("\n==============================")
print("REGRESSION EQUATION")
print("==============================")

print(
    f"Total Marks = {intercept:.2f}"
    f" + ({attendance_coef:.2f} × Attendance)"
    f" + ({study_coef:.2f} × Study_Hours)"
    f" + ({mode_coef:.2f} × Mode)"
)

# ------------------------------------------
# STEP 8: Model Evaluation
# ------------------------------------------

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")

print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# ------------------------------------------
# STEP 9: User Prediction
# ------------------------------------------

print("\n==============================")
print("PREDICT STUDENT MARKS")
print("==============================")

# Attendance Validation
attendance = float(
    input("Enter Attendance (%): ")
)

while attendance < 0 or attendance > 100:
    attendance = float(
        input("Attendance must be between 0 and 100: ")
    )

# Study Hours Validation
study_hours = float(
    input("Enter Study Hours: ")
)

while study_hours < 0 or study_hours > 10:
    study_hours = float(
        input("Study Hours must be between 0 and 10: ")
    )

# Mode Validation
mode = input(
    "Enter Mode (Online/Offline): "
).strip().lower()

while mode not in ["online", "offline"]:
    mode = input(
        "Please enter Online or Offline: "
    ).strip().lower()

# Encode Mode
mode_value = 0 if mode == "online" else 1

# Create DataFrame for prediction
new_student = pd.DataFrame({
    "Attendance": [attendance],
    "Study_Hours": [study_hours],
    "Mode": [mode_value]
})

# Predict
predicted_marks = model.predict(new_student)[0]

# ------------------------------------------
# STEP 10: Restrict Prediction Range
# ------------------------------------------

predicted_marks = max(
    0,
    min(100, predicted_marks)
)

# ------------------------------------------
# STEP 11: Display Prediction
# ------------------------------------------

print("\n==============================")
print("PREDICTION RESULT")
print("==============================")

print(
    f"Predicted Total Marks = "
    f"{predicted_marks:.2f}"
)

# ------------------------------------------
# STEP 12: Interpretation
# ------------------------------------------

print("\nInterpretation:")

if predicted_marks >= 75:
    print("Expected Performance: High")

elif predicted_marks >= 50:
    print("Expected Performance: Average")

else:
    print("Expected Performance: Low")