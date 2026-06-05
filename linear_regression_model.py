# ==============================
# SIMPLE LINEAR REGRESSION MODEL
# Attendance vs Academic Performance
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# -----------------------------
# STEP 1: Load dataset
# -----------------------------
df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)


# -----------------------------
# STEP 2: Define Variables
# -----------------------------
X = df[["Attendance"]]       # Independent Variable
y = df["Total_Marks"]        # Dependent Variable


# -----------------------------
# STEP 3: Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Set Size:", X_train.shape)
print("Testing Set Size:", X_test.shape)


# -----------------------------
# STEP 4: Train Model
# -----------------------------
model = LinearRegression()
model.fit(X_train, y_train)


# -----------------------------
# STEP 5: Predictions on Test Data
# -----------------------------
y_pred = model.predict(X_test)


# -----------------------------
# STEP 6: Regression Equation
# -----------------------------
slope = model.coef_[0]
intercept = model.intercept_

print("\n===== REGRESSION EQUATION =====")
print(f"Total Marks = {slope:.2f} × Attendance + {intercept:.2f}")


# -----------------------------
# STEP 7: Model Evaluation
# -----------------------------
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.2f}")


# -----------------------------
# STEP 8: Visualization
# -----------------------------
plt.figure(figsize=(8,6))

plt.scatter(X_test, y_test, label="Actual Data")
plt.plot(X_test, y_pred, linewidth=2, label="Regression Line")

plt.xlabel("Attendance (%)")
plt.ylabel("Total Marks")
plt.title("Simple Linear Regression: Attendance vs Total Marks")
plt.legend()

plt.show()


# -----------------------------
# STEP 9: User Input Prediction
# -----------------------------
attendance_input = float(input("\nEnter Attendance Percentage to Predict Marks: "))

new_student = pd.DataFrame({
    "Attendance": [attendance_input]
})

predicted_marks = model.predict(new_student)

print("\n===== PREDICTION =====")
print(f"For Attendance = {attendance_input}%")
print(f"Predicted Total Marks = {predicted_marks[0]:.2f}")