import matplotlib.pyplot as plt
import numpy as np

# Data from the practical example
temperature = np.array([20, 30, 40, 50, 60], dtype=float)
pressure = np.array([101.5, 104.2, 107.1, 109.8, 112.6], dtype=float)

# Simple linear regression using first and last observations
b1 = (pressure[-1] - pressure[0]) / (temperature[-1] - temperature[0])
b0 = pressure[0] - b1 * temperature[0]

predicted = b0 + b1 * temperature
residuals = pressure - predicted
mae = np.mean(np.abs(residuals))
mse = np.mean(residuals ** 2)

# Smooth line for plotting the regression equation
x_line = np.linspace(temperature.min() - 2, temperature.max() + 2, 100)
y_line = b0 + b1 * x_line

# Create side-by-side subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "Temperature vs. Pressure — Simple Linear Regression",
    fontsize=14,
    fontweight="bold",
)

# --- Panel 1: Actual vs. Predicted Regression Line ---
ax1.plot(
    x_line,
    y_line,
    color="#E05A2B",
    linewidth=2,
    label=f"Regression Line: $\\hat{{Y}} = {b0:.2f} + {b1:.4f}X$",
)
ax1.scatter(
    temperature,
    pressure,
    color="#1B4F72",
    s=70,
    zorder=5,
    label="Actual Observations",
)
ax1.scatter(
    temperature,
    predicted,
    color="#E05A2B",
    marker="x",
    s=60,
    zorder=6,
    label="Predicted Values",
)

# Draw vertical error lines between actual and predicted points
for x_val, y_act, y_pred in zip(temperature, pressure, predicted):
    ax1.vlines(x_val, y_pred, y_act, color="gray", linestyle="--", linewidth=1)

# Metrics callout box
metrics_text = (
    f"Slope ($b_1$): {b1:.4f}\n"
    f"Intercept ($b_0$): {b0:.2f}\n"
    f"MAE: {mae:.4f} kPa\n"
    f"MSE: {mse:.6f} kPa²\n"
    f"Correlation: Positive"
)
ax1.text(
    0.05,
    0.95,
    metrics_text,
    transform=ax1.transAxes,
    fontsize=9.5,
    verticalalignment="top",
    bbox={"boxstyle": "round,pad=0.5", "facecolor": "#F8F9F9", "edgecolor": "#BDC3C7"},
)

ax1.set_title("Regression Fit")
ax1.set_xlabel("Temperature (°C)")
ax1.set_ylabel("Pressure (kPa)")
ax1.grid(True, linestyle=":", alpha=0.6)
ax1.legend(loc="lower right")

# --- Panel 2: Zoomed-in Residuals (Actual - Predicted) ---
bar_colors = ["#2E86C1" if r >= 0 else "#C0392B" for r in residuals]
bars = ax2.bar(temperature, residuals, width=4, color=bar_colors, edgecolor="black", alpha=0.85)
ax2.axhline(0, color="black", linewidth=1)
ax2.axhline(mae, color="#27AE60", linestyle="--", linewidth=1.2, label=f"+MAE ({mae:.3f})")
ax2.axhline(-mae, color="#27AE60", linestyle="--", linewidth=1.2, label=f"-MAE (-{mae:.3f})")

# Label exact error above/below each bar
for bar, err in zip(bars, residuals):
    offset = 0.004 if err >= 0 else -0.009
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        err + offset,
        f"{err:+.3f}",
        ha="center",
        va="bottom" if err >= 0 else "top",
        fontsize=9,
    )

ax2.set_title("Residuals ($y - \\hat{y}$)")
ax2.set_xlabel("Temperature (°C)")
ax2.set_ylabel("Prediction Error (kPa)")
ax2.set_xticks(temperature)
ax2.set_ylim(-0.10, 0.08)
ax2.grid(True, axis="y", linestyle=":", alpha=0.6)
ax2.legend(loc="lower right")

plt.tight_layout()
plt.savefig("regression_visualisation.png", dpi=150)
plt.show()