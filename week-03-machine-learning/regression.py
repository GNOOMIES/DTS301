from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parent / "student-mat.csv"


def load_data():
    return pd.read_csv(DATA_PATH, sep=";")


# ==========================================
# TASK RUNNERS
# ==========================================


def run_task_1(df):
    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- (a) Shape & Columns ---")
    print("Shape (rows, columns):", df.shape)
    print("Columns:", list(df.columns))

    print("\n--- (b) Statistical Summary ---")
    print(df.describe())

    print("\n--- (c) Missing Values ---")
    print(df.isnull().sum())

    print("\n--- (d) Duplicated Rows ---")
    print("Duplicated rows:", df.duplicated().sum())

    print("\n--- (e) Data Types ---")
    print(df.dtypes)


def run_task_2(df):
    corr_matrix = df.corr(numeric_only=True)

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Correlation Heatmap - Student Performance Dataset")
    plt.tight_layout()
    plt.show()

    df.hist(bins=15, figsize=(14, 10), edgecolor="black")
    plt.suptitle("Histograms of Numeric Features")
    plt.tight_layout()
    plt.show()

def run_task_3(df):
    X = df[["G2"]]
    y = df["G3"]

    # --- Base Model: 80/20 Train/Test Split ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae_80 = mean_absolute_error(y_test, y_pred)
    mse_80 = mean_squared_error(y_test, y_pred)
    rmse_80 = np.sqrt(mse_80)

    print("80/20 Split (G2 -> G3):")
    print(f"  Slope (b1):     {model.coef_[0]:.4f}")
    print(f"  Intercept (b0): {model.intercept_:.4f}")
    print(f"  MAE:            {mae_80:.4f}")
    print(f"  MSE:            {mse_80:.4f}")
    print(f"  RMSE:           {rmse_80:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(X_test["G2"], y_test, color="blue", alpha=0.7, label="Actual G3")
    plt.plot(X_test["G2"], y_pred, color="red", linewidth=2, label="Predicted G3")
    plt.title("Linear Regression: G2 vs G3 (80/20 Split)")
    plt.xlabel("Second Period Grade (G2)")
    plt.ylabel("Final Grade (G3)")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.show()

    # --- Task 3b: 70/30 Train/Test Split ---
    X_train_70, X_test_70, y_train_70, y_test_70 = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model_70 = LinearRegression()
    model_70.fit(X_train_70, y_train_70)
    y_pred_70 = model_70.predict(X_test_70)

    mae_70 = mean_absolute_error(y_test_70, y_pred_70)
    mse_70 = mean_squared_error(y_test_70, y_pred_70)
    rmse_70 = np.sqrt(mse_70)

    print("\n70/30 Split (G2 -> G3):")
    print(f"  MAE:  {mae_70:.4f}")
    print(f"  MSE:  {mse_70:.4f}")
    print(f"  RMSE: {rmse_70:.4f}")


def run_task_3c(df):
    # Only numeric columns can be used in LinearRegression (strings like 'sex' or 'school' will fail)
    features_to_test = ["G2", "G1", "failures"]
    y = df["G3"]

    best_feature = None
    lowest_mse = float("inf")

    for feature in features_to_test:
        X = df[[feature]]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)

        print(f"Feature '{feature}' -> MAE: {mae:.4f} | MSE: {mse:.4f}")

        if mse < lowest_mse:
            lowest_mse = mse
            best_feature = feature

    # Comment for Task 3c:
    # G2 is the best single predictor for G3 because it achieves the lowest MAE and MSE.
    # This matches the heatmap, where G2 has the strongest positive correlation with G3 (~0.90).
    print(f"\nBest single predictor: {best_feature} (Lowest MSE: {lowest_mse:.4f})")

def run_task_3d(df):
    # Selected top correlated numeric features from the Task 2 heatmap
    multi_features = ["G1", "G2", "failures", "absences", "studytime"]
    X = df[multi_features]
    y = df["G3"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Multiple Features: {multi_features}")
    print(f"  Intercept (b0): {model.intercept_:.4f}")
    for name, coef in zip(multi_features, model.coef_):
        print(f"  Weight for {name:<10}: {coef:+.4f}")

    print(f"\n  Multi-Feature MAE: {mae:.4f}")
    print(f"  Multi-Feature MSE: {mse:.4f}")
    # Note: No plot here because 5 input features + 1 target requires a 6D graph.

def run_task_3e():
    # Update these 3 lines to match the CSV you downloaded from UCI or Kaggle
    second_file = Path(__file__).resolve().parent / "your_dataset.csv"
    separator = ","          # Change to ";" if your CSV uses semicolons
    target_col = "target"    # Exact column name you want to predict

    if not second_file.exists():
        print(f"Dataset not found at: {second_file}")
        print("Download a CSV from UCI or Kaggle and place it in week-03-machine-learning/.")
        return

    df2 = pd.read_csv(second_file, sep=separator)
    print("\n--- Second Dataset: Shape & First 5 Rows ---")
    print("Shape:", df2.shape)
    print(df2.head())
    print("\nMissing values:\n", df2.isnull().sum())

    # Drop any rows with missing values and keep numeric columns for regression
    numeric_df = df2.select_dtypes(include=[np.number]).dropna()
    corr = numeric_df.corr()

    plt.figure(figsize=(10, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title(f"Correlation Heatmap - {second_file.name}")
    plt.tight_layout()
    plt.show()

    # Automatically pick all numeric columns except the target as features
    feature_cols = [col for col in numeric_df.columns if col != target_col]
    X = numeric_df[feature_cols]
    y = numeric_df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"\nMultiple Linear Regression on '{second_file.name}' (Target: {target_col})")
    print(f"  Features used: {feature_cols}")
    print(f"  MAE: {mean_absolute_error(y_test, y_pred):.4f}")
    print(f"  MSE: {mean_squared_error(y_test, y_pred):.4f}")

# ==========================================
# MENU SYSTEM
# ==========================================


def main():
    df = load_data()

    tasks = {
        "1": ("Task 1: Load & Explore Dataset", lambda: run_task_1(df)),
        "2": ("Task 2: Heatmap & Histograms", lambda: run_task_2(df)),
        "3": ("Task 3: Single-Variable Regression (80/20 & 70/30)", lambda: run_task_3(df)),
        "3c": ("Task 3c: Compare 3 Numeric Variables", lambda: run_task_3c(df)),
        "3d": ("Task 3d: Multiple Linear Regression", lambda: run_task_3d(df)),
        "3e": ("Task 3e: Repeat on a Second Dataset", run_task_3e),
    }

    while True:
        print("\n" + "=" * 40)
        print(" DTS301 Workshop 3: Regression Menu ")
        print("=" * 40)
        for key, (desc, _) in tasks.items():
            print(f"[{key}] {desc}")
        print("[q] Quit")

        choice = input("\nSelect a task to run: ").strip().lower()

        if choice == "q":
            break
        elif choice in tasks:
            print(f"\n=== Running {tasks[choice][0]} ===")
            tasks[choice][1]()
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()