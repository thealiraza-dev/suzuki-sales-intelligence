import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("suzuki_sales_data.csv")

# -------------------------------
# STYLE (cleaner visuals)
# -------------------------------
plt.style.use("seaborn-v0_8-darkgrid")

# -------------------------------
# CREATE FIGURE LAYOUT
# -------------------------------
fig = plt.figure(figsize=(15, 10))

# -------------------------------
# 1. MODEL PERFORMANCE
# -------------------------------
ax1 = plt.subplot(2, 2, 1)
model_sales = df.groupby("Model")["Sales_Units"].sum().sort_values()
model_sales.plot(kind="bar", color="skyblue", ax=ax1)
ax1.set_title("📊 Model Performance")
ax1.set_ylabel("Total Sales")

# -------------------------------
# 2. CITY PERFORMANCE
# -------------------------------
ax2 = plt.subplot(2, 2, 2)
city_sales = df.groupby("City")["Sales_Units"].sum().sort_values()
city_sales.plot(kind="bar", color="orange", ax=ax2)
ax2.set_title("🌍 City Performance")
ax2.set_ylabel("Total Sales")

# -------------------------------
# 3. INFLATION VS SALES
# -------------------------------
ax3 = plt.subplot(2, 2, 3)
ax3.scatter(df["Inflation_Rate"], df["Sales_Units"], alpha=0.5, color="red")
ax3.set_title("📉 Inflation vs Sales Impact")
ax3.set_xlabel("Inflation Rate")
ax3.set_ylabel("Sales Units")

# -------------------------------
# 4. OVERALL SALES TREND (SIMULATED)
# -------------------------------
ax4 = plt.subplot(2, 2, 4)
df_sorted = df.sort_values("Date")
ax4.plot(df_sorted["Sales_Units"].values, color="green")
ax4.set_title("📈 Sales Trend Over Time (Simulated)")
ax4.set_ylabel("Sales Units")

# -------------------------------
# FINAL LAYOUT
# -------------------------------
plt.suptitle("🚗 Suzuki Sales Intelligence Dashboard (BI View)", fontsize=16)
plt.tight_layout()

# Save dashboard
plt.savefig("suzuki_bi_dashboard.png")

plt.show()